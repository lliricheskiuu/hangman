import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

# chosen_word = word_list[random.randint(0, len(word_list) - 1)]
chosen_word = random.choice(word_list)
print(logo)
# print(chosen_word)


display = []
for _ in range(len(chosen_word)):
    display += '_'
print(' '.join(display))


end_of_game = False
lives = 6

while not end_of_game:

    guess = input("Enter a letter: ").lower()
    clear()

    if guess in display:
        print(f"You've already guessed this letter: {guess}")

    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter

    if guess not in chosen_word:
        lives -= 1
        print(f"'{guess}' is not in chosen word.")
        if lives == 0:
            print("You've run out of lives!")
            print(f"The word was {chosen_word}!")
            end_of_game = True

    print(' '.join(display))

    if '_' not in display:
        print("You win!")
        end_of_game = True

    print(stages[lives])