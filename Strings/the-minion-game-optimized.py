# Time Complexity for this solution is O(N)


def is_vowel(ch):
    return ch in "AaEeIiOoUu"


# Count vowels and consonants from the alphabet frequency dictionary
def count_phonics(frequency_dict):
    vowel_count = 0
    consonant_count = 0
    for letter, frequency in frequency_dict.items():
        if is_vowel(letter):
            vowel_count += frequency
        else:
            consonant_count += frequency
    return (vowel_count, consonant_count)


def count_substring_initials(string):
    alphabet_frequency = {}
    length = len(string)
    for i in range(len(string)):
        # The number of times substrings appears with the letter:string[i]
        if string[i] in alphabet_frequency:
            alphabet_frequency[string[i]] += length - i
        else:
            alphabet_frequency[string[i]] = length - i
    return alphabet_frequency


def cal_total(string):
    alphabet_frequency = count_substring_initials(string)
    (vowel_count, consonant_count) = count_phonics(alphabet_frequency)
    kevin_score = vowel_count
    stuart_score = consonant_count
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
