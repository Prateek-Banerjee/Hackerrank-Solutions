import sys

class Solution:
    # Write your code here
    stack = list()
    queue = list()
    
    def __init__(self):
        super().__init__()
    
    def pushCharacter(self,ch):
        self.stack = [ch]+(self.stack)
    def enqueueCharacter(self,ch):
        self.queue.append(ch)
    def popCharacter(self):
        popped = []
        for i in self.stack:
            popped.append(i)
        return popped
    def dequeueCharacter(self):
        dequeued = []
        for i in self.queue:
            dequeued.append(i)
        return dequeued

# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    