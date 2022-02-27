def merge_the_tools(string, k):
    split_num = len(string) // k
    for n in range(split_num):
        unique_char = "".join(set(string[k * n : k * (n + 1)]))
        print(unique_char)


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
