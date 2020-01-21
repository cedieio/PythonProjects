def create_doormat(length, height):
    if length >= 5 and length <= 101 and height >= 15 and length <= 303:
        for i in range(1, length, 2):
            print(('.|.'  * i).center(height, '-'))
        print('WELCOME'.center(height, '-'))
        for i in range(length-2, -1, -2):
            print(('.|.'  * i).center(height, '-'))

if __name__ == '__main__':
    var1,var2 = list(map(int, input().split()))
    create_doormat(var1, var2)
