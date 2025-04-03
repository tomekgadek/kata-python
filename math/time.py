"""
    time.py: implementacja klasy Time.
"""

class Time:
    def __init__(self, s = 0):
        self.s = s
        
    def __str__(self):
        seconds_in_hours = 3600
        seconds_in_minutes = 60

        h = self.s // seconds_in_hours
        m = (self.s - h * seconds_in_hours ) // seconds_in_minutes
        s = self.s - h * seconds_in_hours - m * seconds_in_minutes

        return f"{h:02d}:{m:02d}:{s:02d}"

    def __repr__(self):
        return f"Time({self.s})"

    def __add__(self, other):
        return self.s + other.s


if __name__ == "__main__":
    t1 = Time(120)
    t2 = Time(89)

    assert t1 + t2 == 209
    assert f"{t2}" == "00:01:29"
    assert repr(t1) == "Time(120)"
