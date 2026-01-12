import pandas as pd

def main():
    print("+----------------------------------------------+")
    print("                    Players Data                ")
    print("+----------------------------------------------+")
    user_input = int(input("Enter one of the following options\n"
                           "1. top 100 players\n"
                           "2. top 10 players\n"
                           "3. player_nation\n"))
    if user_input == 1:
        top_100_players(data)
    elif user_input == 2:
        top_10_players(data)
    elif user_input == 3:
        player_nation(data)

def load_csv():
    df = pd.read_csv('players_data-2024_2025.csv')
    return df

data = load_csv()

def top_100_players(data):
    print(data.iloc[:100,:5])

def top_10_players(data):
    print(data.iloc[:10,:5])

def player_nation(data):
    print(data.iloc[:100,1:3])


if __name__ == '__main__':
    main()