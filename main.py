import random


def check(x, y):
    global mark

    if len(x) == 0 or x[0] != '-' and not x.isdigit():
        print("Incorrect format.")
        return "Error"
    if x.isdigit() and int(x) == y or x[0] == '-':
        print("Right!")
        mark += 1
    else:
        print("Wrong!")


print("""Which level do you want? Enter a number:
1 - simple operations with numbers 2-9
2 - integral squares of 11-29""")

one = "simple operations with numbers 2-9"
two = "integral squares of 11-29"

while True:
    level = input()

    if level.isdigit() and (int(level) == 1 or int(level) == 2):
        break
    else:
        print("Incorrect format.")

mark = 0

if int(level) == 1:
    for i in range(5):
        question = [random.randint(2, 9),
                    random.choice(['+', '-', '*']),
                    random.randint(2, 9)]

        print(question[0], question[1], question[2])

        ans = int
        if question[1] == '+':
            ans = int(question[0]) + int(question[2])
        elif question[1] == '-':
            ans = int(question[0]) - int(question[2])
        elif question[1] == '*':
            ans = int(question[0]) * int(question[2])

        answer = input()

        while check(answer, ans) == "Error":
            answer = input()
else:
    for i in range(5):
        question = random.randint(11, 29)
        print(question)

        answer = input()
        sqrt = question * question

        while check(answer, sqrt):
            answer = input()

print(f"You mark is {mark}/5. Would you like to save the result? "
      f"Enter yes or no.")

save_result = input()

if save_result.lower() in ['y', 'ye', 'yes', 'es']:
    print("What is your name?")
    user_name = input()

    file = open("results.txt", 'a', encoding='utf-8')
    file.write(f"{user_name}: {mark}/5 in level {level} "
               f"({one if int(level) == 1 else two})")
    file.close()

    print('The results are saved in "results.txt".')
