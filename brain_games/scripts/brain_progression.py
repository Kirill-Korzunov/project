import random
import prompt



def welcome_user():
    name = prompt.string('Могу я узнать твое имя? ')
    print(f'Привет, {name}!')
    return name


def get_full_progression(start:int, stop:int, step:int):
    start = min(start, stop)
    end = max(start, stop)
    while not 5 <= (end - start) // step <= 10:
        if end - start < step:
            end += step * 10
        else:
            end -= step
    return [i for i in range(start, end, step)]


def get_example_and_correct_answer(progression, random_index):
    if random_index > len(progression):
        random_index = -1  
    correct_answer = str(progression[random_index])
    progression[random_index] = '...'
    return progression, correct_answer
    



def progression():
    count_true_answer = 0
    while True:
        start = random.randint(1, 1000)
        stop = random.randint(1, 1000)
        step = random.randint(1,25)
        random_index = random.randint(0, 10)
        example, correct_answer = get_example_and_correct_answer(get_full_progression(start, stop, step), random_index)
        print('Вопрос:', end=' ')
        print(*example)
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
    print('brain_progression \n')
    print('Добро пожаловать в игры разума!')
    name = welcome_user()
    print('Заполните пропуск')
    count_correct_answer = progression()
    if count_correct_answer == 3:
        print(f'Превосходно, {name}!')
    else:
        print(f'Попробуем позже, {name}!')


if __name__=='__main__':
    main()