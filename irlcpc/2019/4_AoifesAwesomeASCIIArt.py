from utils import *

_, N = nums(input())
sentence = words(input())
longest = -1
for word in sentence:
    longest = max(longest, len(word))
width = longest + 2

def pprint(s: str):
    left = "* " + s
    n = len(left)
    remaining = width + 2 - n
    print(left, end="")
    print(" " * (remaining - 1) + "*")

header = ""
for i in range(longest + 4):
    if i % 2 == 0:
        header += "*"
    else:
        header += " "

available_space = longest
current = ""
i = 0
print(header)
while i < len(sentence):
    word = sentence[i]
    if not current:
        current = word
        available_space -= len(word)
        i += 1
    else:
        if len(word) < available_space:
            current += " " + word
            available_space -= len(word) + 1
            i += 1
        else:
            pprint(current)
            current = ""
            available_space = longest
if current:
    pprint(current)
print(header)



# * * * * * * *
# * Baking    *
# * is both   *
# * an art    *
# * and a     *
# * science.  *
# * * * * * * *