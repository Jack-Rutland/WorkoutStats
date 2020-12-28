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
import pickle
import kivy

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.tabbedpanel import TabbedPanel

Builder.load_file('workoutstats.kv')
 
class WorkoutStats(TabbedPanel):

    PATH = getcwd()

    #Returns the stems of files in the root/workouts directory as a list
    def fetch_workout_list(self) :
        return [splitext(f)[0] for f in listdir(self.PATH + r'/workouts')]

    #Reads the workout file and update the information in the workout editor
    def read_workout_file(self, text) :
        print(text)

    

class WSApp(App):
    def build(self):
        self.title = 'Workout Stats BETA'
        self.icon = 'assets/ws_icon.png'
        return WorkoutStats()


if __name__ == '__main__':
    WSApp().run()