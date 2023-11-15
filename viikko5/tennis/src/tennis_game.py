class TennisGame:

    scores = ["Love", "Fifteen", "Thirty", "Forty"]

    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.current = [0, 0]

    def won_point(self, player_name):
        player_index = 0 if player_name == self.player1_name else 1
        self.current[player_index] += 1

    def get_score(self):
        score = ""
        if self.current[0] == self.current[1]:
            return self.equal() if max(self.current) < 3 else "Deuce"
        elif max(self.current) >= 4:
            return self.get_advantage_or_win()
        else:
            for i in range(2):
                if i > 0:
                    score += "-"
                score += self.scores[self.current[i]]
            return score

    def equal(self):
        return f"{self.scores[self.current[0]]}-All"


    def get_advantage_or_win(self):
        difference = self.current[0] - self.current[1]
        if abs(difference) == 1:
            leader_name = self.player1_name if difference == 1 else self.player2_name
            return f"Advantage {leader_name}"
        else:
            leader_name = self.player1_name if difference >= 2 else self.player2_name
            return f"Win for {leader_name}"
