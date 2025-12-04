import random
import time

MIN_OPERAND = 2
MAX_OPERAND = 10
OPERATORS = ["+", "-", "/", "*"]
TOTAL_PROBLEMS = 3

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right =random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = f"{str(left)} {operator} {str(right)}"
    answer = round(eval(expr),2)
    return expr, answer

wrong = 0

input("Press any key to begin!")
print("-------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem#{i+1}: {expr}= ")
        if guess == str(answer):
            break
        wrong +=1

end_time = time.time()
total_time = round(end_time - start_time, 2)

print("-------------------------")
if wrong <=1:
    print(f"Well done! You finished in {total_time}sec with {wrong} error!")
else:
    print(f"Well done! You finished in {total_time}sec with {wrong} errors!")
