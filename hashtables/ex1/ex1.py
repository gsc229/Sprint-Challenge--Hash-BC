#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    
    """
    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)      
    
    for i in range(0, length):
        difference = limit - weights[i]
        instance = hash_table_retrieve(ht, weights[i])
        #print(first)
        find_difference = hash_table_retrieve(ht, difference)
        if find_difference:
            
            if find_difference > instance:
                print([find_difference, i])
                return [find_difference, i]
            elif find_difference < instance:
                print([i, find_difference])
                return [i, find_difference]
            else:
                print([i, find_difference])
                return [find_difference, i]
                
        
        

    
    


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")


get_indices_of_item_weights([9], 1, 9) #1
get_indices_of_item_weights([4,4], 2, 8) #2
get_indices_of_item_weights([ 4, 6, 10, 15, 16 ], 5, 10) #3
get_indices_of_item_weights([12, 6, 7, 14, 19, 3, 0, 25, 40], 9, 7) #4