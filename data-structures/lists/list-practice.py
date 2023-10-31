import time

# Remove even integers from list
def return_odds(int_list=None):
    if not int_list:
        return int_list

    start = -time.time()

    # # Naive approach - 0.7562332153320312 seconds for n=10000000
    # new_list = []
    #
    # for num in int_list:
    #     if num % 2 != 0:
    #         new_list.append(num)
    #
    # return new_list

    # Better approach - 0.644946813583374 seconds for n=10000000
    new_list = [num for num in int_list if num % 2 != 0]

    print(f'duration: {start + time.time() }')

    return new_list

# # Tests
# test1 = []
# test2 = [0]
# test3 = [1,2,3,4,5,6]
# test4 = [5,-6,27,-51,-24,7]
# test5 = range(10000000)
# print(f'test1: {return_odds(test1)}')
# print(f'test2: {return_odds(test2)}')
# print(f'test3: {return_odds(test3)}')
# print(f'test4: {return_odds(test4)}')
# return_odds(test5)
# # print(f'test5: {return_odds(test5)}')

# Merge two sorted lists
def merge_lists(list1=None, list2=None):
    if not list1 or not list2:
        return list1 if not list2 else list2

    l1_idx = 0
    l2_idx = 0
    merged = []

    start = -time.time()

    # Optimized approach - 0.00165104 seconds for range(1,100,2), range(100,100000,2)
    while l1_idx < len(list1) or l2_idx < len(list2):
        if l1_idx >= len(list1) and l2_idx < len(list2):
            merged += list2[l2_idx:]
            l2_idx = len(list2)
        elif l2_idx >= len(list2) and l1_idx < len(list1):
            merged += list1[l1_idx:]
            l1_idx = len(list1)
        elif list1[l1_idx] < list2[l2_idx]:
            merged.append(list1[l1_idx])
            l1_idx += 1
        else:
            merged.append(list2[l2_idx])
            l2_idx += 1

    # Non-optimized approach - 0.02242732 seconds for range(1,100,2), range(100,100000,2)
    # while l1_idx < len(list1) or l2_idx < len(list2):
    #     if l1_idx < len(list1) and (l2_idx >= len(list2) or list1[l1_idx] < list2[l2_idx]):
    #         merged.append(list1[l1_idx])
    #         l1_idx += 1
    #     else:
    #         merged.append(list2[l2_idx])
    #         l2_idx += 1

    print(f'duration: {start + time.time() }')

    return merged


# Tests
# print(f'test1 merge: {merge_lists([], [2,4,6])}')
# print(f'test2 merge: {merge_lists([1,3,5], [])}')
# print(f'test3 merge: {merge_lists([1,3,5], [2,4,6])}')
# print(f'test4 merge: {merge_lists([-1,1,3,5,7,9], [-2,0,2,4,6,8,10])}')
# # print(f'test4 merge: {merge_lists(range(1,100000,2), range(0,100000,2))}')
# merge_lists(range(1,100,2), range(100,100000,2))


# Find second max value in list
def find_second_max(input_list):
    if not input_list:
        return -1

    max = None
    max_2nd = None

    for num in input_list:
        if not max:
            max = num

        if not max_2nd:
            max_2nd = num

        if num > max:
            max_2nd = max
            max = num
        elif num > max_2nd or max_2nd == max:
            max_2nd = num

    return max_2nd


# Tests
print(find_second_max([]))
print(find_second_max([3]))
print(find_second_max([3,2,1,0,-1]))
print(find_second_max([1,2,3,4,5]))
print(find_second_max([27,-12,15,105,-87]))
print(find_second_max([270,-12,15,105,-87]))
