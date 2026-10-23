import sys

def main():
    prev_value = 0
    for line in sys.stdin:
        line = line.removesuffix('\n')
        curr_value = int(line)
        if prev_value <= curr_value:
            value_is_bigger = True
        else:
            value_is_bigger = False
        prev_value = curr_value

    if value_is_bigger:
        print("The numbers are in ascending order.")
    else:
        print("The numbers are not in ascending order.")


if __name__ == "__main__":
    main()