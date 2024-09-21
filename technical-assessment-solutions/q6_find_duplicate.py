def find_duplicate(nums):
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    tortoise = nums[0]
    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare


if __name__ == "__main__":
    test_cases = [
        [1, 3, 4, 2, 2],
        [3, 1, 3, 4, 2],
        [1, 1],
        [1, 1, 2],
    ]

    for case in test_cases:
        result = find_duplicate(case)
        print(f"Input: {case}")
        print(f"Duplicate: {result}")
        print("---")