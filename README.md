## Generalized Non-Transitive Dice Game (Python)

This project is a console script game that implements a generalized non-transitive dice game (with the supports of arbitrary values on the dice).
it accepts 3 or more strings aka dices, with any number of faces and values


https://github.com/user-attachments/assets/51299c06-ec9a-43be-afe1-f1ca9d35ca5d



---

### Features

- game supports any number of custom dice with any face values.
- win probability table — shows win probabilities for all dice using a rich library.
- cli menu on every user input (handle exit and showing table).
- fair random generator protocol logic (generates one-time key and hmac(sha3) for every uniformly distributed integer) to prove to the user that choice was fair.
- first move decision and roll logic using fair random generator protocol.
- result calculation use both generated number by computer and user input and their sum using modular arithmetic.
- error handling.

---

## third-party libraries i used: 

- rich
- numpy

---

## Game Flow

  - First move decision
  - Dice selection.
  - Rolling both dice.
  - Declaring a winner.
