# PP3 - Python Essentials - Hangman

Hangman is an interactive python terminal word guessing game. It's target audience is students 15 years and above as well as adults. It's a fun and challening game which helps improve spelling and problem solving. It's purpose is to be an easily accessible and modern way to play a game that traditionally was only played using pen and paper. The game has 2 modes, easy and hard depedning on how ambitious the player feels.

## Live Site

[Click here to play Hangman](https://jbachtiger-ci-pp3-hangman.herokuapp.com/)

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
![Hangman Flowchart](docs/flowcharts/hangman-flowchart.png)
## Features 
- __Welcome Screen__
  - This includes the title to game, with a brief tag line and a hangman image. This title and hangman image are created using ASCII art
  - The purpose of this section is the introduce the game in a visually appealing way which tells you about the game in as little words as possible which is why the accompanying image is also used

  ![Welcome Screen](docs/features/welcome-screen.png)

- __Enter Your Name__
  - The user is then prompted to input their name which once entered returns a welcome message and shows the menu
  - If the user enters an invalid input e.g. empty string an error message is returned
  - This section provides interactivity by taking the users name and provides a personalised welcome message by returning the name they have enterd in the welcome message

  ![Enter Your Name](docs/features/name-input.png)

  ![Invalid Name Input](docs/features/name-input-error-msg.png)

- __Menu__
  - The menu has been created to be simple and direct the player to useful options
  - It clearly informs the player what input returns each option
  - There are 3 choices, start game, instructions and exit which closes the programme
  - Validation has been put in place to provide feedback to the user if they input an invalid command

  ![Menu](docs/features/menu.png)

  ![Menu Validation](docs/features/menu-validation.png)

- __Instructions__
  - This section provides the player with a detialed list of instructions on how to play the hangman game
  - It's purpose is to help the player understand the game mechanics so they can get the most out of playing the game and enjoy their experience
  - There is a command to direct the user back to the main menu
  - Validation has also been added to provide feedback if an invalid input is entered

  ![Instructions](docs/features/instructions.png)

  ![Instructions Validations](docs/features/instructions-validations.png)

- __Exit The Game__
 - The exit game option, exits the application and ends the game
 - To be able to start it again the run programme button needs to be entered
 - This provides the player an option to leave the game should they desire
 - A thank you message is displayed if this option is chosen to thank the player for playing the game

 ![Exit the game](docs/features/exit.png)

 - __Start Game and Difficulty Option__
   - Once the start game option is entered, the player is asked what difficulty they wish to play
   - There are two levels, easy or hard which also has validation to feedback to the player if an incorrect command is entered
   - Once the difficulty is chosen the main game starts
   - The way each step has been designed means that the player is directed for each stage of setting up the game and prompted with feedback if they make a mistake

![Difficulty](docs/features/difficulty.png)

![Difficulty Validation](docs/features/difficulty-validation.png)

![Game](docs/features/hangman-game.png)


- __Enter Your Guess__
  - Takes the players letter guess input
  - If the input is correct then a correct letter message appears and the player is prompted to guess another letter
  - If the player is incorrect then an attempt is removed, a section of the hangman image appears and the player is prompted to guess again until all attempts have been used up
  - All letters that have been guess are put into the used letters section
  - Validation has been put in place to provide feedback to the player if they try to enter an invalid input such as entering nothing, a number, multiple letters or a duplicated letter

  ![Correct Guess](docs/features/correct-guess.png)

  ![Incorrect Guess](docs/features/incorrect-guess.png)

  ![Empty Space Validation](docs/features/empty-space-validation.png)

  ![Number Validation](docs/features/number-validation.png)

  ![Multiple Letters Validation](docs/features/multiple-letter-validation.png)

  ![Repeat Letter Validation](docs/features/duplication-validation.png)


- __Win Game__
  - Once all correct letters have been guessed, the player wins the game and a win game message appears
  - A play again option is then displayed, if the user plays again they will be asked for their difficulty and the game will start
  - If they choose to stop playing they will be returned to the main menu

  ![Win Game](docs/features/win-game.png)


- __Lose Game__
  - Once all guess attempts have been used up the hangman image appears, attempts left becomes 0, the correct word is shown and a you lose message appears
  - A play again option is then displayed, if the user plays again they will be asked for their difficulty and the game will start
  - If they choose to stop playing they will be returned to the main menu

  ![Game Over](docs/features/gameover.png)


-__Validation__
  - Validation has been added throughout the game to provide players with feedback to prompt them when an incorrect/invalid input has been entered
  - They also give the player a hint as to why the error has occured

- __Text Colours__
  - Colours have been used heavily in this game, this is to make it more interactive and engaging 
  - The colours also have meanings behind them such as green for correct answers and red for incorrect/invalid inputs
  - The purpose of these are to inform the player quickly what might be happening without even having to read all the text


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
- [Heroku](https://www.heroku.com/) - this was the platform used to deploy the application
- [Patorjk.com](https://patorjk.com/software/taag/#p=display&f=Rectangles&t=Welcome%20to%20Hangman) - ASCII code generator
- [Lucidchart](https://www.lucidchart.com/pages/) - this program was used to create the flowchart which maps out the logic for this hangman project
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

## Deployment

This application has been deployed using Heroku by following these steps:

1. Commit all changes and push them to GitHub
2. Log in to [Heroku](https://www.heroku.com/) or create a new account
3. From the Heroku dashboard click the "Create New App" button
4. Enter the name of your app and the region your located in. Then click "Create App". It is worth noting that your app name must be unique for Heroku to accept it
5. The next section is the deployment section for the app. Click on the "Settings" tab and scroll down to config vars
6. Click on "Reveals Config Vars" and add the KEY: CREDS and the VALUE stored in creds.json file if needed
7. Add the Config Var, KEY: PORT and VALUE: 8000
8. Next, go to the buildpacks section by scrolling down the page and click "Add Buildpack"
9. Select "Python" and click "Save Changes"
10. Repeat step 8, this time select "Nodejs" and click "Save Changes"
11. Please ensure your buildpacks have been selected in the above order, python on top and nodejs below
12. Go to the "Deploy" tab and scroll down to the "Deployment Method" section
13. Select "GitHub" as the method and click "Connect to GitHub"
14. Scroll down to the "Connet to GitHub" section and search for the depository name you wish to delpoy. Do this by typing in the depository name and click the "Search button
15. Once the depository has been found, connect it by clicking the "Connect" button next to it's name
16. Choose "Automatic deploys" or "Manual deploys" to deploy your application

## Credits
### Code
- [DelftStack](https://www.delftstack.com/howto/python/python-clear-console/) - this website provided the neccessary information and code snippet to create a clear terminal function
- [MJ Codes](https://www.youtube.com/watch?v=wmSysRui0cI&ab_channel=MJCodes) - the base logic of the start_game() function was amended from this Youtube tutorial. The code has been extensively modified and extra features/components added to it

### Media
- The ASCII art code for the different hangman stages were taken from [here](https://github.com/mj-linane/cs4all-python-student-templates/blob/master/hangman-art.py)
- The ASCII header code uses the Rectangles font and was taken from [Patorjk.com](https://patorjk.com/software/taag/#p=display&f=Rectangles&t=Welcome%20to%20Hangman)

### Resources
- [Python.org](https://www.python.org/) - was used to broaden knowledge of language and troubleshoot issues
- [PyPi.org](https://pypi.org/project/colorama/) - was used to understand how to use the colorama api to print coloured terminal text
- [StackOverflow](https://stackoverflow.com/) - was used to broaden knowledge to trooubleshoot issues
- [Kylie Ying Youtube Tutorial](https://www.youtube.com/watch?v=8ext9G7xspg&t=1465s&ab_channel=freeCodeCamp.org) - this Youtube tutorial was used for inspiration and was part of my orignal research into Hangman games
- Code Institute Tutor Support - I used tutor support a couple times to help me identify and resolve issues with my python code

### Acknowledgments
- My mentor for their support, advice and patience when reviewing this project with me
- My partner, for being so supportive and patient with me throughout this project and helping me test it













