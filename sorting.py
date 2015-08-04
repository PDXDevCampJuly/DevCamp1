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
def sort_thenMerge(left_list, right_list, merged_list):
    leftIndex, rightIndex, mergedIndex = 0, 0, 0
    n1, n2 = len(left_list), len(right_list)

    while leftIndex < n1 and rightIndex < n2:
        if left_list[leftIndex] < right_list[rightIndex]:
            merged_list[mergedIndex] = left_list[leftIndex]
            leftIndex = leftIndex + 1
        else:
            merged_list[mergedIndex] = right_list[rightIndex]
            rightIndex = rightIndex + 1
        mergedIndex = mergedIndex + 1

    while leftIndex < n1:
        merged_list[mergedIndex] = left_list[leftIndex]
        leftIndex = leftIndex + 1
        mergedIndex = mergedIndex + 1

    while rightIndex < n2:
        merged_list[mergedIndex] = right_list[rightIndex]
        rightIndex = rightIndex + 1
        mergedIndex = mergedIndex + 1
    return merged_list

def merge_sort(our_list):
    if len(our_list) == 1:
        return our_list
    else:
        middle = len(our_list) // 2
        list1 = merge_sort(our_list[:middle])
        list2 = merge_sort(our_list[middle:])
        list3 = []
        while len(list1) > 0 and len(list2) > 0:
            if list[0] <= list[2]:
                list3.append(list1.pop(0))
            else:
                list3.append(list2.pop(0))
        return list3 + list1 + list2
    pass




    #sorted.append(upper_half.pop(0))

    #"""
    #Our first recursive algorithm.
    #""
print(output)
print(sort_thenMerge([2,6,9], [4,7,8], [0,0,0,0,0,0]))
print(merge_sort(our_list))
