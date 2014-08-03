import FizzBuzzModule


if __name__ == '__main__':
    number = 0
    for number in range(101):
        result = FizzBuzzModule.get_answer(number)
        print(result)