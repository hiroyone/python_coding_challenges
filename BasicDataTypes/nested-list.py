# The first line contains an integer, , the number of students.
# The  subsequent lines describe each student over  lines.
# - The first line contains a student's name.
# - The second line contains their grade.

if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append((name, score))
        sorted_students = sorted(students, key=lambda x: x[0])
        set_scores = set([y for x, y in students])
        set_scores.remove(min(set_scores))
        second_lowest = float(min(set_scores))
        for name, score in sorted_students:
            if score == second_lowest:
                print(name)
