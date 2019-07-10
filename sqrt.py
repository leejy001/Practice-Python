# sqrt.py

def main():
    num1, num2 = map(int, input().split())
    for i in range (num1, num2+1):
        a = [2 ** i for i in range(num1, num2+1)]
    a.pop(1)
    a.pop(-2)
    print(a)

main()
