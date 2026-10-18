from dfa_L import build_dfa_L
from dfa_L2 import build_dfa_L2
from counting import count_accepted

def read_n():
    while True:
        s = input("Enter a number: (1-300): ")
        if s.isdigit() and 1 <= int(s) <= 300:
            return int(s)
        print("Invalid input. Please enter a number between 1 and 300.")


def main():
    delta_L, accepting_L = build_dfa_L()
    delta_L2, accepting_L2 = build_dfa_L2(delta_L)

    while True:
        print()
        print("1) Count strings of length n in L")
        print("2) Count strings of length n in L' (middle two symbols aa)")
        print("3) Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            n = read_n()
            print(f"Number of strings of length {n} in L: {count_accepted(delta_L, accepting_L, n)}")
        elif choice == "2":
            n = read_n()
            if n % 2 == 1:
                count = 0
            else:
                count = count_accepted(delta_L2, accepting_L2, n // 2 - 1)
            print(f"Number of strings of length {n} in L': {count}")
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()