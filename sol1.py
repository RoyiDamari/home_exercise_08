import func_without_return as fp


def main():
    fp.my_ascending(-12, 7);
    help(fp.my_ascending);
    fp.my_details("AI is the best");
    help(fp.my_details);
    fp.say_bool(False);
    fp.say_bool(True);
    help(fp.say_bool);
    fp.print_zugi([5, 3, 2, 10, 15, 14, 14]);
    help(fp.print_zugi);

    grade_list: list[int] = [];
    while True:
        try:
            grade: int = int(input("Please enter your grades: "));

            if grade == -99:
                break;

            if 0 <= grade <= 100:
                print("That is a valid grade");
                grade_list.append(grade);
            else:
                print("Grade must be between 0 and 100. Ignoring invalid grade.");

        except Exception as e:
            print(f"Invalid input. Please enter an integer score ---{e}---...try again");

    fp.my_statistics(grade_list);
    help(fp.my_statistics);

if __name__ == "__main__":
    main()

