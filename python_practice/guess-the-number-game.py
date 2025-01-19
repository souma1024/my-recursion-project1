import sys, random

def get_number(args):
    print(f'{args}\n')
    return int(sys.stdin.buffer.readline().strip().decode())

print('Enter two numbers\n')
num1 = get_number('Enter the one number')
num2 = get_number('Enter the other number')

max_val = num1 if num1 > num2 else num2
min_val = num1 if num1 <= num2 else num2
    
random_num = random.randint(min_val, max_val)
attempt_limit_num = int((max_val - min_val) / 2)

while True:
    print(f'Guess the number between {min_val} and {max_val} by {attempt_limit_num} more times')
    input_val = (int)(sys.stdin.buffer.readline().strip().decode())
    if input_val == random_num or attempt_limit_num == 1:
        break
    attempt_limit_num -= 1

if input_val == random_num:
    print(f'Correct! You guessed the number {random_num}')
else:
    print(f'Failure!, the answer is {random_num}!')