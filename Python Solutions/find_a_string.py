def count_substring(string, sub_string):
    cnt = 0
    for i in range(len(string)):
        if sub_string == string[i:(i+(len(sub_string)))]:
            cnt += 1
    return cnt
