def minion_game(string):
    stuart = 0
    kevin = 0
    n = len(string)
    vowels = 'AEIOU'
    for i in range(n):
        if string[i] in vowels:
            kevin += n - i
        else:
            stuart += n - i
    
    if stuart > kevin:
        print('Stuart {0}'.format(stuart))
    elif stuart < kevin:
        print('Kevin {0}'.format(kevin))
    else:
        print('Draw')

if __name__ == '__main__':
    s = input()
    minion_game(''.join((s.upper())))