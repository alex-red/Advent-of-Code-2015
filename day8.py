import sys
import re
import fileinput

def main():

  output = 0
  for line in fileinput.input():
      line = line.strip()
      output += len(line)
      output -= len(eval(line)) 

  print ("Part 1:", output)

  output = 0
  for line in fileinput.input():
      line = line.strip()
      output -= len(line)
      output += len(re.escape(line)) + 2 

  print ("Part 2:", output)

  
if __name__ == '__main__':
  # Usage: python day8.py day8_input.txt
  main()
