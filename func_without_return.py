# Exercise 1
def my_ascending(num1: int = 0, num2: int = 0) -> None:
    """
      This function is printing two numbers in ascending order

      Parameters:
          the function get two integers

      Returns:
          the function doesn't return any value
      """
    print(min(num1, num2));
    print(max(num1, num2));


def my_details(s: str = "") -> None:
    """
      This function is printing the first, middle, and the last letter of the string

      Parameters:
          the function get one string

      Returns:
          the function doesn't return any value
      """
    if not s:
        print("empty parameter");
        return;
    print(f"First letter is: {s[0]}");
    print(f"Middle letter is: {s[(len(s) // 2)]}");
    print(f"Last letter is: {s[-1]}");


def say_bool(b: bool = True) -> None:
    """
      This function is printing yes if the boolean it get is True,
      no if the boolean it get is False

      Parameters:
          the function get one boolean

      Returns:
          the function doesn't return any value
      """
    print("yes" if b else "no");


def print_zugi(numbers_list: list[int] = []) -> None:
    """
         This function is printing for ech number in the list,
         even if the number in the list is even,
         odd if the number in the list is odd

         Parameters:
             the function get a list of integers

         Returns:
             the function doesn't return any value
         """
    if not numbers_list:
        print("empty parameter");
        return;

    print([f"{i} is {'even' if i % 2 == 0 else 'odd'}" for i in numbers_list]);


import statistics


def my_statistics(grades_list: list[int]) -> None:
    """
            This function is printing the number of grades in the list,
            the maximum and minimum grade,
            the average grade,
            the number of grades above 90,
            the number of grades below 55,
            and the standard deviation

            Parameters:
                the function get a list of integers

            Returns:
                the function doesn't return any value
            """
    number_of_grades: int = len(grades_list);
    print(f"The highest score is: {max(grades_list)}");
    print(f"The lowest score is: {min(grades_list)}");
    print(f"The numbers of scores is: {len(grades_list)}");
    print(f"The average of scores is: {sum(grades_list) / number_of_grades}");
    print(f"The number of passing scores above 90 is: \
         {len([grade for grade in grades_list if grade > 90])}");
    print(f"The number of falling scores below 55 is: \
         {len([grade for grade in grades_list if grade < 55])}");
    print(f"Standard deviation: {statistics.stdev(grades_list) if number_of_grades > 1 else 0:.2f}");

