calculate = input('please insert a calculation: ')
if '*' in calculate:
    action_place = calculate.index('*')
elif '/' in calculate:
    action_place = calculate.index('/')
elif '-' in calculate:
    action_place = calculate.index('-')
elif '+' in calculate:
    action_place = calculate.index('+')
number1 = calculate[0:int(action_place)]
action = calculate[action_place]
number2 = calculate[int(action_place)+int(1):len(calculate)]
if action is '*':
    result = int(number1) * int(number2)
elif action is '/':
    result = int(number1) / int(number2)
elif action is '-':
    result = int(number1) - int(number2)
elif action is '+':
    result = int(number1) + int(number2)
print('your calculation is: ', number1, action, number2)
print('result: ', result)
