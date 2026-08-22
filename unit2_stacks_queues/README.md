# Unit 2 Discussion: Stacks and Queues

## Overview
This program modeled a customer service helpdesk system using two classes, `Stack` and `Queue`, to demonstrate LIFO and FIFO behavior.

## Design Approach
`Stack` used a Python list as its internal structure, since `append()` and `pop()` both operate on the end of the list in constant time. It implemented `push()`, `pop()`, `peek()`, and `is_empty()`. `Queue` used `collections.deque` instead of a list, since removing from the front of a list requires shifting every remaining item over, while `deque.popleft()` does not. It implemented `enqueue()`, `dequeue()`, `front()`, and `is_empty()`. Both classes raised an `IndexError` on empty pop, peek, dequeue, or front calls, rather than returning `None`, so an empty-structure bug surfaces immediately instead of passing through silently.

## Stack Demonstration
In the stack demo, I created a `Stack` object to track a support ticket's status history: Open, In Progress, Escalated, and Resolved. I used `peek()` to show the current status, then used `pop()` to undo the most recent status change, showing the ticket reverting to Escalated. This demonstrated LIFO behavior, since the most recently added status was the first one removed.

## Queue Demonstration
In the queue demo, I created a `Queue` object to model a ticket line, enqueuing four ticket numbers in the order they were submitted. I used `front()` to show which ticket was next, then used `dequeue()` to resolve and remove it, showing the next ticket in line take its place. This demonstrated FIFO behavior, since tickets were handled in the same order they arrived.

## Edge Cases
I tested both structures with a single item added and then removed, confirming `is_empty()` returned `True` afterward for each. I also tested `pop()` and `peek()` on an empty stack, and `dequeue()` and `front()` on an empty queue, each correctly raising an `IndexError` rather than returning `None` or crashing unexpectedly.

## Real-World Use Case
This structure could support an actual helpdesk or customer service platform. A stack would let an agent undo their most recent status change on a ticket without affecting earlier history, while a queue would guarantee tickets get handled in the order customers submitted them, similar to how support platforms like Zendesk or a call center queue process requests fairly rather than arbitrarily.

## Reflection
This assignment taught me that a stack's operations only ever touch one end of the structure, and that's what makes it LIFO. A queue needs two distinct access points, front and back, for FIFO to work. I also learned why the container choice matters beyond correctness: a list works fine for a stack since append() and pop() both operate on the end in constant time, but a queue needs deque, since removing from the front of a list means shifting every remaining item over. The bigger challenge was deciding how to handle empty-structure operations. Returning None looked fine at first, but it let a bug pass through silently and get treated as real data further down the program. Raising an IndexError instead surfaces the problem where it happens

Contrasting the two structures directly, a stack only ever lets you undo or reference the single most recent action, so it fits a status history, where undoing the most recent change is what actually matters. A queue preserves arrival order across every item waiting, so it fits a support ticket line, where the first person in should be the first one helped. That distinction mattered here, since the status history required LIFO to make "undo" meaningful, while the ticket queue required FIFO to keep the wait fair.