import argparse
from sense_hat import SenseHat
from random import randint


def show_text(text='hello'):
  sense = SenseHat()
  sense.set_rotation(180)

  sense.show_message(text, text_colour=(randint(1, 255), randint(1, 255), randint(1, 255)))



if __name__=='__main__':
  parser = argparse.ArgumentParser(description='print to SenseHat')
  parser.add_argument("text", help="Prints the supplied argument.")
  args = parser.parse_args()
  print(args.text)
  show_text(args.text)

