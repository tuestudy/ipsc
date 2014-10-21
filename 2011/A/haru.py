
game_table = {
    'scissors': ['Spock', 'rock'],
    'paper': ['scissors', 'lizard'],
    'rock': ['paper', 'Spock'],
    'lizard': ['rock', 'scissors'],
    'Spock': ['lizard', 'paper']
};

def main():
    t = input()
    result = []
    for _ in range(t):
        x = raw_input()

        if len(result) > 0 and result[-1] == game_table[x][0]:
            result.append(game_table[x][1])
        else:
            result.append(game_table[x][0])

    for x in result:
        print x

if __name__ == '__main__':
    main()
