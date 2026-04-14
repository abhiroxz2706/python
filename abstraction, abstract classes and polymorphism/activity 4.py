class India:
    def capital(self):
        print("New Delhi is the capital of India")
    def language(self):
        print("Hindi is most widely spoken language in India")

class USA:
    def capital(self):
        print("Washington D.C is the capital of USA")
    def language(self):
        print("English is the primary language in USA")

objind=India()
objusa=USA()

for i in (objind,objusa):
    i.capital()
    i.language()

