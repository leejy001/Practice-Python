#judge_file.py

def main(): 
    with open('words.txt', 'r') as file:
        lines = file.readline().split()
        for word in lines:
           if 'c' in word:
                print(word.strip(',.'))

main()
