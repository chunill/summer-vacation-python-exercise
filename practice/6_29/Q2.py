# zerojudge: https://zerojudge.tw/ShowProblem?problemid=a216
def f(n):
    return (n**2 + n) / 2
def g(n):
    return n * (n**2 + 3*n + 2) / 6

def main():
    while True:
        try:
            n = int(input())
        except:
            break
        print(int(f(n)), int(g(n)))
main()