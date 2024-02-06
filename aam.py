class SimpleLP:
    def __init__(self, s1, s2):
        self.c1 = float(s1)
        self.c2 = float(s2)
        self.k = s1 * s2

    def __str__(self):
        return f"{self.c1}, {self.c2}"

    def transact(self, c, amt):
        if c == 1:
            if amt >= self.c1:
                return -1
            
            price = self.calculatePrice(c, amt)
            self.c1 += amt
            self.c2 -= price
    
        if c == 2:
            if amt >= self.c2:
                return -1
            
            price = self.calculatePrice(c, amt)
            self.c2 += amt
            self.c1 -= price
    
    def amtc1(self):
        return self.c1
    
    def amtc2(self):
        return self.c2

    def checkPrice(self, c):
        return self.calculatePrice(c, 1)

    def calculatePrice(self, c, amt):
        if c == 1:
            return self.c2 - self.k / (self.c1 + amt)
        elif c == 2:
            return self.c1 - self.k / (self.c2 + amt)
        return -1