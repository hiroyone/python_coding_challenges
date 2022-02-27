def abcd_adjacent_eraser(S):
    # write your code in Python 3.6
    S = S.replace("AB", "")
    S = S.replace("BA", "")
    S = S.replace("CD", "")
    S = S.replace("DC", "")
    return S
