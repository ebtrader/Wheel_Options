# import random
# from random import random
from random import randint

import Fire_Trades
from Fire_Trades import TradeFire

# random_number = random()
# print(random_number)

random_number = randint(1, 100)
print(random_number)
if random_number > 50:
    Fire_Trades.main()
else:
    print('not high enough')


# lst = []
#
# for i in range(10):
#     random_number = random()
#     lst.append(random_number)
#
# # Prints random items
# print(lst)
