if __name__ == "__main__":
    N = int(input())
    answer = []
    for _ in range(N):
        lines = input().split()
        command = lines[0]
        li = list(map(int, lines[1:]))
        if command == "insert":
            answer.insert(li[0], li[1])
        elif command == "append":
            answer.append(li[0])
        elif command == "remove":
            answer.remove(li[0])
        elif command == "sort":
            answer.sort(reverse=False)
        elif command == "reverse":
            answer.reverse()
        elif command == "pop":
            answer.pop()
        elif command == "print":
            print(answer)
