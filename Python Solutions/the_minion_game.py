def minion_game(string):
    # your code goes here
    vowel_count = consonant_count = 0
    length = len(string)
    for i in range(length):
        if string[i] in "AEIOU":
            vowel_count+=(length-i)
        else:
            consonant_count+=(length-i)
    
    if vowel_count > consonant_count:
        print(f"Kevin {vowel_count}")
    elif vowel_count < consonant_count:
        print(f"Stuart {consonant_count}")
    else:
        print("Draw")

if __name__ == '__main__':
    s = input()
    minion_game(s)