# Unit 1 Discussion: Python OOP, Namespaces, and Copying

## Overview

This program modeled a gym exercise tracker using two classes, `Exercise` and `WeightedExercise`, to demonstrate inheritance, class and instance namespaces, and shallow versus deep copying in Python.

## Design Approach

`Exercise` was the parent class. It stored a name, muscle group, sets, and reps, plus a `training_type` class variable and a `display_info()` method. `WeightedExercise` inherited from `Exercise`. It added a `weight` instance variable, a `unit` class variable, a `total_volume()` method, and an overridden `display_info()` that included weight and volume. I tested this by creating a Push-up (parent) and a Bench Press (child), then comparing their `display_info()` output side by side.

## Namespace Demonstration

In `demonstrate_namespaces()`, I created two `WeightedExercise` objects, Leg Press and RDL. I accessed the `unit` class variable both through the class directly and through an instance. I added a `personal_record` attribute to only one object, then printed both objects' `__dict__`. This showed the new attribute existed only in that object's instance namespace, not the shared class namespace.

## Copying Demonstration

In `demonstrate_copying()`, I created a Calf Press object with a mutable `set_weights` list, then made a shallow copy and a deep copy. After appending a new value to the original's list, the shallow copy reflected the change, since it shared a reference to the same list. The deep copy did not, since it held a fully independent list.

## Student Extension

I added `compare_volume()`, a function that takes two `WeightedExercise` objects and uses their existing `total_volume()` method. It prints which object has the higher training volume. I tested it with my real Leg Press and RDL numbers.

## Edge Case

I tested `compare_volume()` with two exercises producing the same total volume through different combinations of sets, reps, and weight: Lat Pulldown at 3x10x50 and Shoulder Press at 5x6x50, both equaling 1500. The output printed "Both exercises have equal training volume," confirming the function's `else` branch correctly handles a tie instead of always reporting one exercise as higher.

## Real-World Use Case

This structure could support a workout-tracking app. A user would log exercises across a training program, and the app would calculate total volume per session to track progressive overload over time, similar to how fitness apps estimate training load week over week.

## Reflection

This assignment taught me how inheritance lets a child class reuse a parent's behavior through `super()`. It can still add or override what it needs on top of that. I also learned that instance namespaces stay separate from class namespaces, unless an attribute is added directly to one object. Setting up Git and Python on my local machine for the first time was an early challenge, but the bigger challenge was shallow versus deep copying, since both looked identical until I modified the original's list after copying. The shallow copy changed alongside the original, since it shared the same list in memory. The deep copy stayed independent, since it held its own separate list.

Comparing OOP to procedural programming: OOP groups data and behavior into objects, while procedural code keeps them separate. This mattered practically here, since adding a new exercise type only required a new class inheriting shared structure, not rewriting standalone functions. That same principle reduces overhead in larger applications, since shared logic lives in one place and gets reused rather than duplicated. Future exercise types or features can extend existing classes instead of being built from scratch, making the codebase easier to maintain and scale.