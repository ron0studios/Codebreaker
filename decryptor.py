# decrypts stuff in one nice class package
import time # timing

class Decryptor():
    topwords = []
    code = ""


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
        pass

    def cli(self):
        print("Welcome to the CLI")
        print("What would you like to do? (type H for help)")
        
        command = input()


    # rates how close the text is to "english"
    def englishity(self) -> float:

        return 0