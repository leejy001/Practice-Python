# Palindrome2.py

class NotPalindromeError(Exception):
    def __init__ (self):
        super().__init__("Not palindrome")

def palindrome(word):
    if word != word[::-1]:
        raise NotPalindromeError
    else:
        print(word)

def main():
    try:
        word = input()
        palindrome(word)
    except NotPalindromeError as e:
        print(e)

main()
