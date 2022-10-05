# Write your code here.
def get_number_of_teams():
    num_teams = 0
    while num_teams < 2:
        num_teams = int(input("Enter the number of teams in the tournament:"))
        if num_teams < 2:
            print("The minimum number of teams is 2, try again.")
        elif num_teams >= 2:
            print(f"The number of teams in this tournament is {num_teams}")
    return num_teams


def get_team_names(num_teams):
    team_names = []
    for num_teams in range(num_teams + 1):
        while num_teams:
            team_names1 = input(
                f"Enter the name for team #{num_teams}: ")
            if len(team_names1) < 2:
                print("Team names must have at least 2 characters, try again")

            if len(team_names1) > 2:
                print("Team names must have at most 2 words, try again")
            else:
                team_names1 = team_names.append(team_names1)


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
