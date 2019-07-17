# palindrome.py

def main():
    with open('pwords.txt','r') as file:
        words = file.readlines()
        for word in words:
            word = word[:-1]
            if word == word[::-1]:
                 print(word)

main()
            
