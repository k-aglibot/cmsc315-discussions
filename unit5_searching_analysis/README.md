# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.


## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain when to use linear versus binary search, including tradeoffs in real-world scenarios.

This assignment reinforced the difference between algorithmic complexity in theory and what it looks like on a machine. Reading that binary search is O(log n) is one thing, watching it find a target in a million-item list in 0.000009 seconds while linear search takes 0.13 seconds for the same list is another. The comparison count math (log2 of a million is about 20) turned into something concrete rather than a formula to memorize.

The main challenge was picking a large dataset that demonstrated the gap. My first attempt used a target near the front of the list, and both algorithms returned instantly, so the timing difference barely registered. I had to deliberately search for the last element to force linear search into its worst case.

The tradeoff comes down to whether the data is sorted and how often you're searching versus updating it. Linear search works on any list and needs no setup, so it's fine for small or unsorted data. Binary search requires sorted data but pays off fast once you're searching the same large dataset repeatedly, which is exactly what my test data showed.