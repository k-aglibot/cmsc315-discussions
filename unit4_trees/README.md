# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

This assignment gave me a real feel for recursion beyond the basic examples I'd seen before. Writing _insert_recursive and _search_recursive meant trusting that the recursive call would correctly handle whatever subtree it landed on, without tracing through every level by hand. Letting the function call itself and rely on the base case, instead of managing state with loops, took some getting used to.
2. What challenges did you encounter, and how did you overcome them?
   
The main challenge was remembering to return the node at the end of _insert_recursive. Without that return statement, the parent call never reattaches the updated subtree, and inserts silently fail to change the tree. Running the in-order traversal after each insert helped me catch that early.
3. Explain BST behavior and compare to how ordering works to create efficiency as compared to other data structures.

A BST stays efficient because every comparison eliminates half the remaining tree, similar to binary search on a sorted array. Unlike an array, a BST also supports fast insertion, since adding a value just means finding its spot and creating a new node, no shifting elements required. A plain list gives fast insertion but slow search, or fast search but slow insertion if it's kept sorted. A BST gets both, as long as it stays reasonably balanced.