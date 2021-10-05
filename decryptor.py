# decrypts stuff in one nice class package
import time # timing




class Decryptor():
    topwords = []
    code = ""
    commands = ("h", "decrypt", "ciphercheck")

    def __init__(self, code):
        x = time.time()
        print("initialising...")
        self.code = code
        print("reading commonwords")
        with open("commonwords","r") as f:
            for line in f.readlines():
                self.topwords.append(line[:-1]) # [:-1] because of \n at end of line
        print("initilised!")
        print(f"{time.time()-x}")

        print(color.YELLOW)
        print("Welcome to the CLI")
        print("What would you like to do? (type h for help)")
        print(color.END)
        pass

    def cli(self):
        print(color.CYAN,"COMMAND=> ",color.END, end="")
        command = input().lower()
        while command not in self.commands:
            print(color.RED)
            print("Not a valid command! Try again!")
            print(color.END)
            print(color.CYAN,"COMMAND=> ",color.END, end="")
            command = input()
        
        if command == "h":
            print(color.GREEN,color.BOLD,"WELCOME TO THE HELP PAGE!", color.END)
            print(color.GREEN)
            print("there are currently 3 commands: ")
            print("h : help")
            print("decrypt : decrypt the input code")
            print("ciphercheck : find out which cipher works best for the code (unfinished)\n")
            print("current decryption methods supported:")
            print("CC : Caesar cipher")
            print("SC : Substitution cipher")
            print("AC : Affine cipher")
            print(color.END)
        elif command == "decrypt":
            print(color.YELLOW)
            print(color.BOLD, "Welcome to the Decryption station!", color.END)
            print(color.PINK)
            print("Enter your decryption code:")
            print("COMMAND=> ", end="")
            decrypt = input()

        
        
        


    # rates how close the text is to "english"
    def englishity(self) -> float:

        return 0



# output highlighting. Yoinked from stack overflow
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   PINK ='\033[95m'
   END = '\033[0m'