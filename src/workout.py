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

    def __str__(self) :
        return_string = self.name + " : \n"
        for l in self.lift_list :
            return_string += "\t{0}\n\t\tsets:{1}\n\t\treps:{2}\n".format(l.name, l.sets, l.reps)
        return return_string

    def addLift(self, lift) :
        self.lift_list.append(lift)

    def removeLift(self, lift) :
        self.lift_list.remove(lift)