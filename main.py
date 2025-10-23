class Player:
    def __init__(self, player_name, player_age):
        self.player_name = player_name
        self.player_age = player_age

class Teams:
    
    # Властивості класу
    league_name = "Series A"
    league_country = "Italy"
    league_level = 1
    
    
    def __init__(self, team_id, team_name, points, wins, losses, draws, goal_difference): #Конструктор класу
        self.team_id = team_id
        self.team_name = team_name
        self.__points = points # Приватний атрибут
        self.wins = wins
        self.losses = losses
        self.draws = draws
        self.goal_difference = goal_difference
    
    @staticmethod # Статичний метод
    def calculate_goal_difference(goals_scored, goals_conceded):
        return goals_scored - goals_conceded
    
    def get_points(self):
        return self.__points
    
    @staticmethod # Статичний метод
    def set_points(wins, draws):
        return wins * 3 + draws
    
    def show_summary(self):
        return f"{self.team_name}: {self.__points} points, W:{self.wins}, D:{self.draws}, L:{self.losses}"

    def add_match_result(self, goals_for, goals_against):
        self.goal_difference += Teams.calculate_goal_difference(goals_for, goals_against)
        if goals_for > goals_against:
            self.wins += 1
            self.__points += 3
        elif goals_for == goals_against:
            self.draws += 1
            self.__points += 1
        else:
            self.losses += 1
    
class YoungTeams(Teams, Player): #Множинне наслідування
    
    def __init__(self, team_id, team_name, points, wins, losses, draws, goal_difference, max_age, player_name, player_age): #Конструктор класу
        Teams.__init__(team_id, team_name, points, wins, losses, draws, goal_difference)
        Player.__init__(self, player_name, player_age)
        self.max_age = max_age
        self.__roster = []
    
    def is_eligible(self, player_age):
        return player_age <= self.max_age
    
    def add_player(self, player_name, player_age):
        if self.is_eligible(player_age):
            self.__roster.append((player_name, player_age))
            return f"Player {player_name} added to the roster."
        else:
            return f"Player {player_name} is not eligible for this team."
        
class WomenTeams(Teams):
    
    def __init__(self, team_id, team_name, points, wins, losses, draws, goal_difference, league_level): #Конструктор класу
        super().__init__(team_id, team_name, points, wins, losses, draws, goal_difference)
        self.league_level = league_level
        self.__roster = []
        
    def add_women_player(self, player_name):
        self.__roster.append(player_name)
        return f"Player {player_name} added to the roster."
    
    def get_captain(self):
        if self.__roster:
            return self.__roster[0]
        else:
            return "No players in the roster."
        
# Створення об'єктів класів

player1 = Player("Tom", 17)
player2 = Player("Bob", 19)
player3 = Player("Clara", 25)
player4 = Player("Diana", 21)

arsenal_team = Teams(1, "Arsenal", 60, 15, 5, 5, 25)
mu_team = Teams(2, "Manchester United", 45, 13, 7, 4, 20)
liverpool_team = Teams(3, "Liverpool", 48, 14, 6, 4, 22)
mc_team = Teams(4, "Manchester City", 52, 16, 4, 4, 30)

youth_team = YoungTeams(1, "Arsenal Academy", 30, 9, 3, 3, 15, 23)
women_team = WomenTeams(1, "Arsenal Women", 40, 12, 4, 4, 20, 1)

# Приклад поліморфізму

youth_team.add_player(player1.player_name, player1.player_age)
youth_team.add_player(player2.player_name, player2.player_age)

women_team.add_women_player(player3.player_name)
women_team.add_women_player(player4.player_name)

# Використання базових класів та методів

arsenal_team.add_match_result(3, 1)
print(arsenal_team.show_summary())

