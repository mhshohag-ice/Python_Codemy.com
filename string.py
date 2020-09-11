# Clear the terminal screen
import os
os.system('clear')




def Greeting():
	greetings = "Hello!, "
	name = "Shohag."
	return greetings + name


greet = Greeting()

print(greet)