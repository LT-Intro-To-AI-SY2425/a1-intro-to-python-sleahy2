
"""problem 1"""
def fizbuzz(input_num):
    if(input_num%3==0):
        if(input_num%5==0):
            return 'FizzBuzz'
        return 'Fizz'
    elif(input_num%5==0):
        return 'Buzz'
    else:
        return input_num

assert fizbuzz(1) == 1, "fizzbuzz 1 test"
assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
assert fizbuzz(4) == 4, "fizzbuzz 4 test"
assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

"""1. Palindrome Checker 
    Write a function that checks if a given string is a palindrome (reads the same forward and backward)."""

def is_palindrome(word):
    chars = list(word)
    return chars == chars[::-1]

word = "radar"
print(is_palindrome(word))
word = "firetruck"
print(is_palindrome(word))  

"""2. Count Number of Vowels in a String"""
def vowels(str):
    numVowels = 0
    vowel = "aeiouAEIOU"

    for char in str:
        if char in vowel:
            numVowels += 1
    return numVowels

result = vowels("Sean Leahy")
print(result) # Output 3



"""3. Addition Calculator"""

def calc():
    userInput = float(input("Enter First Number:"))
    userInput1 = float(input("Enter Second Number:"))
    ans = userInput + userInput1
    return ans

ans = calc()
print(ans)