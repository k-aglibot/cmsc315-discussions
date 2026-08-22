"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        # A list works since append() and pop() both operate on
        # the end of the list in constant time

        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.
        # append() adds to the end of the list, which is treated as the top,
        # so the last value pushed is the first one popped

        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?
        # Raise an error instead of returning None so a bad pop doesn't
        # slide through and get treated like real data

        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.
        # Returns the top value without removing it, same empty check as pop

        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.

        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.

        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.
        # Adds to the back only, so items leave in the order they arrived

        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.
        # Uses the same idea as Stack.pop(), it raises instead of silently returning None

        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.
        # Returns whoever's been waiting longest, without removing them from the line

        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.

        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


    print("\n=== STACK DEMO: Ticket #4521 Status History ===")
    status_history = Stack()

    print("Logging status changes: Open, In Progress, Escalated, Resolved")
    status_history.push("Open")
    status_history.push("In Progress")
    status_history.push("Escalated")
    status_history.push("Resolved")

    print(f"Current status (top of stack): {status_history.peek()}")

    print(f"Undoing last status change: '{status_history.pop()}' removed")
    print(f"Status reverted to: {status_history.peek()}")

    # Edge case: single-item stack, remove it, confirm empty
    solo = Stack()
    solo.push("Open")
    print(f"\nSingle-entry stack, popped: '{solo.pop()}'")
    print(f"Stack empty after removing only item? {solo.is_empty()}")

    # Edge case: pop and peek on an empty stack
    empty_stack = Stack()
    try:
        empty_stack.pop()
    except IndexError as e:
        print(f"\nPopping an empty stack raised an error: {e}")

    try:
        empty_stack.peek()
    except IndexError as e:
        print(f"Peeking an empty stack raised an error: {e}")

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO: Support Ticket Line ===")
    ticket_queue = Queue()

    print("Tickets submitted: #4521, #4522, #4523, #4524")
    ticket_queue.enqueue("#4521")
    ticket_queue.enqueue("#4522")
    ticket_queue.enqueue("#4523")
    ticket_queue.enqueue("#4524")

    print(f"Next ticket to be handled: {ticket_queue.front()}")

    print(f"Ticket {ticket_queue.dequeue()} has been resolved and closed")
    print(f"Next ticket in line now: {ticket_queue.front()}")

    # Edge case: single-item queue, remove it, confirm empty
    solo_line = Queue()
    solo_line.enqueue("#9001")
    print(f"\nSingle-ticket queue, dequeued: {solo_line.dequeue()}")
    print(f"Queue empty after removing only item? {solo_line.is_empty()}")

    # Edge case: dequeue and front on an empty queue
    empty_queue = Queue()
    try:
        empty_queue.dequeue()
    except IndexError as e:
        print(f"\nDequeuing an empty queue raised an error: {e}")

    try:
        empty_queue.front()
    except IndexError as e:
        print(f"Checking front of an empty queue raised an error: {e}")

if __name__ == "__main__":
    main()
