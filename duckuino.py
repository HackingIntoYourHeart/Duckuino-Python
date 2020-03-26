import os
import sys
from sys import argv

def listToString(LIST):  
	string = ""
	for part in LIST:
		string += part
	return string

os.chdir(os.path.join(sys.path[0], "output"))

if len(argv) < 2:
	print("Please specify duckyscript file as argument 1")
	exit()
else:
	duckyscript = argv[1]

output = "output.ino"

endl = "\n"

##################################
FILE1 = """#include "Keyboard.h"

void typeKey(uint8_t key)
{
  Keyboard.press(key);
  delay(50);
  Keyboard.release(key);
}

/* Init function */
void setup()
{
  // Begining the Keyboard stream
  Keyboard.begin();"""

FILE2 = """  // Ending stream
  Keyboard.end();
}

/* Unused endless loop */
void loop() {}"""
##################################
FILE = FILE1

TYPEKEY1 = "typeKey("
TYPEKEY2 = ");"

#ONLY FOR MULTIPLE COMMANDS AT ONCE
KEYPRESS1 = "Keyboard.press("
KEYPRESS2 = ");"

STRING1 = 'Keyboard.print(F("'
STRING2 = '"));'

REM1 = "//"
REM2 = ""

DELAY1 = "delay("
DELAY2 = ");"

GUI = "KEY_LEFT_GUI"
WINDOWS = GUI

APP = "229"
MENU = APP

ALT = "KEY_LEFT_ALT"

CONTROL = "KEY_LEFT_CTRL"
CTRL = CONTROL

DOWN = "KEY_DOWN_ARROW"
DOWNARROW = DOWN
UP = "KEY_UP_ARROW"
UPARROW = UP
LEFT = "KEY_LEFT_ARROW"
LEFTARROW = LEFT
RIGHT = "KEY_RIGHT_ARROW"
RIGHTARROW = RIGHT

SHIFT = "KEY_LEFT_SHIFT"

DELETE = "KEY_DELETE"

END = "KEY_END"

ESC = "KEY_ESC"
ESCAPE = ESC

PRINTSCREEN = "206"

TAB = "KEY_TAB"

SPACE = " "

ENTER = "KEY_RETURN"

REPEAT1 = "for(int i = 0; i < 10; i++){"
#Command to repeat
REPEAT2 = "}"

RELEASE = "Keyboard.releaseAll();"
#                 0        1        2       3      4        5        6        7         8         9       10       11         12        13          14         15        16      17     18       19          20         21      22       23
command_list = ["GUI", "WINDOWS", "APP", "MENU", "ALT", "CONTROL", "CTRL", "DOWN", "DOWNARROW", "UP", "UPARROW", "LEFT", "LEFTARROW", "RIGHT", "RIGHTARROW", "SHIFT", "DELETE", "END", "ESC", "ESCAPE", "PRINTSCREEN", "TAB", "SPACE", "ENTER"]

lines = []
with open(duckyscript) as readFileLines:
	for line in readFileLines:
		lines.append(line)

