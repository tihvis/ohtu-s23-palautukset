from matchers import And, PlaysIn, HasAtLeast, All, Not, HasFewerThan, Or

class QueryBuilder:
    def __init__(self, matcher = None):
        self._matcher = matcher or All()

    def build(self):
        return self._matcher

    def playsIn(self, team):
        return QueryBuilder(And(PlaysIn(team), self._matcher))
    
    def hasAtLeast(self, value, attr):
        return QueryBuilder(And(HasAtLeast(value, attr), self._matcher))

    def hasFewerThan(self, value, attr):
        return QueryBuilder(And(HasFewerThan(value, attr), self._matcher))
