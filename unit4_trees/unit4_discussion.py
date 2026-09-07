"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Each node holds a value plus left/right child pointers, both None at first.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # An empty tree just has no root yet.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # No root yet means this value becomes the root; otherwise recurse to find its spot.
        if self.root is None:
            self.root = Node(value)
        else:
            self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: hit an empty spot, this is where the new value goes.
        if node is None:
            return Node(value)

        # Smaller values go left, larger go right, this ordering rule is what keeps the tree searchable.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        # If value == node.value, we do nothing (no duplicates).

        # Return the node so the parent call reattaches whatever changed below it.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Each comparison rules out a whole subtree, not just one element,
        # so a balanced tree cuts the remaining search space roughly in half per step.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # Base case 1: fell off the tree, value isn't here.
        if node is None:
            return False
        # Base case 2: found it.
        if value == node.value:
            return True
        # Otherwise keep going left or right based on comparison.
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return
        # Visit the left subtree first (smaller values).
        self._inorder_recursive(node.left, values)
        # Visit this node.
        values.append(node.value)
        # Visit the right subtree (larger values).
        # Left-smaller, right-larger at every node is why this order comes out sorted.
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]
    for v in values_to_insert:
        tree.insert(v)
        # Each comparison sends the search down only one side of the tree,
        # shrinking the space by half at each level.
        print(f"Inserted {v}")

    print(f"Values inserted: {values_to_insert}")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    result = tree.inorder()
    print(f"In-order traversal result: {result}")
    print("Sorted because in-order visits left (smaller), then the node, then right (larger).")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    for v in [40, 80]:
        print(f"Search {v}: {tree.search(v)} (expected True, value exists)")
    for v in [100, 25]:
        print(f"Search {v}: {tree.search(v)} (expected False, value not inserted)")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge case 1: searching/traversing an empty tree.
    empty_tree = BST()
    print(f"Empty tree search for 10: {empty_tree.search(10)} "
          f"(no root, so recursion hits its base case immediately)")
    print(f"Empty tree in-order traversal: {empty_tree.inorder()} "
          f"(no nodes to visit, returns an empty list)")

    # Edge case 2: inserting a duplicate value.
    tree.insert(50)
    print(f"After inserting duplicate 50, in-order: {tree.inorder()} "
          f"(duplicate ignored, tree structure unchanged)")

    # ===============================
    # TODO (Student): REAL-WORLD BST EXAMPLE
    # ===============================

    print("\n=== REAL-WORLD EXAMPLE: PHONE CONTACTS ===")
    # Contacts get looked up by name constantly, a natural fit for BST search.
    contacts = BST()
    contact_names = ["Marcus", "Diana", "Priya", "Aaron", "Kevin", "Zara", "Nina"]
    for name in contact_names:
        contacts.insert(name)
    print(f"Contacts inserted: {contact_names}")

    # In-order traversal gives the list already sorted, exactly how a phone displays contacts.
    print(f"Contacts alphabetically: {contacts.inorder()}")

    # Looking up a contact by name is a search, same as before.
    for name in ["Priya", "Zara"]:
        print(f"Contact '{name}' found: {contacts.search(name)}")
    for name in ["Oliver"]:
        print(f"Contact '{name}' found: {contacts.search(name)}")


if __name__ == "__main__":
    main()