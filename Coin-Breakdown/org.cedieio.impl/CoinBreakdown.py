# Greedy algorithm

def coin_breakdown(amount):
    arr_val = []

    coins = [25, 10, 5, 1]
    for coin in coins:
        if amount >= coin:
            num_of_appearance = amount // coin
            arr_val.append("Coin {0}, number of times {1}".format(coin, num_of_appearance) )
            amount = amount - (num_of_appearance * coin)
    return arr_val


print (coin_breakdown(1))
print (coin_breakdown(26))
print (coin_breakdown(33))
print (coin_breakdown(38))


