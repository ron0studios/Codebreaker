# decrypts stuff in one nice class package
import time # timing
from collections import defaultdict # because normal dicts dont support default key-value values
from cipher_solver.simple import SimpleSolver


class Decryptor():
    COMMON_WORDS = []
    BIGRAMS = {}
    TRIGRAMS = {}

    CODE = "" # thanks Chris
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    COMMANDS = ("h", "q", "decrypt", "ciphercheck")
    CYPHER_SUPPORT = ("caesar", "affine", "substitution", "atbash")


    def __init__(self, code=""):
        t1 = time.time()
        print(color.GREEN)
        print("Initialising...")
        self.CODE = code
        print("Loading common words...")
        with open("common_words", "r") as f:
            for line in f.readlines():
                self.COMMON_WORDS.append(line[:-1]) # [:-1] to get rid of \n
        print("Loading bigrams...")
        with open("bigrams", "r") as f:
            for line in f.readlines():
                temp_count_list = line.split()
                self.BIGRAMS[temp_count_list[0]] = float(temp_count_list[1][:-1]) # [:-1] to get rid of \n
        print("Initilised!")
        print(f"Time taken: {time.time()-t1} seconds")

        print(color.YELLOW)
        print("Welcome to the CLI")
        while not self.CODE:
            print(color.RED,"it seems that you haven't set a code yet, please input it below:")
            print(color.CYAN,"INPUT CODE=> ",color.END, end="")
            self.CODE = input()
        
        print("What would you like to do? (type h for help)")
        print(color.END)
        pass
    

    # enjoy this eyesore of a CLI:
    def cli(self):
        print(color.CYAN,"COMMAND=> ",color.END, end="")
        command = input().lower()
        while command not in self.COMMANDS:
            print(color.RED)
            print("Not a valid command! Try again!")
            print(color.END)
            print(color.CYAN,"COMMAND=> ",color.END, end="")
            command = input()
        if command == "q":
            quit()
        if command == "h":
            print(color.GREEN,color.BOLD,"WELCOME TO THE HELP PAGE!", color.END)
            print(color.GREEN)
            print("there are currently 4 commands: ")
            print("h : help")
            print("q : quit")
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
            output, timetaken = self.decrypt()
            print(color.GREEN)
            print(output)
            print(color.END)
            print(color.PURPLE)
            print(f"Time Taken: {color.BOLD}{timetaken}{color.END}{color.PURPLE} seconds")
            print(color.END)
        elif command == "cyphercheck":
            print(color.YELLOW)
            print(color.BOLD, "Checking which cypher works best!")
            print(self.cyphercheck)
            

    def cyphercheck():
        return "this is unfinished!!!! Sorry"
    

    # decrypt command cli 
    def decrypt(self):
        inp = input().lower()
        while inp not in self.CYPHER_SUPPORT:
            print("This is an invalid cypher! Try again:")
            print("INPUT CYPHER=> ", end="")
            inp = input()

        if inp == "caesar":
            t1 = time.time()
            out = self.caesar_decode(self.CODE)
            return out, time.time()-t1
        elif inp == "substitution":
            print("SOLVE TYPE => ", end="")
            method = input()
            t1 = time.time()
            out = self.substitution_decode(self.CODE, method=method)
            return out, time.time()-t1
        elif inp == "atbash":
            t1 = time.time()
            out = self.atbash_decode(self.CODE)
            return out, time.time()-t1


    # rates how close the text is to "english"
    # uses bigram detection and chi squared formula
    def englishity(self, code) -> float:

        total = 0

        # occurences of bigrams in the code
        codecount = {}

        # occurences of bigrams in real life
        realcount = self.BIGRAMS

        # creates defaultdict because then the += operator wont work on empty keys
        codecount = defaultdict(lambda:0,codecount)

        # counts bigrams
        for i in range(len(code)-1):
            total += 1
            if code[i]+code[i+1] in realcount:
                codecount[code[i]+code[i+1]]+=1
        
        # converts codecount to a percentage instead of raw occurences (so we can compare with realcount)
        for i in codecount.keys():
            codecount[i] = float(codecount[i]/total)
        
        # chi squared formula, which is basically just standard deviation
        chisquared = 0
        for i in realcount.keys():
            chisquared += pow(codecount[i]-realcount[i],2)/realcount[i]

        return chisquared


    # thanks Chris
    # np lol
    def caesar_decode(self, code):
        key = 1
        decrypted_messages = []

        while key < 26:
            new_message = ""

            for c in code:
                c = c.lower()
                if c in self.ALPHABET:
                    position = self.ALPHABET.find(c)
                    new_position = (position - key) % 26
                    new_character = self.ALPHABET[new_position]
                    new_message += new_character
                else:
                    new_message += c
            
            decrypted_messages.append(new_message)
            key += 1

        optimal_message = ""
        optimal_englishity = 10000000000000000
        

        for message in decrypted_messages:
            val = self.englishity(message)
            if val < optimal_englishity:
                optimal_englishity = val
                optimal_message = message
        
        return optimal_message
    

    def atbash_decode(self, code):
        reversed_alphabet = self.ALPHABET[::-1]
        new_message = ""

        for c in code:
            c = c.lower()
            if c in self.ALPHABET:
                position = self.ALPHABET.find(c)
                new_character = reversed_alphabet[position]
                new_message += new_character
            else:
                new_message += c
        
        return new_message
    
    
    def substitution_decode(self, code, method):
        if method == "random":
            s = SimpleSolver(code)
            s.solve()
            return s.plaintext()
        elif method == "deterministic":
            s = SimpleSolver(code)
            s.solve()
            return s.plaintext()
        else:
            print("Wrong solve method: random / deterministic")
            return None


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
