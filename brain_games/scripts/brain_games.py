#!/usr/bin/env python3
import prompt


def welcome_user():
    name = prompt.string('Могу я узнать твое имя? ')
    print(f'Привет, {name}!')
    return name


def main():
    print('Добро пожаловать в игры разума!')


if __name__ == '__main__':
    main()
