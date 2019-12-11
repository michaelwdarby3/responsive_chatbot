import sqlite3
import click
import uuid


def front_end():
    try:
        db_connection = sqlite3.connect("chatbot.db")
        cursor = db_connection.cursor()

        c_id = uuid.uuid4().hex
        first_name = input("Please tell me your first name.\n")
        last_name = input("Please tell me your last name.\n")
        gender = input("Please tell me your gender.\n")
        age = input("Please tell me your age.\n")


        cursor.execute("INSERT INTO CustomerData VALUES (?,?,?,?,?)", (c_id, first_name, last_name, gender, age))

        cursor.execute("SELECT * from Questions;")
        questions = cursor.fetchall()
        print(questions)
        for question in questions:
            q_id = question[0]
            response = input(question[1] + "\n")
            cursor.execute("INSERT INTO CustomerResponses VALUES (?,?,?)", (c_id, q_id, response))

        
        db_connection.commit() 
        db_connection.close() 

        print("Thank you for your time! We'll be back to you with results shortly.  Please check your email.")
    except:
        print("Something went wrong.  Please try again later.")




if __name__ == '__main__':
    front_end()