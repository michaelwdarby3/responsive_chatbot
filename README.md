# responsive_chatbot
The front and back end of a chatbot, storing question responses, and allowing questions to update over time.


*FEATURES*

There's three major features of this chatbot: 

One is the SQL back end, which stores the questions currently in use, the history of all questions and their past versions, the data for all customers who have gone through the system, and the responses of these customers from responding to each question that existed when they entered their information.

The second is the CLI, which allows us to check what questions are in use, add questions, modify either a questions text or internal meaning, to display the history of either any given question or all questions at once, and check what customers have entered their information.

The third is the front end, which allows customers to enter their information and respond to the questions that exist at this point.

This is, of course, very bare bones.  Use should be fairly self explanatory, especially as the cli has the built-in --help function.  


*SETUP INSTRUCTIONS*

Setup requires only that you have access to sqlite3, click, and uuid.  sqlite3 is included in the standard python module since 2.5, so that's no issue.  Click requires you to run "pip install click", which you may do in a virtual environment or package manager if you don't have it.  uuid should also be built into python.


*USE INSTRUCTIONS*

To begin use, you should first run 'python initialize_sql_backend.py', which will create the database object and all tables you need within it.  Next, you should add questions to the tables, using cli.py's add_question and change_question_text and change_question_meaning functionality.  You should also use front_end.py to simulate a user on this system, to see your questions come up and provide responses.  You can sanity check that these have come through using the cli, as well.  


*CHALLENGES*

The primary challenge was developing a sensible structure to retain questions over time and map those to customer responses in a limited time frame. The problem is not particularly complex, but coming up with an extensible and appropriate structure with so little time to stew was the most difficult part for me.

Additional challenges were trying to keep the cli reasonably small while providing all functionality to the backend user, such that it would be a functional system, as well as testing the system to sanity check integrity.  I mostly implemented the front end as a convenient way to test functionality; the fact that it was actually an invaluable portion of the system on the whole was just a helpful side effect at the time, as I found the testing part to be more important.


*IMPROVEMENTS*

Given more time, I would develop some kind of system to select which questions to ask based on previous responses to questions.  A simple version could be as dumb as a conversation tree, and a more complex version could use ML or NLP techniques.  I would also improve the integrity checks this uses, as there is very little error handling, and tests were entirely just use tests.  I regret that there are no unit tests and no special exceptions, nor is there much handling of bad inputs by anyone.  This is very clearly not production material by any means, as it fails many safety standards, and I would fix that given more time.