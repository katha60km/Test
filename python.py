import math
price = 100000
has_good_credit = False

if has_good_credit:
    downpayment = 0.1 * price
    
else:
    downpayment = 0.2 * price

print(f'downpayment : {downpayment}')