if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    num_set = set(arr)
    num_set.remove(max(num_set))
    second_max = max(num_set)
    print(second_max)