# Journal of thoughts during Te Hiku Media coding exercise

The intent of this journal is to document my stream of concious thoughts throughout the Te Hiku Media coding exercise so I can share my thought process with the assessment team afterwards.

- 25 March @ 5:25pm - Created this journal document
- 25 March @ 5:30pm - Added `requirements.txt` file with `pytest` as only dependency
- 25 March @ 5:30pm - Added `pyproject.toml` file to set up a Python project with `src` and `test` subdirectories
- 25 March @ 5:30pm - Created a python virtual environment, activated it and installed the requirements file to get `pytest` installed
- 25 March @ 5:30pm - Tested `pytest` command words
- 25 March @ 5:35pm - Added a placeholder readme with setup and testing instructions for the project
- 25 March @ 5:40pm - Created new git repository
- 25 March @ 5:40pm - Added generic python gitignore file
- 25 March @ 5:40pm - Pushed new project to my GitHub
- 25 March @ 5:50pm - Add `black` formatter to dependencies and install it
- 26 March @ 9:00am - Received programming test document link
- 26 March @ 9:00am - Reviewing Tic Tac Toe google document with test instructions
- 26 March @ 9:05am - Confirmed with Keoni that I received instructions
- 26 March @ 9:10am - Getting started on exercise using my existing project setup
- 26 March @ 9:10am - I figure I need a way to print out a Tic Tac Toe board. I will start with writing a unit test to expect an empty board to be returned.
- 26 March @ 9:10am - Grabbed a sample test fixture from my coding kata project to get me started (I can never remember the boilerplate for tests off the top of my head).
- 26 March @ 9:15am - Have test for intial empty board rendering set up. Next I will work on the game state.
- 26 March @ 9:15am - I figure I need to store the moves made by each symbol (player) and pass that to my render function to include any existing moves made. I will store moves as two lists, one for noughts and one for crosses. Each list will include coordinates for a move previously made.
- 26 March @ 9:25am - I was preivously rendering the entire empty board at once, now I need to refactor that code into rendering line by line. It is helpful to extract that responsibility to separate functions.
- 26 March @ 9:30am - In an attempt to keep the render code concise, I googled how to do a ternary operation in Python. I decided to use an `f string` and Googled that syntax too.
- 26 March @ 9:35am - I am reasonably confident my board rendering is working right. Next step will be to add the player interaction in. Unit testing is going to be less helpful as I move into user driven behaviour, so I will test commandline interaction manually.
- 26 March @ 9:40am - I will now set up the game loop to alternate between players, adding moves to respective game state lists each time. To do that, I need to add a code entry point, I will grab a snippet of code from my coding kata project again, as I cannot remember the syntax for the `main` function in Python.
- 26 March @ 9:55am - Have the basic game loop set up, I now need to parse the input into coordinates. The game state must not advance to the next player if an invalid move is specified, but I will handle validation in a moment.
- 26 March @ 10:00am - I am having some trouble with the input parsing, so I will wrap the function in a test to help tease out the bug.
- 26 March @ 10:05am - Looks like I had a bracket syntax error, testing made it very clear and then I found the missing bracket.
- 26 March @ 10:05am - The core of the game loop is now in place, and if the user only enters valid moves it will properly move back and forth between players without getting into a weird state. However, there is still the matter of the win condition and move validation to get right.
- 26 March @ 10:10am - I will get the win condition working, that will give us a complete game. I am going to move back to unit testing to express the win condition logic.
- 26 March @ 10:25am - The win condition is now correctly being checked. I realise I need to add a check for a tie board. I will do that now.
- 26 March @ 10:35am - The tie condition is now being correctly checked. Next I will move on to tightening up the user input and validation scenarios to ensure a smooth game.
- 26 March @ 10:40am - I will first check the boundaries of the coordinates, it strikes me that I should probably accept a 1-based index from user input and convert to a 0-based index in code to be as accomodating for non-programmers as possible.
- 26 March @ 10:45am - I once again need to refer to my coding kata project for how to assert an exception is thrown in a test.
- 26 March @ 10:50am - Have to Google how to grab message from an exception.
- 26 March @ 10:55am - The coordinate boundaries are now being checked for. Next I will move to validating that a move has not already been taken by the other player.
- 26 March @ 11:05am - Moves cannot be taken that another player has already taken now. I believe the game is functionally complete now. Though it feels very rough.
- 26 March @ 11:05am - I am going to sweep over the code, see if I can tidy up or comment anything that feels messy.
