print("Minimum number of students in each class")


def allocate_classes(number_of_students):
    number_of_classes = number_of_students // 10
    remaining_students = number_of_students % 10

    classes = []
    allocation = {}

    for i in range(number_of_classes):
        name_of_class = f"Class {i + 1}"
        number_of_students_in_class = 10
        classes.append(name_of_class)
        allocation[name_of_class] = number_of_students_in_class

    if remaining_students > 0:
        name_of_class = f"Class {number_of_classes + 1, 3}"
        classes.append(name_of_class)
        allocation[name_of_class] = remaining_students

    classes_string = ", ".join(classes)

    print(f"Proposed Allocation: {classes_string}")
    print("Allocation:")
    for name_of_class, number_of_students in allocation.items():
        print(f"{name_of_class}: {number_of_students} students")


# Test the function
total_number_of_students = 39
allocate_classes(total_number_of_students)

total_number_of_students2 = 87
allocate_classes(total_number_of_students2)

