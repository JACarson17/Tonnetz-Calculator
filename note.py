from constants import name_to_value, value_to_name
class Note():
    def __init__(self, name:str) -> None:
        self.name = name
        self.value = name_to_value[name]

    def update(self, delta:int):
        self.value += delta
        while self.value > 11:
            self.value -= 12
        while self.value < 0:
            self.value += 12

        self.name = value_to_name[self.value]
        return self

    # def __repr__(self) -> str:
        # self.name