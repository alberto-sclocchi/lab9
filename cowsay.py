import sys
from heifer_generator import get_cows

def list_cows(cows):
    return [cow.name for cow in cows]

def get_cow(name, cows):
    for cow in cows:
        if cow.name == name:
            return cow

    return None


def main():
    system_argument = sys.argv
    cows = get_cows()
    cows_available = list_cows(cows)

    if system_argument[-1] == "-l":
        print("Cows available:", end=" ")
        print(" ".join(cows_available))
    elif "-n" not in system_argument:
        cow = get_cow("heifer", cows)
        print(" ".join(system_argument[1:]))
        print(cow.image)
    else:
        if system_argument[2] in cows_available:
            cow = get_cow(system_argument[2], cows)
            print(" ".join(system_argument[3:]))
            print(cow.image)
        else:
            print(f"Could not find {system_argument[2]} cow!")

if __name__ == "__main__":
    main()