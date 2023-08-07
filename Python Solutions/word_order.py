# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
wordCount = dict()
for i in range(n):
    word = input()
    if word not in wordCount.keys():
        wordCount[word] = 1
    else:
        wordCount[word] += 1
print (len(wordCount.keys()))
for i in wordCount:
    print(wordCount.get(i),end=" ")
