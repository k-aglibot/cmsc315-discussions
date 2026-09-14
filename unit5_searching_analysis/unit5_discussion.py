"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import time
import random


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Checks each element one at a time from index 0 until it finds
    # the target or runs out of list. Time complexity is O(n) because
    # in the worst case (target is last, or missing entirely), every
    # element gets checked once. There's no way to skip ahead, since
    # linear search doesn't rely on the list being sorted.
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Compares the target to the middle element and eliminates half
    # the remaining search space on every iteration: if target is
    # smaller, the answer (if it exists) must be in the left half, so
    # the right half gets discarded, and vice versa. Because the
    # search space is cut in half each time, the number of comparisons
    # needed grows logarithmically with list size, giving O(log n).
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2  # the "reduce search space by half" step
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    small_data = list(range(0, 100, 2))  # 50 sorted even numbers: 0, 2, 4, ..., 98
    print(f"Dataset size: {len(small_data)}")

    target_found = 44
    lin_result = linear_search(small_data, target_found)
    bin_result = binary_search(small_data, target_found)
    print(f"Searching for {target_found} (exists): linear -> index {lin_result}, binary -> index {bin_result}")

    target_missing = 45  # odd number, won't be in the list
    lin_result = linear_search(small_data, target_missing)
    bin_result = binary_search(small_data, target_missing)
    print(f"Searching for {target_missing} (missing): linear -> {lin_result}, binary -> {bin_result}")

    # On a 50-item list the speed difference between the two
    # algorithms isn't noticeable to a human. The gap only shows
    # up once the dataset gets much larger.

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    large_data = sorted(random.sample(range(0, 10_000_000), 1_000_000))
    print(f"Dataset size: {len(large_data)}")

    target = large_data[-1]  # worst case for linear search: last element

    start = time.perf_counter()
    lin_result = linear_search(large_data, target)
    lin_time = time.perf_counter() - start

    start = time.perf_counter()
    bin_result = binary_search(large_data, target)
    bin_time = time.perf_counter() - start

    print(f"Target found at index {lin_result} (linear) / {bin_result} (binary)")
    print(f"Linear search time: {lin_time:.6f} seconds")
    print(f"Binary search time: {bin_time:.6f} seconds")

    # With a million items, linear search has to check nearly every
    # element to find one near the end, while binary search only needs
    # about log2(1,000,000), around 20 comparisons, to land on the same
    # answer. That gap is why binary search is the standard choice once
    # a dataset gets large.

    # ===============================
    # REAL WORLD SEARCH SCENARIO
    # ===============================
    print("\n=== REAL WORLD SEARCH SCENARIO: LOYALTY PROGRAM LOOKUP ===")

    # A casino loyalty program with 500,000 active members looks up
    # guests by member ID constantly, at kiosks, tables, and the front
    # desk, and that list is sorted, so binary search fits naturally.
    # It finds any member in about 19 comparisons instead of scanning
    # up to 500,000 IDs, which is the difference between an instant
    # lookup and a guest standing there waiting.
    member_ids = sorted(random.sample(range(1_000_000, 9_999_999), 500_000))
    target_member = member_ids[250_000]  # a real member ID, buried in the middle

    start = time.perf_counter()
    lin_result = linear_search(member_ids, target_member)
    lin_time = time.perf_counter() - start

    start = time.perf_counter()
    bin_result = binary_search(member_ids, target_member)
    bin_time = time.perf_counter() - start

    print(f"Looking up member ID {target_member}")
    print(f"Linear search: found at index {lin_result} in {lin_time:.6f} seconds")
    print(f"Binary search: found at index {bin_result} in {bin_time:.6f} seconds")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Case 1: empty list
    empty_list = []
    print(f"Empty list, linear: {linear_search(empty_list, 5)}")
    print(f"Empty list, binary: {binary_search(empty_list, 5)}")
    # Both loops never execute (range(0) and low > high right away),
    # so both correctly return -1. This confirms both algorithms
    # handle n=0 without needing a special-case check.

    # Case 2: single-element list, value present
    single = [7]
    print(f"Single-element list [7], target 7, linear: {linear_search(single, 7)}")
    print(f"Single-element list [7], target 7, binary: {binary_search(single, 7)}")
    # Only one comparison needed for either algorithm; both return
    # index 0, confirming the loop terminates correctly on the
    # smallest non-trivial input.


if __name__ == "__main__":
    main()