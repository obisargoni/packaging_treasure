from argparse import ArgumentParser
from .hunt import * # Note python 3 relative import

def process():
   parser = ArgumentParser(description = "Generate a Dumb Hunting for the Wumbus
   and print the success fraction.")

   parser.add_argument('dungeon')

   arguments= parser.parse_args()

   print(success_chance(arguments.dungeon))

if __name__ == "__main__":
    process()
