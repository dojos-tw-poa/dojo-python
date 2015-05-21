

class FizzBuzz():
    def generate_response(self, number):
        response = ""
        if (number % 3 == 0):
            response = "Fizz"
        if (number % 5 == 0):
            response += "Buzz"

        if response:
            return response

        return number



if __name__ == '__main__':
    FizzBuzz.main()
