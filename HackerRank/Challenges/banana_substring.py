def minion_game(string):
    vowels = 'AEIOU'
    for char in string:
        if char not in vowels:
            print(char)

if __name__ == '__main__':
    s = input()
    minion_game(s.upper())