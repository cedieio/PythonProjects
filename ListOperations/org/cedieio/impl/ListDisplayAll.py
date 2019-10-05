
words = ['Well','hello','there']

# display and override the \n to ' '
def print_to_oneline(words):
    for word in words:
        print(word, end=" ")

# reverse the string in two  ways

# The easy way ::-1 means include the beggining and end then start backwards
def reverse_easy_way(words):
    reverse_word = words[::-1]
    print_to_oneline(reverse_word)

def reverse_manual_way(words):
    for i in range(len(words) - 1, -1, -1):
        print(words[i], end=" ")


print_to_oneline(words)
print()
reverse_easy_way(words)
print()
reverse_manual_way(words)

numbers = [99, 20, 50]

def sum_of_list(x):
    ret_val = 0
    for num in x:
        ret_val += num
    return ret_val

print()
print("**** SUM OF Numbers {0}".format(sum_of_list(numbers)))

