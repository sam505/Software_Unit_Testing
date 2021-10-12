from threading import Timer
import enchant
import random

d = enchant.Dict("en-US")


def calculate_word_score(word):
    score = 0
    for letter in word:
        score += calculate_letter_score(letter)

    return score


def calculate_letter_score(letter):
    if letter.upper() in ["A", "E", "I", "O", "U", "L", "N", "R", "S", "T"]:
        return 1
    elif letter.upper() in ["D", "G"]:
        return 2
    elif letter.upper() in ["B", "C", "M", "P"]:
        return 3
    elif letter.upper() in ["F", "H", "V", "W", "Y"]:
        return 4
    elif letter.upper() in ["K"]:
        return 5
    elif letter.upper() in ["J", "X"]:
        return 8
    elif letter.upper() in ["Q", "Z"]:
        return 10
    else:
        return 0


def check_word(word):
    return d.check(word)


def main():
    timeout = 15
    t = Timer(timeout, print)
    length = random.randint(3, 10)
    t.start()
    prompt = "Enter a word of {} letters in {} seconds: ".format(length, timeout)
    word = input(prompt)
    t.cancel()
    if t.is_alive():
        if check_word(word):
            if len(word) == length:
                print("Your score is: {}".format(calculate_word_score(word)))
                return True
            else:
                print("Word did not match length")
                return False
        else:
            print("Word not found")
            return False

    else:
        print("Sorry, times up")
    return t.is_alive()


if __name__ == "__main__":
    main()
