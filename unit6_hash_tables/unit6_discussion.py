"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    print("\n=== INSERT OPERATIONS ===")
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # A Python dict is a hash table under the hood. Each key gets run through
    # a hash function (hash()), and that hash value determines which "bucket"
    # the key-value pair lands in. That's why lookups, inserts, and deletes
    # run in average O(1) time instead of scanning every item like a list would.
    hash_table = {}

    # Inserting pairs one at a time to show each one landing in the table.
    hash_table["apple"] = 1.20
    hash_table["banana"] = 0.55
    hash_table["cherry"] = 3.75
    hash_table["date"] = 4.10
    hash_table["elderberry"] = 5.00

    print("Dictionary after inserting 5 key-value pairs:")
    print(hash_table)

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    print("\n=== LOOKUP OPERATIONS ===")
    print("TODO: Demonstrate successful key lookups.")

    # hash_table["apple"] hashes the string "apple" and jumps straight to the
    # bucket that holds it, no need to walk through banana, cherry, etc.
    apple_price = hash_table["apple"]
    print(f"Lookup 'apple': {apple_price}")

    # .get() works the same way but returns None instead of raising an error if the key isn't found.
    cherry_price = hash_table.get("cherry")
    print(f"Lookup 'cherry': {cherry_price}")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")

    print("Before update:", hash_table)

    # Assigning to an existing key hashes it, finds the same bucket,
    # and overwrites the value there.
    hash_table["banana"] = 0.65

    print("After update:", hash_table)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")

    print("Before deletion:", hash_table)

    # del hashes the key to find its bucket, then removes that slot entirely.
    # Once removed, the key no longer exists, a later lookup on it will fail.
    del hash_table["date"]

    print("After deletion:", hash_table)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: looking up a key that was never inserted.
    # hash_table["fig"] would raise a KeyError; .get() sidesteps that
    # and returns a default instead.
    missing_lookup = hash_table.get("fig", "NOT FOUND")
    print(f"Lookup missing key 'fig': {missing_lookup}")

    # Edge case 2: deleting a key that doesn't exist.
    # del hash_table["fig"] would also raise a KeyError, so check membership first.
    if "fig" in hash_table:
        del hash_table["fig"]
        print("Deleted 'fig'.")
    else:
        print("Tried to delete 'fig', but it isn't in the table, so nothing happened.")


if __name__ == "__main__":
    main()