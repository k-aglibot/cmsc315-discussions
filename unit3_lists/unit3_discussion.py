"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student): Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # Front insertion shifts every element right, which makes it O(n).
    # End insertion is O(1) on average, since resizing the list only happens occasionally.
    # Middle insertion still shifts everything after it, just fewer elements than front.
    lst.insert(index, value)
    return lst

def delete_at(lst, index):
    """
    TODO (Student): Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # An out-of-range index would make pop() raise an IndexError.
    # Validating first avoids that crash.
    # It also lets the caller decide how to handle an invalid position.
    if index < 0 or index >= len(lst):
        return None
    return lst.pop(index)

def search_value(lst, value):
    """
    TODO (Student): Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # This is a linear search, checking each index in order.
    # A plain list has no structure to let it skip elements.
    # That makes it O(n), even when the value isn't there at all.
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # A user's saved playlists in a music app
    playlists = ["Study Session", "Gym", "Lounging"]
    print("Original list:", playlists)

    # Beginning: a new playlist gets pinned to the top of the library
    insert_at(playlists, 0, "Shower Karaoke")
    print("After inserting 'Shower Karaoke' at index 0:", playlists)

    # Middle: a playlist gets slotted in partway through the library
    mid = len(playlists) // 2
    insert_at(playlists, mid, "Night Owl")
    print(f"After inserting 'Night Owl' at index {mid}:", playlists)

    # End: a new playlist gets added to the bottom of the library
    insert_at(playlists, len(playlists), "Road Trip")
    print("After inserting 'Road Trip' at the end:", playlists)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Beginning: the top playlist in the library gets deleted
    removed = delete_at(playlists, 0)
    print(f"Removed '{removed}' from index 0. List is now:", playlists)

    # Middle: a playlist partway through the library gets deleted
    mid = len(playlists) // 2
    removed = delete_at(playlists, mid)
    print(f"Removed '{removed}' from index {mid}. List is now:", playlists)

    # End: the last playlist in the library gets deleted
    removed = delete_at(playlists, len(playlists) - 1)
    print(f"Removed '{removed}' from the last index. List is now:", playlists)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Existing value
    target = "Night Owl"
    result = search_value(playlists, target)
    print(f"Searching for '{target}': found at index {result}"
          if result != -1 else f"Searching for '{target}': not found")

    # Missing value
    target = "Cooking"
    result = search_value(playlists, target)
    print(f"Searching for '{target}': found at index {result}"
          if result != -1 else f"Searching for '{target}': not found")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: deleting with an invalid index
    result = delete_at(playlists, 99)
    print("Deleting at index 99 (out of range) returns:", result)
    # There's no index 99 in this list, so delete_at's validation catches
    # it and returns None instead of letting pop() crash the program.

    # Edge case 2: duplicate values only remove the first match
    library = ["Gym", "Gym", "Night Owl"]
    index = search_value(library, "Gym")
    # search_value() returns the FIRST matching index.
    # If two playlists share the name "Gym," this always removes the first one, not necessarily the one intended.
    delete_at(library, index)
    print("Library with a duplicate 'Gym' playlist, after removing one copy:", library)

if __name__ == "__main__":
    main()