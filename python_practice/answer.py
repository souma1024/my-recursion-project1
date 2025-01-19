import sys
sys.stdout.buffer.write(b'What is your favorite food?\n')
sys.stdout.flush()
food = sys.stdin.buffer.readline()
try:
    print('Thanks for letting me your favorite food is ' + food.decode())
except BrokenPipeError:
    sys.exit(0)