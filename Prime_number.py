# prime_number.py

def prime_number_generator(start,stop):
    for i in range(start,stop):
        chk = True
        for j in range(2, i):
            if i%j == 0:
                chk = False
        if chk:
            yield i

def main():
    start, stop = map(int, input().split())
 
    g = prime_number_generator(start, stop)
    print(type(g))
    for i in g:
        print(i, end=' ')

main()
