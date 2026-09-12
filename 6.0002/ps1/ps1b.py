###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================
import math

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {}):
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """

    best_num = math.inf

    if target_weight in memo:
        return memo[target_weight]
    #base case
    elif target_weight == 0:
        return 0
    #recursive case
    else:
        for weight in egg_weights:
            if weight <= target_weight:
                result = 1 + dp_make_weight(egg_weights, target_weight - weight)
                if result < best_num:
                    best_num = result
        memo[target_weight] = best_num
            
            
    return best_num


    
    



    

    



# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1, 5, 10, 20)
    n = 99
    print("Egg weights = (1, 5, 10, 20)")
    print("n = 99")
    print("Expected output: 10")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()