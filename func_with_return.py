# Exercise 2

def my_avg(num1: int = 0, num2: int = 0) -> float:
    """
      This function is calculating the average of two numbers

      Parameters:
          the function get two integers

      Returns:
          the function return a float number
     """
    return (num1 + num2) / 2;


def my_headline(s: str) -> str:
    """
      This function is changing the string from lower - case letter to a capital letter
      and adding an exclamation mark in the end

      Parameters:
          the function get one string

      Returns:
          the function return a string
     """
    return s.upper() + "!";


def concat_list(first_l: list[int], second_l: list[int], third_l: list[int]) -> list[int]:
    """
      This function is concatenating three different lists to one list

      Parameters:
          the function get three lists of integers

      Returns:
          the function return a list of integers
      """
    return first_l + second_l + third_l;