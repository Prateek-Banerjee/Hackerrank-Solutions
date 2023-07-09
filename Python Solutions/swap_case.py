def swap_case(s):
    es = str()
    for i in range(len(s)):
        if s[i].islower()==True: es = es + s[i].upper()
        elif s[i].isupper()==True: es = es + s[i].lower()
        else: es = es + s[i]
    return es

