"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
# Replace the pass statement with your implementation.

class Exercise:
    training_type = "Strength Training"

    def __init__(self, name, muscle_group, sets, reps):
        self.name = name
        self.muscle_group = muscle_group
        self.sets = sets
        self.reps = reps

    def display_info(self):
        return (f"{self.name} ({self.muscle_group}) - "
                f"{self.sets} sets x {self.reps} reps [{self.training_type}]")



# TODO 2:
# Create a child class that inherits from the parent class.
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
# Replace the pass statement with your implementation.

class WeightedExercise(Exercise):
    unit = "lbs"

    def __init__(self, name, muscle_group, sets, reps, weight):
        super().__init__(name, muscle_group, sets, reps)
        self.weight = weight

    def total_volume(self):
        return self.sets * self.reps * self.weight

    def display_info(self):
        base_info = super().display_info()
        volume = self.total_volume()
        return f"{base_info} @ {self.weight}{self.unit}, total volume: {volume}{self.unit}"


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    lift_a = WeightedExercise("Leg Press", "Legs", 3, 10, 145)
    lift_b = WeightedExercise("RDL", "Hamstrings", 3, 10, 35)

    print(f"Class access -> WeightedExercise.unit: {WeightedExercise.unit}")
    print(f"Instance access -> lift_a.unit: {lift_a.unit}")

    lift_a.personal_record = True

    print(f"\nlift_a namespace (__dict__): {lift_a.__dict__}")
    print(f"lift_b namespace (__dict__): {lift_b.__dict__}")

    print(f"\nWeightedExercise class namespace (relevant keys): "
          f"training_type={WeightedExercise.training_type}, unit={WeightedExercise.unit}")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = WeightedExercise("Calf Press", "Calves", 2, 15, 35)

    # mutable data for copy demo
    original.set_weights = [25, 30, 35]

    shallow = copy(original)
    deep = deepcopy(original)

    original.set_weights.append(40)

    print(f"Original : {original.set_weights}")
    print(f"Shallow  : {shallow.set_weights}")
    print(f"Deep     : {deep.set_weights}")

    # Explanation:
    # A shallow copy copies the object, but nested mutable objects are still shared.
    # So original.set_weights and shallow.set_weights refer to the same list object.
    # A deep copy copies everything recursively, including nested objects.
    # So deep.set_weights is a separate independent list.
    # After modifying original.set_weights, shallow is affected but deep is not.

# TODO 6:
# Student-created extension.
# Compares two WeightedExercise objects and reports which has higher total volume.

def compare_volume(exercise_a, exercise_b):
    print("\n=== Volume Comparison ===")
    volume_a = exercise_a.total_volume()
    volume_b = exercise_b.total_volume()

    print(f"{exercise_a.name}: {volume_a}{exercise_a.unit}")
    print(f"{exercise_b.name}: {volume_b}{exercise_b.unit}")

    if volume_a > volume_b:
        print(f"{exercise_a.name} has the higher training volume.")
    elif volume_b > volume_a:
        print(f"{exercise_b.name} has the higher training volume.")
    else:
        print("Both exercises have equal training volume.")

# TODO 5:
# Complete the main function.
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    exercise = Exercise("Push-up", "Chest", 3, 12)
    print("\nParent Object:")
    print(exercise.display_info())

    weighted = WeightedExercise("Bench Press", "Chest", 4, 8, 135)
    print("\nChild Object:")
    print(weighted.display_info())

    print("\nInheritance Demo:")
    print(f"Parent display_info(): {exercise.display_info()}")
    print(f"Child  display_info(): {weighted.display_info()}")
    print(f"Total Volume: {weighted.total_volume()}")

    demonstrate_namespaces()
    demonstrate_copying()

    leg_press = WeightedExercise("Leg Press", "Quadriceps", 3, 10, 145)
    rdl = WeightedExercise("RDL", "Hamstrings", 3, 10, 35)
    compare_volume(leg_press, rdl)

    # Edge case: two exercises with equal total volume
    tie_a = WeightedExercise("Lat Pulldown", "Back", 3, 10, 50)
    tie_b = WeightedExercise("Shoulder Press", "Shoulders", 5, 6, 50)
    compare_volume(tie_a, tie_b)

if __name__ == "__main__":
    main()