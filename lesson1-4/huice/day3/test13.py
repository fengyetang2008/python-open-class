class Student(object):


    # def get_score(self):
    #     return self._score

    @property
    def score(self):
        return self._score

    # def set_score(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('score must be an integer!')
    #     if value < 0 or value > 100:
    #         raise ValueError('score must between 0 ~ 100!')
    #     self._score = value

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value


# std = Student()
# std.set_score(100)
# print std.get_score()

std2 = Student()
std2.score = 90
print(std2.score)
