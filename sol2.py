import func_with_return as fr


def main():

    avg1: float = fr.my_avg(90, 99);
    print(avg1);
    help(fr.my_avg);
    head1: str = fr.my_headline("python has concurred the world");
    print(head1);
    print(head1);
    help(fr.my_headline);
    res_con: list[int] = fr.concat_list([1, 2], [3, 4, 5, 6], [7, 8, 9]);
    print(res_con);
    print(len(res_con));
    help(fr.concat_list);


if __name__ == "__main__":
    main()
