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
from kivy.uix.scatter import Scatter

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
    grid = random.sample(cards, len(cards))
    characters = range (1, len(grid) + 1)
    def play():
        matched = []
        while True:
            print_grid(grid, matched)
            if len(matched) == len(grid):
                print "You have matched all the animals!"
                break

            while True:
                i = int(raw_input("choose a numbered tile!"))
                if i not in matched:
                    print "You picked %s" %grid[i-1].name
                    break
                else:
                    print "This number in unavailable, pick again."
                        
            while True: 
                k = int(raw_input("choose another numbered tile!"))
                if k == i:
                    print "Sorry, you cannot guess the same tile twice."
                if k not in matched:
                    print "You picked %s" %grid[k-1].name
                    break
                else:
                    print "This number in unavailable, pick again."

            if k != i and grid[i-1].kind == grid[k-1].kind:
                matched.append(k)
                matched.append(i)
                print "it's a match!"
            else:
                if grid[i-1].kind != grid[k-1].kind:
                    print "Sorry, these tiles aren't a match"


class MatchingApp(App):
    def build(self):
        return MatchingGame()


if __name__ == '__main__':
    MatchingApp().run()