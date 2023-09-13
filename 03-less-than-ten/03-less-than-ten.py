import time

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# a = [5, 8, 13, 21, 34, 55, 89]
a = [*range(10000000)]

def less_than_list(check, input_list):
    start = -time.time()

    # # Naive approach -- 1.273 seconds
    # new_list = [x for x in input_list if x < check]

    # # Better approach -- 0.7296 seconds
    # target_idx = None
    # input_list.sort()
    # for i, x in enumerate(input_list):
    #     if x >= check:
    #         target_idx = i
    #         break

    # new_list = input_list[:target_idx]

    # Even better approach -- 4.196e-05 seconds
    # Example: input_list = [0,1,2,3,4], check = -1
    target_idx = None
    def find_target_idx(left, right, target_val, list_data):
        if left > right:
            return left

        mid = ((right - left) // 2) + left

        if list_data[mid] == target_val:
            return mid
        elif list_data[mid] < target_val:
            return find_target_idx(mid+1, right, target_val, list_data)
        else:
            return find_target_idx(left, mid-1, target_val, list_data)

    target_idx = find_target_idx(0, len(input_list)-1, check, input_list)

    new_list = input_list[:target_idx]

    print(f'Execution time: {time.time() + start}')

    return new_list


print(less_than_list(100, a))
