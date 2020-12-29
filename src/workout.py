class Lift :

    def __init__(self,name='UNNAMED',sets=3,reps=8) :
        self.name = name
        self.sets = sets
        self.reps = reps

    def __str__(self) :
        return self.name


class Workout :

    def __init__(self,name="UNNAMED") :
        self.name = name
        self.lift_list = []

    def addLift(self, lift) :
        self.lift_list += lift
    
    def removeLift(self, lift) :