# Implimentation of various sorting algorithms for lists
##########################
from sys import argv
with open(argv[1], "r") as f:
    output = eval(f.read())



def python_sort(our_list):
    #return sorted(our_list)
    pass

def list_swap(our_list, low, high):
    # take one index and swap with another
    #print(low, high)
    our_list[low], our_list[high] = our_list[high], our_list[low]

    return our_list


def selection_sort(our_list):
        ##### need more code here ####
    #for our_list[high] in range(1, len(our_list)):
    #        if our_list[high] < our_list[low]:
    #            low = high

    #our_list[low], our_list[high] = our_list[high], our_list[low]
    #return our_list

#####   Kyle's way:
    for start in range(len(our_list)):
        index_minimum = start
        minimum = our_list[start]
        for index in range(start + 1, len(our_list)):
            if our_list[index] < minimum:
                print(" our_list[index] < minimum", our_list[index], minimum)
                index_minimum = index
                minimum = our_list[index]
                if index_minimum != start:
                    print("swap these two", our_list[start], our_list[index_minimum])
                    list_swap(our_list, start, index_minimum)
    return our_list
### not working ####  fix it!
    #"""
    #Look through the list.  Find the smallest element.  Swap it to the front.
    #Repeat.
    #"""

def insertion_sort(our_list):

    for index in range(1, len(our_list)):
        candidate = our_list[index]
        comparison_index = index - 1
        while comparison_index >= 0:
            if candidate < our_list[comparison_index]:
                list_swap(our_list, comparison_index, comparison_index + 1)
                comparison_index -= 1
            else:
                break
    return our_list


##from website
    #for (k = index; k > 1 and a[k] < a[k-1]; k--)
#        swap a[k,k-1]
    #Insert (via swaps) the next element in the sorted list of the previous
    #elements.
    #"""


###  Divide and Conquer approach ####
def merge_sort(our_list):
    index1, index2, index3 = 0, 0, 0


    #sorted.append(upper_half.pop(0))

    #"""
    #Our first recursive algorithm.
    #""
print(output)
print(merge_sort(output))
