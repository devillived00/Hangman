import random

#Fail count used for breaking a loop, those are our "lives" in game
fail_guess_count = 10

#Appending words from a text file
a_file = open("sample.txt", "r")
list_of_lists = []
for line in a_file:
    list_of_lists.append(line.strip())

a_file.close()

#Making a list that contains all the letters of a random word chosen from the list of words
random_word = []
random_word1 = list_of_lists[random.randint(0, len(list_of_lists))]
for i in random_word1:
    random_word.append(i)

#It's for a display
spaces = []
for i in random_word:
    spaces.append(' _ ')


class Main:
    def __init__(self, spaces, random_word, fail, random_word1):
        self.spaces = spaces
        self.random_word = random_word
        self.fail = fail
        self.random_word1 = random_word1

    def game(self):
        while True:
            #Live display of correct answers
            print()
            print('\t', *self.spaces, sep=' ')
            print()

            #Breaks the loop if we won or lost
            if ' _ ' not in self.spaces:
                print("You've won!")
                break

            elif self.fail == 0:
                print("You've lost!")
                print()
                print("The word was:")
                print()
                print(*self.random_word1, sep='')
                break

            user_input = str(input("Enter a letter:\n>>>> "))

            #It counts our chances left
            if user_input not in self.random_word:
                self.fail -= 1
                if self.fail > 0:
                    print(f'Try again, you have {self.fail} chances left')

            #If statement to check whether our guess was correct or not, it's replacing " _ " in the correct place
            #It is working on indexes
            for i in range(5):
                if user_input in self.random_word:
                    x = self.random_word.index(user_input)
                    self.spaces[x] = user_input
                    self.random_word[x] = "0"
                    if user_input in self.random_word:
                        y = self.random_word.index(user_input)
                        self.spaces[y] = user_input


game1 = Main(spaces, random_word, fail_guess_count, random_word1)
game1.game()
