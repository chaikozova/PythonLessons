def on_going_decorator(function):
    def on_going_wrapper():
        result = function()
        return f"result {result}"

    return on_going_wrapper()


@on_going_decorator
def going():
    return 2+2


class Anime:

    def __init__(self, name):
        self.name = name

    @on_going_decorator
    def on_going(self):
        if self.name:
            return True
        else:
            return False

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if type(value) != str:
            raise ValueError("Wrong name type!!!")
        self._name = value



anime = Anime()
anime.name = "1234"
print(anime.name)
