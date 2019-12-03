if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    l_val = []
    for x_val in range(0, x + 1):
        for y_val in range(0, y + 1):
            for z_val in range(0, z + 1):
                if x_val + y_val + z_val != n:
                    l_val.append([x_val, y_val, z_val])

    
    print(l_val)