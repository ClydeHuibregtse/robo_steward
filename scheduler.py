

class Brother(object):
    def __init__(self, name, year, pledge_num, conflicts):
        self.name = name
        self.year = year
        self.rank = pledge_num
        self.conflicts = conflicts

        self.num_complete = 0
        self.alternating = 0


    def compute_peking_metric(self):
        metric = self.rank * 10 + self.num_complete * 5 + 1e15 * self.alternating
        return metric

    def __lt__(self, other):
        my_order, other_order = self.compute_peking_metric(), other.compute_peking_metric()

        return my_order < other_order


    def add_conflict(self, conflict):
        self.conflicts.add(conflict)

    def remove_conflict(self, conflict):
        self.conflicts.remove(conflict)



class Scheduler(object):
    def __init__(self, brothers):

        self.brothers = brothers


    def make_weekly_schedule(self):

        slots = {"M":{"Waitings": [], "Midnights": []},
                 "T":{"Waitings": [], "Midnights": []},
                 "W":{"Waitings": [], "Midnights": []},
                 "R":{"Waitings": [], "Midnights": []},
                 "F":{"Waitings": [], "Midnights": []},
                 "S":{"Waitings": [], "Midnights": []},
                 }




if __name__ == "__main__":
    Clyde = Brother("Clyde Huibregtse", 4, 4, {"M+","W-"})
    Evan = Brother("Evan Kim", 3, 2, {})

    print(Clyde > Evan)
