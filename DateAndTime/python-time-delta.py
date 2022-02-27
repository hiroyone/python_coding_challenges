from datetime import datetime


def diff_sec(t1, t2):
    
    time_format = "%a %d %b %Y %H:%M:%S %z"
    d = datetime.strptime(t1, time_format) - datetime.strptime(t2, time_format)
    d_abs_int_sec = abs(int(d.total_seconds()))
    return d_abs_int_sec


if __name__ == "__main__":
    num = int(input())
    for _ in range(num):
        t1 = input()
        t2 = input()
        time_diff = diff_sec(t1, t2)
        print(time_diff)
