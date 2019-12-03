if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split()) 
    arr_list = set(arr)
    largest_num = max(arr_list)
    arr_list.remove(largest_num)
    print(max(arr_list))