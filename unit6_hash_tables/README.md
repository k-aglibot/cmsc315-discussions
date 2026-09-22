# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?

This assignment reinforced how Python dictionaries work as hash tables. Assigning a key runs it through a hash function that maps it to a bucket, which is why insert, lookup, update, and delete run in constant time instead of scanning every item. Building the price-lookup example also clarified that "updating" and "inserting" use the same syntax, `dict[key] = value`, and Python distinguishes them only by whether the key already exists.

2. What challenges did you encounter, and how did you overcome them?

The main challenge was the edge cases. Missing keys raise a KeyError on direct access, which crashed the program the first time I tested a lookup on a key that didn't exist. I fixed this by switching to .get() for lookups and adding an in check before deletion, so the program handles a missing key gracefully instead of crashing.

3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.

A hash table stores each entry in a bucket determined by hashing its key, which is what lets it retrieve, insert, and remove entries without searching the whole structure. A collision is when two different keys hash to the same bucket, an unavoidable event once enough keys are added, since the number of possible keys usually exceeds the number of buckets. Hash tables stay efficient because most keys land in their own bucket, so the average lookup, insert, or delete touches just one or two buckets instead of the whole structure, even though collisions are always possible.