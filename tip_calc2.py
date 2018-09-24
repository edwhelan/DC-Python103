total_bill = float(input('Total bill amount? '))
level_of_service = str(input('Level of Service? (good, fair, bad) '))

number_of_people = int(input('Split how many ways?'))

if level_of_service == 'good':
    tip_value = float(.20)
elif level_of_service == 'fair':
    tip_value = float(.15)
else:
    tip_value = float(.10)

tip_amount = float(total_bill * tip_value)
total_with_tip = float(total_bill + tip_amount)
split_total = float(total_with_tip / number_of_people)

print('Tip amount? $%.2f' % (tip_amount))
print('Total bill amount? $%.2f' % (total_with_tip))
print('Amount per person: $%.2f' % (split_total))