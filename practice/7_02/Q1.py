def recurrence(from_t, to_t,three_t, N):
    if N == 1:
        print(f"Move ring {N} from {from_t} to {to_t}")
    else:
        recurrence(from_t, three_t, to_t, N-1)
        print(f"Move ring {N} from {from_t} to {to_t}")
        recurrence(three_t, to_t, from_t, N-1)

def main():
    while True:
        try:
            N = int(input())
        except:
            break
        recurrence("A", "C", "B", N)

main()