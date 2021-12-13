"""
273. Integer to English Words
Convert a non-negative integer num to its English words representation.

Example 1:

Input: num = 123
Output: "One Hundred Twenty Three"
Example 2:

Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"
Example 3:

Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"
Example 4:

Input: num = 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One"
"""


def translate(num):
    digits = [_ for _ in str(num)]
    partitions = []
    l = len(digits)
    while l:
        partitions.append(digits[max(0, l-9):l])
        l = max(0, l-9)
    words = ""
    for i in range(len(partitions)):
        if i>0:
            words += "billion "
        words += billion(partitions[i]) + " "
    return words


def billion(p):
    words = ""
    if len(p)>7:
        million_words = hundred(p[0:len(p)-6])
        words += million_words + " "
        if million_words:
            words += "million "

    if len(p)>3:
        thousand_words = hundred(p[max(0, len(p)-6):len(p)-3])
        words += thousand_words + " "
        if thousand_words:
            words += "thousand "

    words += hundred(p[max(0, len(p)-3): len(p)]) + " "
    return words


MAP1 = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "0": "",
}

MAP2 = {
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "forteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
}
MAP3 = {
    "0":"",
    "2": "twenty",
    "3": "thirty",
    "4": "forty",
    "5": "fifty",
    "6": "sixty",
    "7": "seventy",
    "8": "eighty",
    "9": "ninety",
}


def hundred(p):
    words = ""
    if len(p)>2:
        hundred_word = MAP1[p[0]]
        words += hundred_word + " "
        if hundred_word:
            words += "hundred "

    if len(p)>1:
        tenth = p[len(p)-2]
        if tenth=='1':
            words += MAP2[p[len(p)-2:len(p)]] + " "
        else:
            words += MAP3[p[len(p)-2]] + " "
            words += MAP1[p[len(p)-1]] + " "
    return words


print(translate(345678))