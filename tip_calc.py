# total_bill = float(input('Total bill amount? '))
# level_of_service = str(input('Level of Service? (good, fair, bad) '))

# if level_of_service == 'good':
# 	print('Tip amount: $'+ str(float(total_bill) * float(.20)))
# 	print('Total amount: $'+ str(float(total_bill) + total_bill * float(.20)))
# elif level_of_service == 'fair':
# 	print('Tip amount: $' + str(float(total_bill) * float(.15)))
# 	print('Total amount: $' + str(float(total_bill) + total_bill * float(.15)))
# else:
# 	print('Tip amount: $' + str(float(total_bill) * float(.10)))
# 	print('Total amount: $' + str(float(total_bill) +  total_bill * float(.10)))

#take input from user
total_bill = float(input('Total bill amount? '))
level_of_service = str(input('Level of Service? (good, fair, bad) '))

#establish the tipping value
if level_of_service == 'good':
    tip_value = float(.20)
elif level_of_service == 'fair':
    tip_value = float(.15)
else:
    tip_value = float(.10)

#do the maths with values
tip_amount = float(total_bill * tip_value)
total_with_tip = float(total_bill + tip_amount)

#print amount
print('Tip amount? $%.2f' % (tip_amount))
print('Total bill amount? $%.2f' % (total_with_tip))  