"""
Python Web Development Techdegree
Project 2 - Build a Soccer League
--------------------------------
"""

# Coding style complies with PEP 8.

import csv
import os


def remove_team_file():
    """Removes "teams.txt" if it exists"""
    if os.path.exists("teams.txt"):
        os.remove("teams.txt")


def divide_into_3teams(copy, d, s, r):
    """
    Divides the list containing 9 players based on their experience
    into 3 teams such that each team has equal number
    of players according to their experience.Each team must
    have 3 experience and  3 no experience players
    """
    count_of_d = 0
    count_of_s = 0
    count_of_r = 0
    while len(copy):
        for item in copy:
            if count_of_d <= 2:
                d.append(item)
                copy.remove(item)
                count_of_d += 1
            elif count_of_s <= 2:
                s.append(item)
                copy.remove(item)
                count_of_s += 1
            else:
                r.append(item)
                copy.remove(item)
                count_of_r += 1


def get_player_details(group):
    """ Appends Player details like Name,Experience and Guardian into a List.
    And writes the details into a file 'teams.txt'
    """
    for team_details in group[1:]:
        new_list = []
        player_name = team_details["Name"]
        experience = team_details["Soccer Experience"]
        guardian_name = team_details["Guardian Name(s)"]
        new_list.append(player_name)
        new_list.append(experience)
        new_list.append(guardian_name)
        with open('teams.txt', 'a') as file:
            file.write('{}\n'.format(', '.join(new_list)))


def invitation(group):
    """Create 18 text files with a personalised invitation to the
    guardian with the playername and their team"""
    team = group[0].values()
    team = str(team)  # Converts value a dictionary object into string
    team = team.replace("dict_values(['", "")
    team = team.replace("'])", "")
    for item in group[1:]:  # Iterates from index 1 since index 0 is Team
        full_name = item["Name"]
        guardian = item["Guardian Name(s)"]
        time = "9:00"
        date = "01/10/2018"
        invite = """
        Dear {},\n
        Welcome {} as a member of the {} soccer team.\n
        Our first practice will be held at the Vihar Grounds at {} on {}.\n
        Thank you,\n
        Arjun
        (Team Coach)""".format(guardian, full_name, team, time, date)
        name_spilt = full_name.split()
        with open("text_files/{}_{}.txt".format(
                  name_spilt[0].lower(), name_spilt[1].lower()), 'w') as files:
            files.write('{}'.format(invite))


def start_building_teams():
    """

    Reads the CSV and Divides the CSV into two Lists
    acording to their Experience.Calls the function
    divide_into_3teams().Calls get_player_details()
    and invitation()

    """
    experience = []
    no_experience = []
    # Add Team name into the 3 teams
    Dragon = [{'Team': 'Dragon'}]
    Sharks = [{'Team': 'Sharks'}]
    Raptors = [{'Team': 'Raptors'}]
    with open('soccer_players.csv') as csvfile:
        player_reader = csv.DictReader(csvfile, delimiter=',')
        for row in player_reader:
            if row["Soccer Experience"] == "YES":
                del row["Height (inches)"]  # Removes the key Height
                experience.append(row)
            elif row["Soccer Experience"] == "NO":
                del row["Height (inches)"]
                no_experience.append(row)
    experience_copy = experience[:]  # Creates a copy of experience list
    # Creates a copy of no_experience list
    no_experience_copy = no_experience[:]
    divide_into_3teams(experience_copy, Sharks, Dragon, Raptors)
    divide_into_3teams(no_experience_copy, Sharks, Dragon, Raptors)
    with open('teams.txt', 'a') as file:
        file.write('Sharks\n')
    get_player_details(Sharks)
    with open('teams.txt', 'a') as filedragon:
        filedragon.write('\nDragons\n')
    get_player_details(Dragon)
    with open('teams.txt', 'a') as fileraptor:
        fileraptor.write('\nRaptors\n')
    get_player_details(Raptors)
    print("""\nOpen teams.txt file to see the players
and there assigned team\n""")

    invitation(Sharks)
    invitation(Dragon)
    invitation(Raptors)
    print("""Open the folder 'text_files'to see 18 text files
with a personalised messsages to the Team Members\n""")


if __name__ == '__main__':
    remove_team_file()
    start_building_teams()
