# Write your code here.
def get_number_of_teams():
    while True:
        num_teams = int(input("Enter the number of teams in the tournament:"))
        if num_teams >= 2:
            break

        print("The minimum number of teams is 2, try again")
    return num_teams


def get_team_names(num_teams):
    team_names = []
    for teamNumber in range(num_teams):
        while True:
            team_names1 = input(f"Enter the name for team #{teamNumber + 1}: ")
            num_words = len(team_names1.split(" "))
            if num_words > 2:
                print("Team names must have at most 2 words, try again")
            elif len(team_names1) < 2:
                print("Team names must have at least 2 characters, try again")
            else:
                break
        team_names.append(team_names1)
    return team_names


def get_number_of_games_played(num_teams):
    pass

def get_team_wins(team_names, games_played):
    pass


# It is not necessary to use the functions defined above. There are simply here
# to help give your code some structure and provide a starting point.
num_teams = get_number_of_teams()
team_names = get_team_names(num_teams)
# games_played = get_number_of_games_played(num_teams)
# team_wins = get_team_wins(team_names, games_played)

print("Generating the games to be played in the first round of the tournament...")
