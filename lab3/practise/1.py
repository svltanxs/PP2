class myclass:
    def getString(self):
        self.text = input()
    def upperString(self):
        print(self.text.upper())
p1 = myclass()
p1.getString()
p1.upperString()
