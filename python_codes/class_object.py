class Human:
    def __init__(self, n, g):
        self.name = n
        self.gender = g

    def works_at(self):
        if self.name == "Hasan":
            print(self.name, "works at ostad")
        elif self.name == "Sayem":
            print(self.name, "works at remote job")

    @staticmethod
    def speaks():
        print("Speaks in Bangla")


human_1 = Human("Hasan", "Male")
human_2 = Human("Sayem", "Male")

human_1.works_at()
human_2.works_at()

human_1.speaks()
human_2.speaks()

print(human_1.name, human_2.name)
