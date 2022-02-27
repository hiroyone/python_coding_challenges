def find_missing_pos_int(a):
    pos_a = filter(lambda x: x > 0, a)
    unique_a = list(set(pos_a))
    sorted_a = sorted(unique_a)
    answer = 1
    for a in sorted_a:
        if answer == a:
            answer += 1
        else:
            break
    return answer
