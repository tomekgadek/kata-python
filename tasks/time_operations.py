"""
    Klasa 'Time'. Operacje zwiazane z czasem.

    h: godzina
    m: minuta
    s: sekunda
"""

class Time:
    def __init__(self, h=0, m=0, s=0):
        self.h = h
        self.m = m
        self.s = s
    
    def __str__(self):
        return "{}:{}:{}".format(self.h, self.m, self.s)
    
    def __add__(self, other):
        time = Time(self.h, self.m, self.s)
        time.increment(other.time2sec())

        return time
    
    def __cmp__(self, other):
        return self.time2sec() - other.time2sec()
    
    def increment(self, sec):
        self.s += sec
        
        while self.s >= 60:
            self.s -= 60
            self.m += 1
            
            if(self.m == 60):
                self.h += 1
                self.m = 0
            
            if self.h == 24:
                self.h = 0
    
    def time2sec(self):
        minutes = self.h * 60 + self.m
        seconds = minutes * 60 + self.s
        return seconds

time = Time(9, 0, 1)
assert str(time) == "9:0:1"
assert time.time2sec() == (9 * 3600 + 1)

time.increment(60)
assert str(time) == "9:1:1"
assert time.time2sec() == (9 * 3600 + 61)

time.increment(3600)
assert str(time) == "10:1:1"
assert time.time2sec() == (10 * 3600 + 61)

time.increment(3600 * 9)
assert str(time) == "19:1:1"
assert time.time2sec() == (19 * 3600 + 61)

time.increment(3600 * 5 - 61)
assert str(time) == "0:0:0"
assert time.time2sec() == 0

t1 = Time(1, 0, 1)
t2 = Time(0, 1, 0)

t3 = t1 + t2
assert str(t3) == "1:1:1"
assert not(t1 == t2)
assert t1 == t1
