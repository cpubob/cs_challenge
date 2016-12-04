from challenge import Challenge

class ChallengeOne(Challenge):
    def __init__(self):
        self.name = "Challenge 1"
        description = "Given two numbers, a and b, return the product."
        base = "def g(a, b):\n  #TODO: Your code goes here.\n  #return something\n"
        tests = """[
            [[1,2], 2],
            [[2,2], 4],
            [[3,3], 9],
        ]"""
        testing = "for t in %s:\n\tprint g(t[0][0], t[0][1]) == t[1]" % tests
        Challenge.__init__(self, description, base, tests, testing)
