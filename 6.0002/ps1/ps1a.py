###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1 ---> DONE
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    #vara definitions
    file = open("ps1_cow_data.txt", "r")
    data_dict = {}

    #iteration, update dict
    for line in file:
        line_list = line.split(",")
        data_dict[line_list[0]] = int(line_list[1])

    #close file, return dict
    file.close()
    return data_dict




# Problem 2 ---> DONE
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    #vara definitions
    cows = cows.copy()
    big_list = []
    

    while len(cows) > 0:
        little_list = []
        heaviest = 0
        remaining = limit

        #iteratation of a little_list
        while True:
            best_cow = None
            heaviest = 0

            #finding largest cow
            for cow in cows:
                if cows[cow] > heaviest and cows[cow] <= remaining: #check if a new heaviest, and if its within remaining limit
                    heaviest = cows[cow]
                    little_list.append(cow)
                    best_cow = cow

            #exit if none found
            if best_cow == None:
                break

            #update list + varas
            little_list.append(best_cow)
            remaining -= cows[best_cow]
            del cows[best_cow]

        big_list.append(little_list)

    return big_list

                
    



    
        



# Problem 3 --> TODO
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """

    best_list = []
    curr_list = []
    cows_copy = cows.copy()
    weight = 0
    valid = True
    
    #for each partition
    for partition in get_partitions(cows_copy):
        #reset variables
        curr_list = []
        valid = True
            
        for trip in partition:
                
            weight = 0

            for cow in trip:
                weight += cows_copy[cow]

            if weight > limit:
                valid = False
                break
                
            curr_list.append(trip)

            
        if valid and (len(curr_list) < len(best_list) or best_list == []):
            best_list = curr_list.copy()


    print(best_list)
    return best_list
    
    
            


    
        
# Problem 4 --> TODO
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    start = time.time()
    greed_cows = greedy_cow_transport(load_cows(None), 10)
    end = time.time()
    time1 = end - start
    start = time.time()
    brute_cows = brute_force_cow_transport(load_cows(None), 10)
    end = time.time()
    time2 = end - start


    print("Greed cow algo took " + str(len(greed_cows)) + " trips, and took " + str(time1) + " seconds")    

    print("Brute cow algo took " + str(len(brute_cows)) + " trips, and took " + str(time2) + " seconds")


brute_force_cow_transport(load_cows(None), 10)
#compare_cow_transport_algorithms()