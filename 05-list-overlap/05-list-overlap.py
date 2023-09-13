import random
import time

def list_overlap(list1, list2):
    duration = -time.time()
    overlap = []

    # # Naive approach -- 12.49 seconds for n=10000
    # # Take all elements from one list and check if they exist in the other list - O(n**2)

    # # for num in list1:
    # #     if num in list2 and not num in overlap:
    # #         overlap.append(num)

    # [overlap.append(num) for num in list1 if num in list2 and not num in overlap]

    # Better approach -- 0.0887 seconds for n=10000
    # Sort lists and use pointers in while loop to compare elements
    list1.sort()
    list2.sort()

    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(list1) and ptr2 < len(list2):
        # if elem1 == elem2 -> insert into output list
        if list1[ptr1] == list2[ptr2] and not list1[ptr1] in overlap:
            overlap.append(list1[ptr1])
            ptr1 += 1
            ptr2 += 1
        # if elem1 > elem2 -> increment list2 pointer
        elif list1[ptr1] > list2[ptr2]:
            ptr2 += 1
        # if elem1 < elem2 -> increment list1 pointer
        else:
            ptr1 += 1

    duration += time.time()
    print(f'Execution time: {duration}')

    return overlap

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
n = 10000
a = random.sample(range(1,n*10), n)
b = random.sample(range(1,n*10), int(1.2*n))

print(list_overlap(a, b))