count = 0
for line in lines:
	count += 1
	commands = line.split()
	if commands[0]=="REM":
		FILE += endl + "  " + REM1 + listToString(" ".join(commands[1:])) + REM2 + endl
	elif line.split()[0]=="STRING":
		FILE += endl + "  " + STRING1 + listToString(" ".join(commands[1:])) + STRING2 + endl
	elif commands[0]=="DELAY":
		if len(commands) > 2:
			print("Error, line " + str(count) + "; Invalid use of \"DELAY\": Too many arguments")
			exit()
		else:
			FILE += endl + "  " + DELAY1 + listToString(commands[1]) + DELAY2 + endl
	elif commands[0] == "REPEAT":
		#TO DO
		print("Error, line " + str(count) + "; \"REPEAT\" is to be added in a later version")
		exit()
	elif commands[0] in command_list:
		if len(commands) > 1:
			for part in commands:
				if part == command_list[0]:
					RESPONSE = GUI
				elif part == command_list[1]:
					RESPONSE = WINDOWS
				elif part == command_list[2]:
					RESPONSE = APP
				elif part == command_list[3]:
					RESPONSE = MENU
				elif part == command_list[4]:
					RESPONSE = ALT
				elif part == command_list[5]:
					RESPONSE = CONTROL
				elif part == command_list[6]:
					RESPONSE = CTRL
				elif part == command_list[7]:
					RESPONSE = DOWN
				elif part == command_list[8]:
					RESPONSE = DOWNARROW
				elif part == command_list[9]:
					RESPONSE = UP
				elif part == command_list[10]:
					RESPONSE = UPARROW
				elif part == command_list[11]:
					RESPONSE = LEFT
				elif part == command_list[12]:
					RESPONSE = LEFTARROW
				elif part == command_list[13]:
					RESPONSE = RIGHT
				elif part == command_list[14]:
					RESPONSE = RIGHTARROW
				elif part == command_list[15]:
					RESPONSE = SHIFT
				elif part == command_list[16]:
					RESPONSE = DELETE
				elif part == command_list[17]:
					RESPONSE = END
				elif part == command_list[18]:
					RESPONSE = ESC
				elif part == command_list[19]:
					RESPONSE = ESCAPE
				elif part == command_list[20]:
					RESPONSE = PRINTSCREEN
				elif part == command_list[21]:
					RESPONSE = TAB
				elif part == command_list[22]:
					RESPONSE = SPACE
				elif part == command_list[23]:
					RESPONSE = ENTER
				elif len(part) == 1:
					RESPONSE = "'" + part + "'"
				else:
					print("Error, line " + str(count) + "; unknown argument: \"" + part + "\"")
					exit()
				FILE += endl + "  " + KEYPRESS1 + RESPONSE + KEYPRESS2 + endl
			FILE += endl + "  " + RELEASE + endl
		else:
			if listToString(commands[0]) == command_list[0]:
				RESPONSE = GUI
			elif listToString(commands[0]) == command_list[1]:
				RESPONSE = WINDOWS
			elif listToString(commands[0]) == command_list[2]:
				RESPONSE = APP
			elif listToString(commands[0]) == command_list[3]:
				RESPONSE = MENU
			elif listToString(commands[0]) == command_list[4]:
				RESPONSE = ALT
			elif listToString(commands[0]) == command_list[5]:
				RESPONSE = CONTROL
			elif listToString(commands[0]) == command_list[6]:
				RESPONSE = CTRL
			elif listToString(commands[0]) == command_list[7]:
				RESPONSE = DOWN
			elif listToString(commands[0]) == command_list[8]:
				RESPONSE = DOWNARROW
			elif listToString(commands[0]) == command_list[9]:
				RESPONSE = UP
			elif listToString(commands[0]) == command_list[10]:
				RESPONSE = UPARROW
			elif listToString(commands[0]) == command_list[11]:
				RESPONSE = LEFT
			elif listToString(commands[0]) == command_list[12]:
				RESPONSE = LEFTARROW
			elif listToString(commands[0]) == command_list[13]:
				RESPONSE = RIGHT
			elif listToString(commands[0]) == command_list[14]:
				RESPONSE = RIGHTARROW
			elif listToString(commands[0]) == command_list[15]:
				RESPONSE = SHIFT
			elif listToString(commands[0]) == command_list[16]:
				RESPONSE = DELETE
			elif listToString(commands[0]) == command_list[17]:
				RESPONSE = END
			elif listToString(commands[0]) == command_list[18]:
				RESPONSE = ESC
			elif listToString(commands[0]) == command_list[19]:
				RESPONSE = ESCAPE
			elif listToString(commands[0]) == command_list[20]:
				RESPONSE = PRINTSCREEN
			elif listToString(commands[0]) == command_list[21]:
				RESPONSE = TAB
			elif listToString(commands[0]) == command_list[22]:
				RESPONSE = SPACE
			elif listToString(commands[0]) == command_list[23]:
				RESPONSE = ENTER
			elif len(listToString(commands[0])) == 1:
				RESPONSE = '"' + listToString(commands[0]) + '"'
			else:
				print("Error: Unknown")
				exit()
			FILE += endl + "  " + TYPEKEY1 + RESPONSE + TYPEKEY2 + endl
	else:
		print("Error, line " + str(count) + "; unknown command: \"" + commands[0] + "\"")
		exit()
		
FILE += FILE2
output = open(output, 'w')
output.write(FILE)
exit()
