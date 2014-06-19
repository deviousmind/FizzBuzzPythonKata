class FizzBuzz:

    @staticmethod
    def get_answer(number):
        if(number == 3):
            return 'fizz'

        return number.__str__()

