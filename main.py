from word import arrayWords
from guess import allowedWords
import random

green = "\033[37;42m"
yellow = "\033[37;43m"
grey = "\033[37;100m"
reset = "\033[0m"

yellows = []
greens = []
usedLetters = []

def delete(letter):
    for haha in range(len(yellows)):
        try:
            if yellows[haha] == letter:
                yellows.pop(haha)
        except:
            pass

def main():

    print(green + "Evan's" + reset + " Wordle " + yellow + "Clone" + reset)
    currentWord = arrayWords[random.randint(0,2314)]
    
    for g in range(7):
      yellows.clear()
      greens.clear()
      genGuess()
      for i,c in enumerate(guess):
          if c not in usedLetters:
              usedLetters.append(c)
        
          if c in currentWord:
              if c == currentWord[i]:
                  greens.append(c)
              else: 
                  yellows.append(c)
              
      for b in guess:
          if (greens.count(b) == currentWord.count(b)) and (greens.count(b) != 0):
              delete(b)
          elif (yellows.count(b) + greens.count(b)) > (currentWord.count(b)):
              yellows.remove(b)

      for j,k in enumerate(guess):
          if k in currentWord:
              if k == currentWord[j]:
                  print(green + k + reset, end='')
              elif k not in yellows:
                  print(grey + k + reset, end='')
              elif k in yellows:
                  print(yellow + k + reset, end='')
                  yellows.remove(k)
          else:
              print(grey + k + reset, end='')
      print("")
      print("Used Letters:", usedLetters)
      print("")
      if guess == currentWord:
        print("You win!")
        break
    print("gg")
def genGuess():
    global guess
    guess = input("Guess: ")
    print("")
    if (type(guess) != str) or len(guess) != 5 or (guess not in allowedWords and guess not in arrayWords):
        print("Invalid word, try again")
        genGuess()

if __name__ == '__main__':
  main()