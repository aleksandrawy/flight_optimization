import time

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from math import sin, cos, sqrt, atan2, radians
import json
from geopy.geocoders import Nominatim


class Functions():

    polygon = None
    waypoints_list = []
    plane = None

    def calculate_distance(self, p1, p2):
        #lat1, lat2, lon1, lon2 = 0.0
        with open("waypoints_filtered.json", encoding='utf-8') as input_file:
            w_data = json.load(input_file)

        with open("airports.geojson", encoding='utf-8') as input_file:
            a_data = json.load(input_file)

        if len(p1) <= 9:
            for i in w_data:
                if i["properties"]["Name"] == p1:
                    lat1 = radians(i["geometry"]["coordinates"][1])
                    lon1 = radians(i["geometry"]["coordinates"][0])
        else:
            for i in a_data["features"]:
                if i["properties"]["name"] == p1:
                    lat1 = radians(i["geometry"]["coordinates"][1])
                    lon1 = radians(i["geometry"]["coordinates"][0])

        if len(p2) <= 9:
            for i in w_data:
                if i["properties"]["Name"] == p2:
                    lat2 = radians(i["geometry"]["coordinates"][1])
                    lon2 = radians(i["geometry"]["coordinates"][0])
        else:
            for i in a_data["features"]:
                if i["properties"]["name"] == p2:
                    lat2 = radians(i["geometry"]["coordinates"][1])
                    lon2 = radians(i["geometry"]["coordinates"][0])


        # print(str(lat1) +", "+ str(lon1))
        # print(str(lat2) + ", " + str(lon2))
        # approximate radius of earth in km
        R = 6373.0

        # lat1 = radians(52.2296756)
        # lon1 = radians(21.0122287)
        # lat2 = radians(52.406374)
        # lon2 = radians(16.9251681)

        dlon = abs(lon2 - lon1)
        dlat = abs(lat2 - lat1)

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = R * c

        return distance

    def set_rectangle(self, airport1, airport2):
        with open("airports.geojson", encoding='utf-8') as input_file:
            data = json.load(input_file)
        for i in data["features"]:
            if i["properties"]["name"] == airport1:
                lat1 = radians(i["geometry"]["coordinates"][1])
                lon1 = radians(i["geometry"]["coordinates"][0])
            if i["properties"]["name"] == airport2:
                lat2 = radians(i["geometry"]["coordinates"][1])
                lon2 = radians(i["geometry"]["coordinates"][0])
        R = 6373.0
        dist = 150
        x1 = R * cos(lat1) * cos(lon1)
        y1 = R * cos(lat1) * sin(lon1)
        x2 = R * cos(lat2) * cos(lon2)
        y2 = R * cos(lat2) * sin(lon2)
        self.polygon = Polygon([((x1-dist), y1), ((x1+dist), y1), ((x2+dist), y2), ((x2-dist), y2)])

    def get_rectangle(self):
        return self.polygon

    def is_in_rectangle(self, point_name):
        # point = Point(1, 0.5)
        # polygon = Polygon([(0, 0), (0, 1), (1, 1), (1, 0)])
        # print(polygon.contains(point))
        with open("waypoints_filtered.json", encoding='utf-8') as input_file:
            data = json.load(input_file)
        for i in data:
            if i["properties"]["Name"] == point_name:
                lat = radians(i["geometry"]["coordinates"][1])
                lon = radians(i["geometry"]["coordinates"][0])

        R = 6373.0
        x = R * cos(lat) * cos(lon)
        y = R * cos(lat) * sin(lon)
        point = Point(x, y)
        return self.get_rectangle().contains(point)

    def get_points_from_rectangle(self):
        with open("waypoints_filtered.json", encoding='utf-8') as input_file:
            data = json.load(input_file)

        list = []

        for i in data:
            if self.is_in_rectangle(i["properties"]["Name"]):
                list.append(i)

        return list

    def get_closest_points(self, point):
        # with open("waypoints_filtered.json", encoding='utf-8') as input_file:
        #     data = json.load(input_file)

        closest = {}
        neigbours_number = 8
        start = time.time()
        print(start)

        waypoints_list = self.waypoints_list
        with open("waypoints_list.json", encoding='utf-8') as input_file:
            waypoints_list = json.load(input_file)

        for i in waypoints_list:
            if (i["properties"]["Name"] != point):
                dist = self.calculate_distance(point, i["properties"]["Name"])
                if len(closest) < neigbours_number:
                   # closest.append((i["properties"]["Name"], dist))
                   closest[i["properties"]["Name"]] = dist
                   #print(closest)
                else:
                    max = 0
                    for key, val in closest.items():
                        if val > max:
                            max = val
                            max_el = key
                    if max > dist:
                        del closest[max_el]
                        closest[i["properties"]["Name"]] = dist

                    # for n in range(len(closest)):
                    #     if closest[n][1] > max:
                    #         max = closest[n][1]
                    #         index_max_el = n
                    # if max > dist:
                    #     closest[index_max_el] = (i["properties"]["Name"], dist)
        #print(closest)
        print("CZAS: " + str(time.time() - start))
        # with open("closest.json", "w") as output_file:
        #     json.dump(closest, output_file, indent=4)

        return closest


    def set_graph(self, airport1, airport2):
        graph = {}

        start = time.time()
        self.set_rectangle(airport1, airport2)

        # self.waypoints_list = self.get_points_from_rectangle()
        # with open("waypoints_list.json", "w") as output_file:
        #     json.dump(self.waypoints_list, output_file, indent=4)
        with open("waypoints_list.json", encoding='utf-8') as input_file:
            self.waypoints_list = json.load(input_file)
        #graph.append({airport1 : self.get_closest_points(airport1)})
        graph[airport1] = self.get_closest_points(airport1)
        points_list = self.waypoints_list
        closest_to_end = self.get_closest_points(airport2)
        # graph.append({airport2: closest_to_end})
        graph[airport2] = closest_to_end
        for i in points_list:
                    #closest_points.append(airport2)
            closest_points = self.get_closest_points(i["properties"]["Name"])
            for key in closest_to_end:
                if i["properties"]["Name"] == key:
            #
            # for n in range(len(closest_to_end)):
            #     if i["properties"]["Name"] == closest_to_end[n][0]:
                    #closest_points.append([airport2, self.calculate_distance(closest_to_end[n][0], airport2)])
                    closest_points[airport2] = self.calculate_distance(key, airport2)
            #graph.append({i["properties"]["Name"] : closest_points})
            graph[i["properties"]["Name"]] = closest_points
        print("CZAS tworzenia grafu: " + str(time.time() - start))
        print(graph)
        with open("graf.json", "w") as output_file:
            json.dump(graph, output_file, indent=4)

    # def set_costs(self, graph):


    def calculate_travel_cost(self, p1, p2):
        with open("oplaty.json", encoding='utf-8') as input_file:
            costs = json.load(input_file)

        with open("waypoints_filtered.json", encoding='utf-8') as input_file:
            w_data = json.load(input_file)

        with open("airports.geojson", encoding='utf-8') as input_file:
            a_data = json.load(input_file)

        if len(p1) <= 9:
            for i in w_data:
                if i["properties"]["Name"] == p1:
                    lat1 = i["geometry"]["coordinates"][1]
                    lon1 = i["geometry"]["coordinates"][0]
        else:
            for i in a_data["features"]:
                if i["properties"]["name"] == p1:
                    lat1 = i["geometry"]["coordinates"][1]
                    lon1 = i["geometry"]["coordinates"][0]

        if len(p2) <= 9:
            for i in w_data:
                if i["properties"]["Name"] == p2:
                    lat2 = i["geometry"]["coordinates"][1]
                    lon2 = i["geometry"]["coordinates"][0]
        else:
            for i in a_data["features"]:
                if i["properties"]["name"] == p2:
                    lat2 = i["geometry"]["coordinates"][1]
                    lon2 = i["geometry"]["coordinates"][0]


        country1 = self.get_country_name(str(lat1), str(lon1))
        #country2 = self.get_country_name(str(lon2), str(lat2))

        for key in costs:
            if key == country1:
                cost = self.calculate_distance(p1, p2)/100 * float(costs[key]) * sqrt(self.get_mtow()/50)
        return cost

    def get_country_name(self, lat, lon):
        geolocator = Nominatim()
        loc = lat + ", " + lon
        location = geolocator.reverse(loc, language="pl")
        country = location.raw['address']['country']
        return country

    def set_plane(self, plane):
        with open("planes.json", encoding='utf-8') as input_file:
            planes = json.load(input_file)

        for p in planes:
            if p["name"] == plane:
                self.plane = p

    def get_mtow(self):
        mtow = self.plane["mtow"]
        mtow = mtow.replace(" ", "")
        return float(mtow)/1000

    def get_speed(self):
        return self.plane["speed"]

    def calculate_flight_time(self, p1, p2):
        km_h = int(self.get_speed()) * 1.852
        hours = self.calculate_distance(p1, p2) / km_h
        sec = hours*3600
        flight_sec = time.gmtime(sec)
        flight_time = time.strftime("%H:%M:%S", flight_sec)
        return hours, flight_time

    def calculate_fuel_consumption(self, p1, p2):
        return int(self.plane["fuel consumption"])/1000*self.calculate_distance(p1, p2)

    def calculate_all_costs(self, p1, p2):
        return (self.calculate_travel_cost(p1, p2)+self.calculate_flight_time(p1, p2)[0]+self.calculate_fuel_consumption(p1, p2))/3


fun = Functions()
# fun.calculate_distance("Young Airport", "MOSUD WYP")
# fun.calculate_distance("Gdańsk Lech Wałęsa Airport", "John Paul II International Airport Kraków-Balice Airport")
# fun.set_rectangle("Gdańsk Lech Wałęsa Airport", "John Paul II International Airport Kraków-Balice Airport")
# print(fun.is_in_rectangle("OLKIN WYP"))
# fun.get_closest_points("OLKIN WYP")
fun.set_plane("Boeing 737-400")
print(fun.calculate_travel_cost("Gdańsk Lech Wałęsa Airport", "Berlin-Tegel International Airport"))
print(fun.calculate_flight_time("Gdańsk Lech Wałęsa Airport", "John Paul II International Airport Kraków-Balice Airport")[1])
print(fun.calculate_fuel_consumption("Gdańsk Lech Wałęsa Airport", "John Paul II International Airport Kraków-Balice Airport"))
print(fun.calculate_all_costs("Gdańsk Lech Wałęsa Airport", "John Paul II International Airport Kraków-Balice Airport"))
#fun.set_graph("Gdańsk Lech Wałęsa Airport", "John Paul II International Airport Kraków-Balice Airport")