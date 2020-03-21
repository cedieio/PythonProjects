def merge_the_tools(string, k):
    value = len(string)//k
    for i in range(0, len(string), value):
        print(''.join(list(map(lambda s: '' if s not in string[i:i+value] else s , string[i:i+value]))))

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)