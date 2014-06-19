class FizzBuzz:

    @staticmethod
    def get_answer(number):
        if(number % 3 == 0 == number % 5):
            return 'fizzbuzz'
        elif(number % 3 == 0):
            return 'fizz'
        elif(number % 5 == 0):
            return 'buzz'

        return number.__str__()

