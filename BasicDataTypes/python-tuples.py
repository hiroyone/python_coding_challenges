if __name__ == "__main__":
    n = int(input())
    integer_list = map(int, input().split())
    integer_tuple = tuple(i for i in integer_list)
    hashed = hash(integer_tuple)
    print(hashed)
