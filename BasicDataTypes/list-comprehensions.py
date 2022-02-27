if __name__ == "__main__":
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    # Create a permutation list of all (i, j, k) where 0 =< i =< x, 0 =< j =< y, 0 =< k =< z except i + j+ k != n.
    li = [
        [x_num, y_num, z_num]
        for x_num in range(x + 1)
        for y_num in range(y + 1)
        for z_num in range(z + 1)
        if x_num + y_num + z_num != n
    ]
    print(li)
