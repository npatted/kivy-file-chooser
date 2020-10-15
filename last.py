import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder

import os
import csv

Builder.load_file('design2.kv')

names=[]
age=[]
class MyWidget(BoxLayout):
    def open(self, path, filename):
        global names,age
        with open(os.path.join(path, filename[0])) as f:
            csv_data = csv.reader(f)
            datalines = list(csv_data)
            names = [i[0] for i in datalines]
            age = [i[1] for i in datalines]
            print(names)
            print(age)
class MyApp(App):
    def build(self):
        return MyWidget()


if __name__ == '__main__':
    MyApp().run()