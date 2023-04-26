import prompt
import random

def welcome_user():
    name = prompt.string('Могу я узнать твое имя? ')
    print(f'Привет, {name}!')
    return name


def get_example():
    x = random.randint(1, 25)
    y = random.randint(1, 25)
    symbol = random.choice(['+', '-', '*'])
    return f'{x} {symbol} {y}'

def get_correct_answer(example):
    try:
        correct_answer = eval(example)
        return str(correct_answer)
    except:
        print('Что-то пошло не так...')

def calc():
    count_true_answer = 0
    while True:
        example = get_example()
        print(example)
        correct_answer = get_correct_answer(example)
        answer = input('Твой ответ: ')
        if answer == correct_answer:
            count_true_answer += 1
            if count_true_answer == 3:
                break
            else:
                print('Правильно!')
        else:
            print(f'"{answer}" - неправильный ответ ;(. Правильным ответом было "{correct_answer}"')
            break
    return count_true_answer

def main():
    print('brain_calc \n')
    print('Добро пожаловать в игры разума!')
    name = welcome_user()
    print('Посчитайте значение выражения')
    count_correct_answer = calc()
    if count_correct_answer == 3:
        print(f'Превосходно, {name}!')
    else:
        print(f'Попробуем позже, {name}!')
    

if __name__ == '__main__':
    main()
    