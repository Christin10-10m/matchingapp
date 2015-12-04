import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Color
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import StringProperty, ObjectProperty,NumericProperty,ListProperty
from kivy.uix.image import Image
from kivy.uix.button import Button
from functools import partial

class Tile(ToggleButton):
     # A tile on the game grid will have the following attributes:

     #    Attributes:
     #       Kind: Species of the animal depicted in the tile
     #       name: name of the animal, denotes whether it's an adult or a baby. 
     #        url: image url for the tile

  def __init__(self,kind, name, imageurl):
    self.kind = kind
    self.name = name
    self.imageurl = imageurl

walrus = Tile("walrus", "walrus", "images/walrus.png")
babywalrus = Tile("walrus", "baby walrus", "images/babywalrus.png")
tiger = Tile("tiger", "tiger", "images/tiger.png")
babytiger = Tile("tiger", "baby tiger", "images/babytiger.png")
narwhal = Tile("narwhal", "narwhal", "images/narwhal.png")
babynarwhal = Tile("narwhal", "baby narwhal", "images/babynarwhal.png")
orangutan = Tile("orangutan", "orangutan", "images/orangutan.png")
babyorangutan = Tile("orangutan", "baby orangutan", "images/babyorangutan.png")
robin = Tile("robin", "robin", "images/robin.png")
babyrobin = Tile("robin", "baby robin", "images/babyrobin.png")
dog = Tile("dog", "dog", "images/dog.png")
babydog = Tile("dog", "baby dog", "images/babydog.png")
iguana = Tile("iguana", "iguana", "images/iguana.png")
babyiguana = Tile("iguana", "baby iguana", "images/babyiguana.png")
cow = Tile("cow", "cow", "images/cow.png")
babycow = Tile("cow", "baby cow", "images/babycow.png")

cards = [
    walrus,
    babywalrus, 
    tiger,
    babytiger,
    narwhal,
    babynarwhal,
    orangutan,
    babyorangutan,
    robin,
    babyrobin,
    dog,
    babydog,
    iguana,
    babyiguana,
    cow,
    babycow
    ]

class MatchingGame(Widget):
    grid = random.sample(cards, len(cards))
    characters = range (1, len(grid) + 1)
    matched = []
    selected = []
    
# Function to pass back info about the clicks
    def passed_back(self, arg):
        clickedOn = MatchingGame.grid[arg - 1]
        if clickedOn not in MatchingGame.matched:
            print "clicked on = %s" % clickedOn.name
        if MatchingGame.selected and MatchingGame.selected[0].kind == clickedOn.kind:   
            print "MATCH!"
            MatchingGame.matched.append(MatchingGame.selected) # how do you add both? 
            MatchingGame.selected = []
            print "Matched:" 
            print MatchingGame.matched # how to get it to print list attributes? 
        elif MatchingGame.selected and MatchingGame.selected[0].kind != clickedOn.kind:
            print "NO MATCH!"
            MatchingGame.selected = []
        else:
            MatchingGame.selected.append(clickedOn) 
            print "Selected:"
            print MatchingGame.selected[0].kind

class MatchingApp(App):
    def build(self):
        return MatchingGame()


if __name__ == '__main__':
    MatchingApp().run()