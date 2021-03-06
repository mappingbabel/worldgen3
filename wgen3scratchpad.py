__author__ = 'iamja_000'

from itertools import product, starmap
import random

x = 5
y = 5
lx = 5
ly = 5

def world_coordinates():
    w_coord = list(product(range(x), range(y)))
    return w_coord

our_coord = world_coordinates()
#print(our_coord)

def border_adder(base_coord_list):
    the_new_borders = []
    for i in base_coord_list:
        a, b, = i
        if a == 0:
            the_new_borders.append(i)
        elif b == 0:
            the_new_borders.append(i)
        elif a == x-1:
            the_new_borders.append(i)
        elif b == y-1:
            the_new_borders.append(i)
    return the_new_borders

our_borders = border_adder(our_coord)
print("TEST")
#print(our_borders)

choice_options = [" ", "W"]
world_map = [[random.choice(choice_options) for i in range(x)] for i in range(y)]
for i in world_map:
    print(i)

def neighbour_check(x, y, check_type):
    neigh_count = 0
    if (x+1, y) in world_coordinates():
        if world_map[x+1][y] == check_type:
            neigh_count += 1
            if (x+1, y) not in neighbour_list:
                neighbour_list.append((x+1, y))
    if (x-1, y) in world_coordinates():
        if world_map[x-1][y] == check_type:
            neigh_count += 1
            if (x-1, y) not in neighbour_list:
                neighbour_list.append((x-1, y))
    if (x, y+1) in world_coordinates():
        if world_map[x][y+1] == check_type:
            neigh_count += 1
            if (x, y+1) not in neighbour_list:
                neighbour_list.append((x, y+1))
    if (x, y-1) in world_coordinates():
        if world_map[x][y-1] == check_type:
            neigh_count += 1
            if (x, y-1) not in neighbour_list:
                neighbour_list.append((x, y-1))
    return neigh_count


def room_explore(x, y):
    our_type = world_map[x][y]
    print("Our type is: {}".format(our_type))
    neighbour_check(x, y, our_type)
    print(neighbour_list)
    while neighbour_check(x, y, our_type) > 0:
        print(neighbour_list)
        x, y = random.choice(neighbour_list)
        neighbour_check(x, y, our_type)


for i in world_coordinates():
    neighbour_list = []
    #room_explore(i[0], i[1])

def base_flood_fill_algorithm(world_map, x, y, old_character, new_character):

        if world_map[y][x] != old_character:
            return
        world_map[y][x] = new_character


        if x > 0: # left
            base_flood_fill_algorithm(world_map, x-1, y, old_character, new_character)

        if y > 0: # up
            base_flood_fill_algorithm(world_map, x, y-1, old_character, new_character)

        if x < x-1: # right
            base_flood_fill_algorithm(world_map, x+1, y, old_character, new_character)

        if y < y-1: # down
            base_flood_fill_algorithm(world_map, x, y+1, old_character, new_character)

def count_rooms(world_map):
    roomCount = 0
    for x in range(lx):
        for y in range(ly):
            if world_map[y][x] == " ":
                base_flood_fill_algorithm(world_map, x, y, " ", "$")

                roomCount += 1
        print(" ")
    for i in world_map:
        print(i)

    return roomCount

our_count = count_rooms(world_map)
print(our_count)


#WORK OUT HOW TO COUNT CONTENTS OF A ROOM USING AN ALGORITHM

#REIMPEMT THIS ALGORITHM https://www.raywenderlich.com/4946/introduction-to-a-pathfinding
    def routefinding(self, start_location, end_location):
        print("Checking between {} and {}".format(start_location, end_location))
        open_list = []
        closed_list = []
        closed_list.append(start_location)
        open_list.extend(self.neighbour_type_check_return(start_location[0], start_location[1], 1, self.initial_seed_land))
        open_list.remove(start_location)
        print(closed_list)
        print(open_list)

        def path_scoring_loop(path_to_score, start_location, end_location):
            list(start_location)
            list(path_to_score)
            test_route_dictionary = { }
            for i in path_to_score:
                actual_distance_a = abs(i[0] - start_location[0])
                actual_distance_b = abs(i[1] - start_location[1])
                combined_distance = actual_distance_a, actual_distance_b
                print("Distance: {}".format(combined_distance))
                #measure that punishes diagonals
                merged_distance = actual_distance_a + actual_distance_b
                print("Merged distance: {}".format(merged_distance))

                movement_distance = abs(start_location[0] - end_location[0]), abs(start_location[1] - end_location[1])
                merged_movement_distance =abs(start_location[0] - end_location[0]) + abs(start_location[1] - end_location[1])
                print(movement_distance)
                print(merged_movement_distance)
                our_final_score = merged_distance + merged_movement_distance
                print(our_final_score)
                test_route_dictionary[i] = our_final_score
            print(test_route_dictionary)

        test_route_dictionary = { }
        while end_location not in open_list:
            for i in open_list:
                merged_distance = abs(i[0] - start_location[0]) + abs(i[1] - start_location[1])
                merged_movement_distance = abs(start_location[0] - end_location[0]) + abs(start_location[1] - end_location[1])
                our_final_score = merged_distance + merged_movement_distance
                test_route_dictionary[i] = our_final_score
            min_val = min(test_route_dictionary.values())
            pos_values = [k for k, v in test_route_dictionary.items() if v == min_val]
            potential_route = random.choice(pos_values)
            closed_list.append(potential_route)
            open_list.extend(self.neighbour_type_check_return(potential_route[0], potential_route[1], 1, self.initial_seed_land))
            open_list.remove(potential_route)
            print(test_route_dictionary)



        path_scoring_loop(open_list, start_location, end_location)