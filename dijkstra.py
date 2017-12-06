import json
import sys

class Dijkstra():

    done = False

    def unroll_shortest_path(self, current, optimal_parent_map, path=()):
        if current is None:  # Reached the start node
            return path
        else:
            return self.unroll_shortest_path(optimal_parent_map[current], optimal_parent_map, (current,) + path)


    def dijkstra(self, start_city, end_city, city_data, verbose=False):
        if start_city == end_city:
            return (start_city,)

        # Inefficiency: should be implemented as a priority queue
        start_city_distance_entry = [0, start_city]
        city_node_lookup = {start_city: start_city_distance_entry}
        unvisited = [start_city_distance_entry]
        visited = set()
        optimal_parent = {start_city: None}
        for city_name in city_data.keys():
            if city_name != start_city:
                city_distance_entry = [999999999, city_name]
                city_node_lookup[city_name] = city_distance_entry
                unvisited.append(city_distance_entry)

        destination_reached = False
        while not destination_reached and unvisited != []:
            (distance_to_current, current) = unvisited.pop(0)
            if verbose:
                print("CURRENT: {}, DISTANCE: {:,} meters".format(current, distance_to_current))
            visited.add(current)
            neighbors = city_data[current].keys()
            if verbose:
                print("\tNEIGHBORS:", list(neighbors))
            for neighbor in neighbors:
                if verbose:
                    print("\t\tNEIGHBOR: {}".format(neighbor))
                if neighbor == end_city:
                    destination_reached = True
                    optimal_parent[neighbor] = current
                    break
                elif neighbor not in visited:
                    total_distance_to_neighbor = distance_to_current + city_data[current][neighbor]
                    # Changing the distance here changes the distance in unvisited
                    city_distance_entry = city_node_lookup[neighbor]
                    if city_distance_entry[0] > total_distance_to_neighbor:
                        if verbose:
                            print("\t\t\tNEW OPTIMAL PARENT ({}) TO {}".format(current, neighbor))
                        city_distance_entry[0] = total_distance_to_neighbor
                        optimal_parent[neighbor] = current

            unvisited.sort()  # Needed in the abscence of heap

        if destination_reached:
            self.done = True
            return self.unroll_shortest_path(end_city, optimal_parent)
        else:
            self.done = True
            return None


    def get_city_data(self):
        with open("graf.json","r") as f:
            city_data = json.loads(f.read())

        return city_data

# if __name__ == '__main__':
#     dij = Dijkstra()
#     city_data = dij.get_city_data()
#
#     # try:
#     #     city_from = sys.argv[1]
#     #     city_to = sys.argv[2]
#     # except IndexError:
#     #     print("Usage:", sys.argv[0], "\"from city\" \"to city>\"")
#     #     print("City choices:")
#     #     for city in city_data:
#     #         print("   -", city)
#     #     sys.exit(1)
#
#     city_from = 'Gdańsk Lech Wałęsa Airport'
#     city_to = 'John Paul II International Airport Kraków-Balice Airport'
#     print(dij.dijkstra(city_from, city_to, city_data, False))

