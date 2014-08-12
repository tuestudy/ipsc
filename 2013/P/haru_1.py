import sys

numbers = ["minus one", "zero",
    "one", "two", "three", "four", "five",
    "six", "seven", "eight", "nine", "ten",
    "eleven", "twelve", "thirteen", "fourteen", "fifteen", 
    "sixteen", "seventeen", "eighteen", "nineteen", "twenty",
    "twenty-one", "-",
    "twenty-nine", "thirty", "thirty-one", "-",
    "thirty-nine", "fourty", "fourty-one", "-",
    "fourty-nine", "fifty", "fifty-one", "-",
    "fifty-nine", "sixty", "sixty-one", "-",
    "sixty-nine", "seventy", "seventy-one", "-",
    "seventy-nine", "eighty", "eighty-one", "-",
    "eighty-nine", "ninety", "ninety-one", "-",
]

def find_next_english_number(num):
    try:
        idx = numbers.index(num)
        return numbers[idx + 1]
    except:
        return None

def main():
    for line in sys.stdin:
        a = line.strip()
        try:
            print int(a) + 1
        except ValueError, e:
            result = find_next_english_number(a)

            if result == None and '-' in a:
                a1, a2 = a.split('-')
                result = a1 + '-' + find_next_english_number(a2)

            print result

if __name__ == '__main__':
    main()
