class Player:
    def __init__(self, dict):
        self.name = dict['name']
        self.nationality = dict['nationality']
        self.team = dict['team']
        self.goals = dict['goals']
        self.assists = dict['assists']
        self.total = self.goals + self.assists

    def __str__(self):
        return (f"{self.name:20}{self.team:6}{self.goals:3} + {self.assists:1} = {self.total:1}")