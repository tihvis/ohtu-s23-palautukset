import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search(self):
        #testaa olemassaolevan pelaajan hakua
        player = self.stats.search("Gretzky")
        self.assertEqual("Gretzky", player.name)

        #testaa puuttuvan pelaajan hakua
        player = self.stats.search("Litmanen")
        self.assertIsNone(player)

    def test_players_of_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(3, len(players))

    def test_top_players(self):
        top_players = self.stats.top(4)
        self.assertEqual(4, len(top_players))
        self.assertEqual("Gretzky", top_players[0].name)
        self.assertEqual("Lemieux", top_players[1].name)
        self.assertEqual("Yzerman", top_players[2].name)
        self.assertEqual("Kurri", top_players[3].name)

        top_players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual("Lemieux", top_players[0].name)
        self.assertEqual("Yzerman", top_players[1].name)
        self.assertEqual("Kurri", top_players[2].name)

        top_players = self.stats.top(3, SortBy.ASSISTS)
        self.asserEqual("Gretzky", top_players[0].name)
        self.assertEqual("Yzerman", top_players[1].name)
        self.assertEqual("Lemieux", top_players[2].name)

