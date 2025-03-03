import re
from functools import reduce

pat = re.compile(
    r"one|two|three|four(?!teen)(?!ty)|five|six(?!teen)(?!ty)|seven(?!teen)(?!ty)|eight(?!een)(?!y)|nine(?!teen)(?!ty)"
    r"|ten|eleven|twelve|thirteen|fourteen||fifteen|sixteen|seventeen|eighteen|nineteen"
    r"|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety"
    r"|hundred"
)

def strToNum(s: str) -> int:
    return {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
    }[s]

def digitToStr(d: str) -> str:
    return {
        "0": "",
        "1": "one",
        "2": "two",
        "3": "three",
        "4": "four",
        "5": "five",
        "6": "six",
        "7": "seven",
        "8": "eight",
        "9": "nine",
    }[d]

def tensToStr(s: str) -> str:
    # print("tens", s, type(s))
    if s[0] == "0":
        return digitToStr(s[-1])
    teens = {
        "11": "eleven",
        "12": "twelve",
        "13": "thirteen",
        "14": "fourteen",
        "15": "fifteen",
        "16": "sixteen",
        "17": "seventeen",
        "18": "eighteen",
        "19": "nineteen"
    }
    tens = {
        "1": "ten",
        "2": "twenty",
        "3": "thirty",
        "4": "forty",
        "5": "sixty",
        "6": "sixty",
        "7": "seventy",
        "8": "eighty",
        "9": "ninety"
    }
    if s in teens.keys():
        return teens[s]
    num = int(s)
    if num % 10 == 0:
        return tens[str(num // 10)]
    else:
        return tens[str(num // 10)] + digitToStr(str(num % 10))


for _ in range(1000):
    line = input()
    if line == "zero":
        print("one")
        continue
    components = list(filter(lambda c: c != "", re.findall(pat, line)))
    # print(components)
    acc = reduce(lambda lhs, rhs: lhs * 100 if rhs == "hundred" else lhs + strToNum(rhs), components, 0)
    # print(acc)
    succ = str(acc + 1)
    # print(succ)
    if succ == "1000":
        print("onethousand")
        continue
    if len(succ) == 1:
        print(digitToStr(succ[-1]))
        continue
    ans = ""
    if len(succ) >= 2:
        ans = tensToStr(succ[-2] + succ[-1])
    if len(succ) >= 3:
        hundreds_str = digitToStr(succ[-3])
        if ans == "":
            ans = hundreds_str + "hundred"
        else:
            ans = hundreds_str + "hundredand" + ans
    print(ans)