# Exercise 3
def say_bool(b: bool = True) -> str:
    return "yes" if b else "no";


print(say_bool(False));
print(say_bool(True));


# Exercise 4
def print_zugi(numbers_list: list[int] = []) -> list[str]:
    if not numbers_list:
        print("empty list");
        return [];

    return [f"{i} is {'even' if i % 2 == 0 else 'odd'}" for i in numbers_list];


print(print_zugi([5, 3, 2, 10, 15, 14, 14]));


# Exercise 5
def get_int(message: str) -> int:
    while True:
        try:
            number: int = int(input(message));
            return number;

        except Exception as e:
            print(f"Invalid input. Please enter an integer number ---{e}---...try again");


one_int: int = get_int("Please enter a number: ");
print(f"The number you entered is: {one_int}");

import statistics, func_without_return

grade_list: list[int] = [];
while True:
    grade: int = get_int("Please enter your grade: ");

    if grade == -99:
        break;

    if 0 <= grade <= 100:
        print("That is a valid grade");
        grade_list.append(grade);
    else:
        print("Grade must be between 0 and 100. Ignoring invalid grade.");

func_without_return.my_statistics(grade_list);

# Exercise 6
# If we print what came back from a function that has no return at all, what will we get? None
# If we print what is returned from a function that has None return, what will we get? None
# What is the similarity between break and return?
# break is jumping out of a loop immediately and return is jumping out of function immediately
