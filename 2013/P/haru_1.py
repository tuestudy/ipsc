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

    #
    # hard
    #
    "minus seven", "minus six", "-",

    # IPSC 2012: http://ipsc.ksp.sk/2012/real/problems/
    "evil matching", "fair coin toss", "-",

    # Solar System: http://en.wikipedia.org/wiki/Solar_System
    "saturn", "uranus", "-",

    "iiiiiiiiiiiiiiiiiiiiiiiiiiiii",
    "iiiiiiiiiiiiiiiiiiiiiiiiiiiiii",
    "-",

    # Pokemon: http://pokemondb.net/pokedex/ekans
    "ekans", "arbok", "-",

    # Spanish: 34 -> 35
    #   https://translate.google.com/#es/en/treinta%20y%20cuatro
    #   https://translate.google.com/#en/es/thirty%20five
    "treinta y cuatro", "treinta y cinco", "-", # spanish

    # morse code: 49 -> 50
    #   http://morsecode.scphillips.com/morse.html
    "di-di-di-di-dah dah-dah-dah-dah-dit", # morse code
    "di-di-di-di-dit dah-dah-dah-dah-dah",
    "-",

    # binary number: 110111 -> 111000
    "one-one-zero-one-one-one",
    "one-one-one-zero-zero-zero",
    "-",

    # reversed number string: 57 -> 58
    "neves-ytfif", "thgie-ytfif", "-",

    # permutation
    "abcdefghijklmnopqrstuxyzwv",
    "abcdefghijklmnopqrstuxzvwy", "-",

    # sixty-nine -> seventy
    "51x7y-n1n3", "53v3n7y", "-",

    # Deutsch: 73 ->74
    #   https://translate.google.com/#de/en/dreiundsiebzig
    #   https://translate.google.com/#en/de/seventy%20four
    "dreiundsiebzig",
    "vierundsiebzig", "-",

    # French: 74 -> 75
    #   https://translate.google.com/#fr/en/soixante-quatorze
    #   https://translate.google.com/#en/fr/seventy%20five
    "soixante-quatorze",
    "soixante-quinze", "-",

    # Roman numeral: 78 -> 79
    #   http://www.onlineconversion.com/roman_numerals_advanced.htm
    "lxxviii",
    "lxxix", "-",

    # Periodic Table: gold(79) -> mercury(80)
    #   http://en.wikipedia.org/wiki/Periodic_table
    "gold", "mercury", "-",

    # Slovak: 89 -> 90
    #   https://translate.google.com/#sk/en/osemdesiat%20devat
    #   https://translate.google.com/#en/sk/ninety
    "osemdesiatdevat",
    "devatdesiat", "-"
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
