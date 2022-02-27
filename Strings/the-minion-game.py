# Time Complexity for this solution is O(N**2)


def is_vowel(ch):
    return ch in "AaEeIiOoUu"


def count_phonics(words):
    vowel_count = 0
    consonant_count = 0
    for word in words:
        if is_vowel(word[0]):
            vowel_count += 1
        else:
            consonant_count += 1
    return (vowel_count, consonant_count)


def make_substr_initial(string):
    return (
        string[i : i + num + 1]
        for num in range(len(string))
        for i in range(len(string))
        if len(string[i : i + num + 1]) == num + 1
    )


def cal_total(string):
    kevin_score = 0
    stuart_score = 0
    substr_list = make_substr_initial(string)
    (vowel_count, consonant_count) = count_phonics(substr_list)
    kevin_score += vowel_count
    stuart_score += consonant_count
    return (kevin_score, stuart_score)


def minion_game(string):
    kevin_score, stuart_score = cal_total(string)
    if kevin_score > stuart_score:
        print("Kevin {}".format(kevin_score))
    elif kevin_score < stuart_score:
        print("Stuart {}".format(stuart_score))
    else:
        print("Draw")


if __name__ == "__main__":
    s = input()
    minion_game(s)
