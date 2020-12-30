'''
WORKOUT STATISTICS TRACKER
---------------------------------------------------------------------
AUTHOR : Jack Rutland

Description : A windows application written in python to log and
display information about your workouts.

'''
#IMPORTS
from os import listdir
from os import getcwd
from os.path import splitext
import kivy

from workout import Lift
from workout import Workout

import pickle

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file('workoutstats.kv')

'''
This is how pickle works
lift1 = Lift('bench',3,10)
workout1 = Workout('pushing')

workout1.addLift(lift1)

print(workout1)

pickle_out = open('lift.workout','wb')
pickle.dump(workout1, pickle_out)
pickle_out.close()

pickle_in = open('lift.workout','rb')
workout2 = pickle.load(pickle_in)

print(workout2)

'''
class WorkoutStats(TabbedPanel):

    PATH = getcwd()

    #Returns the stems of files in the root/workouts directory as a list
    def fetch_workout_list(self) :
        return [splitext(f)[0] for f in listdir(self.PATH + r'/workouts')]

    #Reads the workout file and update the information in the workout editor
    def read_workout_file(self, text) :
        pickle_in = open (text + '.workout' , 'rb')
        workout = pickle.load(pickle_in)

    

class WSApp(App):
    def build(self):
        self.title = 'Workout Stats BETA'
        self.icon = 'assets/ws_icon.png'
        return WorkoutStats()


if __name__ == '__main__':
    WSApp().run()