import argparse

def greet(name):
    print(f'Hello {name}')

def square(number):
    print(number ** 2)

def add(a, b):
    print(a+b)

def greet(name, debug):
    if debug:
        print('Calling greet function')
    print(f'Hello {name}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # "name" is positional argument
    parser.add_argument("name", type=str, help="name to be greeted")
    p = parser.parse_args()
    greet(p.name)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # "n" is positional argument
    parser.add_argument("n", type=int, help="Number to be squared")
    p = parser.parse_args()
    square(p.n)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # "a" and "b" are positional arguments
    parser.add_argument("a", type=int)
    parser.add_argument("b", type=int)
    p = parser.parse_args()
    add(p.a, p.b)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # "name" is positional argument
    parser.add_argument("name", type=str, help="name to be greeted")
    # --debug is keyword argument
    parser.add_argument("--debug", type=bool)
    p = parser.parse_args()
    greet(p.name, p.debug)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # "name" is positional argument
    parser.add_argument("name", type=str, help="name to be greeted")
    # --debug is keyword argument
    parser.add_argument("--debug", action="store_true")
    # If --debug option is mentioned in command line, assign the value True to p.debug. Not specifying it implies False. 
    p = parser.parse_args()
    greet(p.name, p.debug)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    # "name" is positional argument
    parser.add_argument("name", type=str, help="name to be greeted")
    # --debug is keyword argument
    # -d is short-cut. Insted of using --debug in the command line, we can specify -d
    parser.add_argument("-d", "--debug", action="store_true")
    p = parser.parse_args()
    greet(p.name, p.debug)

# ==================================================================
def word_count(word):
    from collections import defaultdict
    d = defaultdict(int)
    with open('./sample.log') as f:
        for line in f:
            if word in line:
                d[word] += 1
    return d

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-word", "--word", type=str)
    p = parser.parse_args()
    print(word_count(p.word))    
# ==================================================================
from requests import request
import json

def validate_code(ifsc_code):
    url = f"https://ifsc.razorpay.com/{ifsc_code}"
    response = request("GET", url)
    json_response = json.loads(response.text)
    try:
        return json_response['BRANCH']
    except TypeError:
        return f"******* Invalid IFSC Code ******** {ifsc_code}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--code", type=str)
    # it is needed to return the data from the arguments specified options 
    p = parser.parse_args()
    print(validate_code(p.code))
