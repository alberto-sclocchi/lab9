from dragon import Dragon
from cow import Cow

class IceDragon(Dragon):
    def __init__(self, name, image):
        super().__init__(name, image)

    @staticmethod
    def can_breath_fire():
        return False


