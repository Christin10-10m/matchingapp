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
     # A tile on the game grid will have the folloing attributes:

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
    first = 0
    grid = random.sample(cards, len(cards))
    characters = range (1, len(grid) + 1)
    matched = []
    
# Function to pass back info about the clicks
    def passed_back(self, arg):
        if MatchingGame.first not in MatchingGame.matched:
            MatchingGame.first = arg
            print "first: %s" % MatchingGame.first
            print "You picked %s" %(MatchingGame.grid[MatchingGame.first-1].name)
        # ok, now, if they click again and it's the same 'kind' tell that it's a match
        # if arg == MatchingGame.first: 
        #     MatchingGame.first == None
        #     # Then if kind == kind... print, it's a match!
        #     print MatchingGame.first


        # Now, add the two matched tiles to the "self.matched" list, and make them untoggalable. 
            print MatchingGame.matched

class MatchingApp(App):
    def build(self):
        return MatchingGame()


if __name__ == '__main__':
    MatchingApp().run()