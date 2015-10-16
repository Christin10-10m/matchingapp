import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.graphics import Color
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
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
     #       name: name of the animal, deontes whether it's an adult or a baby. 
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
    first = "Why does this string work?"
    grid = random.sample(cards, len(cards))
    characters = range (1, len(grid) + 1)
# Function to pass back info about the clicks
    def passed_back(self, arg):
        if self.first:
            self.first = arg
        print "first: %s" % self.first
        print "hooray!!"
        print "%s" % arg

    def play():
        matched = []
        while True:
            # if x in matched:...maybe?
            #     toggle the tile open and make it unclickable
            if len(matched) == len(grid):
                print "You have matched all the animals!"
                break
        while True:
            i = "passed_back(self, arg) #this might not work. self.passed_back()"
            if i not in matched:
                print "You picked %s" %grid[i-1].name
                break
        while True: 
            k = "passed_back(self, arg)"
            if k not in matched:
                print "You picked %s" %grid[k-1].name
                break

        if k != i and grid[i-1].kind == grid[k-1].kind:
            matched.append(k)
            matched.append(i)
            print "it's a match!"

    # while True:
    #     play()
    #     # # interstitial loads with two buttons, "Want to play again? (y/n)"
    #     # y = "yes button pressed"
    #     # if y != "y":
    #     #     break
    #     pass

class MatchingApp(App):
    def build(self):
        return MatchingGame()


if __name__ == '__main__':
    MatchingApp().run()