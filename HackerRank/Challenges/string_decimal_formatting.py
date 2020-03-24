def format_nums(num):
    width = len(bin(num)) - 2
    for i in range(1, num+1):
        print('{0:{width}d} {0:{width}o} {0:{width}X} {0:{width}b}'.format(i, width=width))

if __name__ == "__main__":
    n = int(input())
    format_nums(n)