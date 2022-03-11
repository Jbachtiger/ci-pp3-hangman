# PP3 - Python Essentials - Hangman

Hangman is an interactive python terminal word guessing game. It's target audience is students 15 years and above as well as adults. It's a fun and challening game which helps improve spelling and problem solving. It's purpose is to be an easily accessible and modern way to play a game that traditionally was only played using pen and paper. The game has 2 modes, easy and hard depedning on how ambitious the player feels.

![Responsive Mockup]()

## Live Site

[Click here to play Hangman]()

## Table of Contents
- [User Experience (UX)](#user-experience)
  - [User Stories](#user-stories)

- [Design](#design)
  - [Colour Scheme](#colour-scheme)
  - [Typography](#typography)
  - [Wireframes](#wireframes)

- [Features](#features)
  - [Future Development](#future-development)

- [Technologies Used](#technologies-used)
  - [Languages Used](#languages-used)
  - [Frameworks, Libaries and Programs Used](#frameworks-libaries-and-programs-used)

- [Testing](#testing)
  - [Browser and Device Testing](#browser-and-device-testing)
  - [W3C and JSHint Validators](#w3c-and-jshint-validators)
  - [Colour Contrast Checks](#colour-contrast-checks)
  - [Lighthouse Tool](#lighthouse-tool)
  - [Solved Bugs](#solved-bugs)
  - [Known Bugs](#known-bugs)

- [Deployment](#deployment)

- [Credits](#credits)
  - [Code](#code)
  - [Media](#media)
  - [Acknowledgments](#acknowledgments)

## User Experience
### User Stories
__Project Goals__
- To engage students and adults offering an interactive way to play a traditionally none digital game
- Teach players new words
- Improve players problem solving ability
- To be fun and make players want to play again

__Business Owner Goals__
- As a site owner I want to create a fun and engaging game
- As a site owner I want to easily to navigate my game and ensure it is user friendly
- As a site owner I want to have a clear menu showing start game, instructions and exit
- As a site owner I want it to be clear both visually and through text how many attempts/lives a player has left
- As a site owner I want to there to be a choice of difficulty
- As a site owner I want the words in the game to be generated at random
- As a site owner I want consistent feedback to be provided if a user inputs invalid data
- As a site owner I want to allow the player to have an option to continue playing after each game has been finished

__First Time Visitor Goals__
- As a first time visitor I want to be able to find out what type of game it is
- As a first time visitor I want to be able to find clear instructions easily
- As a first time visitor I want to be able to play the game quickly
- As a first time visitor I want to have fun playing the game

 __Returning Visitors__
 - As a returning visitor I want to be able to play the game instantly

## Design
### Colour Scheme
- The colour scheme has been carefully chosen to ensure accessability for all
- The colours compliment each other to ensure text is easily readable in the python terminal
- The colours used provide a fun, colourful and engaging interface
- The main colours used in the game are magenta, cyan, green and red.

### Flowchart

## Features 

### Future Development
- Add a scoring system where players get points for each letter they get right, this would be achived by adding a score variable and incrementing the score each time a letter is correct
- Create a leaderboard display for the players to display there high scores, this would be achieved by using a Google API to link to a Google Sheet where the player names and scores are stored

## Technologies Used
### Languages Used
- [Python](https://www.python.org/)

### Frameworks, Libaries and Programs Used

- [Gitpod](https://gitpod.io/projects) - this was my code editor for this project
- [Git](https://git-scm.com/) - was used for version control using the terminal through Gitpod to commit to Git and push to Github
- [Github](https://github.com/) - is used to store the code for this project after being pushed from Git
- [Techsini](http://techsini.com/multi-mockup/index.php) - was used to generate multi-device website mockups
- [Fireshot](https://chrome.google.com/webstore/detail/take-webpage-screenshots/mcbpblocgmgfnpjjppndjkmgjaogfceg?hl=en) - this was a Google chrome extension used to take screenshots
- [PEP8 Online](http://pep8online.com/) - was used to validate python code to ensure no errors were present
- [Heroku] - (https://www.heroku.com/) - this was the platform used to deploy the application
- Python Packages: 
  - [colorama](https://pypi.org/project/colorama/) >> This import allowed the terminal text to be printed in different colours

  - [os](https://docs.python.org/3/library/os.html) >> The os library was imported to create a function using os.name and os.system to clear the terminal. This library import provided a better user experience ensuring the terminal was clear after each guess and on returning to main menu

  - [random](https://docs.python.org/3/library/random.html?highlight=random#module-random) >> The random library was imported in order to access the functionality to generate a random word the from word.py file using the "random.choice()" method

  - [sys](https://docs.python.org/3/library/sys.html?highlight=sys#module-sys) >> The sys library was imported to use the sys.exit method to allow the user to exit the game

## Testing
This project has been manually tested by doing the following:
- Passed the code through the PEP8 linter and confirmed that there were no issues
- Tested all functionality of the game, ensuring all valid and invalid inputs work e.g. out of bounds inputs, entering nothing, muliple inputs of the same letters
- Thorough manual tesing in my local terminal and the Code Institute Heroku terminal

### PEP8 Linter Results
See below results for the PEP8 linter validation test. No syntax errors/warnings were found in the code.

![PEP8 Linter Results](docs/testing-and-validation/pep8-linter.png)

### Solved Bugs
1. Indentation Errors - a couple times throughout the project I was getting an indentation error due to my lines of code not following the correct indentation procedue. I fixed this by going through the problem code line by line ensuring all the code was following the correct indentation rules

2. Empty spaces, numbers and multiple letters counting as a guess - this issue was solved by refactoring the guess input into a take_guess_input function which has a while loop and if statement to validate the data before input is accepted. [Link to commit](https://github.com/Jbachtiger/ci-pp3-hangman/commit/618065e7f02d53ebc83d7af0aa3af7ec3b1d5c92)

### Known Bugs
There are no known bugs left in this project.












