if __name__ == '__main__':
    N = int(input())
    action_list = []
    for num in range(N):
        input_val = str(input())
        if input_val is not '':
            input_val_array = input_val.split()
            if input_val_array[0] == 'print':
                print(action_list)
            elif input_val_array[0] == 'insert':
                if len(input_val_array) == 3:
                    action_list.insert(int(input_val_array[1]), int(input_val_array[2]))
            elif input_val_array[0] == 'append':
                action_list.append(int(input_val_array[1]))
            elif input_val_array[0] == 'remove':
                if len( action_list ) > 0:
                    action_list.remove(int(input_val_array[1]))
            elif input_val_array[0] == 'pop':
                if len( action_list ) > 0:
                    action_list.pop()
            elif input_val_array[0] == 'reverse':
                action_list.reverse()
            elif input_val_array[0] == 'sort':
                action_list.sort()