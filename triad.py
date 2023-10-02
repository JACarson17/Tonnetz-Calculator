from note import Note
from constants import name_to_value, value_to_name
class Triad():
    def __init__(self, root, major = True) -> None:
        self.root = Note(root)
        self.major = major
        self.name = self.root.name + ' major' if major else self.root.name + ' minor'

        third_val = self.root.value + 4 if major else self.root.value + 3
        while third_val > 11:
            third_val -= 12
        self.third = Note(value_to_name[third_val])
        
        fifth_val = self.root.value + 7
        while fifth_val > 11:
            fifth_val -= 12
        self.fifth = Note(value_to_name[fifth_val])

    def p_transform(self):
        if self.major:
            transform = Triad(self.root.name, False)
        else:
            transform = Triad(self.root.name, True)
        return transform

    def l_transform(self):
        if self.major:
            transform = Triad(self.third.name, False)
        else:
            temp = self.fifth.value
            temp += 1
            if temp > 11:
                temp -= 12
            transform = Triad(value_to_name[temp], True)
        return transform

    def r_transform(self):
        if self.major:
            temp = self.fifth.value
            temp += 2
            if temp > 11:
                temp -= 12
            transform = Triad(value_to_name[temp], False)
        else:
            transform = Triad(self.third.name, True)
        return transform