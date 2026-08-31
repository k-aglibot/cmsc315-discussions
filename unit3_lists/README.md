# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists.

## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

This assignment worked through insertion, deletion, and search on Python lists, and the concept that stuck most was seeing why position matters for performance. Inserting or deleting at the front of a list costs more than doing it at the end, since Python has to shift every element over to make room or fill the gap. Appending to the end skips that shifting entirely, which is why it runs in constant time while front operations run in linear time.

2. What challenges did you encounter, and how did you overcome them?

The main challenge was writing the search function as a manual loop instead of just using Python's built-in in operator. It felt redundant at first, but doing it manually made the linear scan visible instead of hidden, which made the O(n) cost easier to actually explain rather than just state.

3. How do list operations impact performance in real-world applications?

A to-do list is a practical example of this tradeoff. Tasks don't need to stay in a fixed order, but users are constantly adding new ones, checking off completed ones, and searching for a specific task, which is exactly where insertion position and search cost start to matter. Checking off a task near the top means every task below it has to shift up, and finding one by name means scanning through however many tasks came before it. Those costs stay invisible with a short list, but they add up as the list grows.
