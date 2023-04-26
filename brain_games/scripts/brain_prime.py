import random
import prompt


def welcome_user():
    name = prompt.string('Могу я узнать твое имя? ')
    print(f'Привет, {name}!')
    return name


def is_prime(x):
    for i in range(2, (x//2 + 1)):
        if x % i == 0:
            return False
    return True

def get_correct_answer(x):
    return 'да' if is_prime(x) else 'нет'



def even_or_odd():
    count_true_answer = 0
    while True:
        x = random.randint(1, 1000)
        print(f'Вопрос: {x} простое?')
        answer = input('Твой ответ: ')
        correct_answer = get_correct_answer(x)
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
    print('brain_prime \n')
    print('Добро пожаловать в игры разума!')
    name = welcome_user()
    print('Ответьте "да", если число простое, в противном случае ответьте "нет".')
    count_correct_answer = even_or_odd()
    if count_correct_answer == 3:
        print(f'Превосходно, {name}!')
    else:
        print(f'Попробуем позже, {name}!')


if __name__=='__main__':
    main()