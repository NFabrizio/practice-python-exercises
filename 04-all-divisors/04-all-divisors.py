import time

def all_divisors():
    divisor_list = []

    target = input("Enter an integer: ")

    while not target.isdigit():
        target = input("That number is not an integer. Please enter an integer: ")

    start = -time.time()

    target = int(target)

    # # Naive approach -- 3.417 seconds for input of 10000000
    # for num in range(1, target):
    #     if target % num == 0:
    #         divisor_list.append(num)

    # # Better approach -- 1.368 seconds for input of 10000000
    # # Since numbers greater than half the target value cannot divide into target evenly, we can stop early
    # for num in range(1, target // 2 + 1):
    #     if target % num == 0:
    #         divisor_list.append(num)

    # Even better approach -- 0.00127 seconds for input of 10000000
    # Reduce the search space even more since the largest pair of divisors we can have is the square root of the target
    divisor_dict = {}

    for num in range(1, int(target ** 0.5) + 1):
        if not divisor_dict.get(num) and target % num == 0:
            pairing = int(target / num)
            divisor_list.append(num)

            if not num == pairing:
                divisor_list.append(pairing)

            divisor_dict[pairing] = num

    # divisor_list.sort()

    print(f'Execution time: {time.time() + start}')

    return divisor_list

print(all_divisors())
