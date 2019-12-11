import sqlite3
import click
import uuid

'''
The command line interface here is fairly simple.  
Use -q to display all questions in the Questions database.
Use -a to add questions.  It autogenerates a unique id for that question.
Use -c to change question text.  It takes, in order, id and the new text.
Use -m to change question meaning. It takes, in order, id and the new meaning.
Use -d to display the history of questions.  You can use it multiple times for specific questions if you wish. Use the unique question ID.
Use -u to display all customers.
Use --help to see the help display.

NOTE: YOU MUST USE QUOTATION MARKS WHEN USING MULTIWORD ARGUMENTS, LIKE ADDING A QUESTION.
'''

@click.command()
@click.option('-q', '--questions', is_flag=True, help="List all questions that exist.")
@click.option('-a', '--add_question', required=False, multiple=True, nargs=2, type=str, help="Add a new question.")
@click.option('-c', '--change_question_text', required=False, multiple=True, nargs=2, type=str, help="Change the text presented to a customer of a question ")
@click.option('-m', '--change_question_meaning', required=False, multiple=True, nargs=2, type=str, help="Change the internal meaning of a question.")
@click.option('-d', '--display_history', required=False, multiple=True, type=str, help="List all past versions of questions.  Give id for specific question, or type 'all' for all questions.")
@click.option('-u', '--customers', is_flag=True, help="List all customers that exist.")

def cli(questions, add_question, change_question_text, change_question_meaning, display_history, customers):

    db_connection = sqlite3.connect("chatbot.db")
    cursor = db_connection.cursor()

    if questions:
        print("Printing all questions.")
        for q in cursor.execute("SELECT * FROM Questions;"):
            print("ID: " + str(q[0]))
            print("Text: " + str(q[1]))
            print("Meaning: " + q[2])
        print("Done printing questions.")

    if add_question:
        for addition in add_question:
            q_id = uuid.uuid4().hex
            cursor.execute("INSERT INTO Questions VALUES (?,?,?)", (q_id, addition[0], addition[1]))
            cursor.execute("INSERT INTO QuestionHistory VALUES (?,?,?,datetime('now'))", (q_id, addition[0], addition[1]))
            print("Question id is: " + str(q_id))

    if change_question_text:
        for change in change_question_text:
            cursor.execute("SELECT * FROM Questions WHERE question_id = ?", (change[0],))
            row = cursor.fetchone()
            if row == None:
                print('ID ' + change[0] + ' does not exist.  Skipping.')
                continue
            cursor.execute("INSERT INTO QuestionHistory VALUES (?,?,?,datetime('now'))", (change[0], change[1], row[2]))
            cursor.execute("UPDATE Questions SET question_id = ?, question_text = ?, question_meaning = ? WHERE question_id = ?", (change[0], change[1], row[2], change[0]))

    if change_question_meaning:
        for change in change_question_meaning:
            cursor.execute("SELECT * FROM Questions WHERE question_id = ?", (change[0],))
            row = cursor.fetchone()
            if row == None:
                print('ID ' + change[0] + ' does not exist.  Skipping.')
                continue
            cursor.execute("INSERT INTO QuestionHistory VALUES (?,?,?,datetime('now'))", (change[0], row[1], change[1]))
            cursor.execute("UPDATE Questions SET question_id = ?, question_text = ?, question_meaning = ? WHERE question_id = ?", (change[0], row[1], change[1], change[0]))

    if display_history:
        if len(display_history) == 1 and display_history[0] == 'all':
            print("History for all rows is as follows:")
            for row in cursor.execute("SELECT * FROM QuestionHistory ORDER BY datetime(creation_time) ASC"):
                print(row)
        else:
            for history_id in display_history:
                print("History for id " + history_id + " is as follows:")
                for row in cursor.execute("SELECT * FROM QuestionHistory WHERE question_id = ? ORDER BY datetime(creation_time) ASC", (history_id,)):
                    print(row)

    if customers:
        print("Printing all customers.")
        for c in cursor.execute("SELECT * FROM CustomerData;"):
            print("ID: " + str(c[0]))
            print("First name: " + str(c[1]))
            print("Last name: " + str(c[2]))
            print("Gender: " + str(c[3]))
            print("Age: " + str(c[4]))
        print("Done printing questions.")

    db_connection.commit()
    db_connection.close()



if __name__ == '__main__':
    cli()
