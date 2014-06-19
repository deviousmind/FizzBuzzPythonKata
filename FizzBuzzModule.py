class FizzBuzz:

    @staticmethod
    def get_answer(number):
        if(number == 3):
            return 'fizz'
        elif(number == 5):
            return 'buzz'

        return number.__str__()

