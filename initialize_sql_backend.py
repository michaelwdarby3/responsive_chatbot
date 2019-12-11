import sqlite3


def initialize_db_tables():

    db_connection = sqlite3.connect("chatbot.db")

    cursor = db_connection.cursor()

    exists_query = '''SELECT name FROM sqlite_master WHERE type='table' AND name=?;'''

    cursor.execute(exists_query, ('Questions',))
    if len(cursor.fetchall()) == 0:
        cursor.execute("""
            CREATE TABLE Questions (
            question_id VARCHAR(32) NOT NULL PRIMARY KEY,
            question_text text NOT NULL,
            question_meaning text NOT NULL);
        """)

    cursor.execute(exists_query, ('QuestionHistory',))
    if len(cursor.fetchall()) == 0:
        cursor.execute("""
            CREATE TABLE QuestionHistory (
            question_id VARCHAR(32) NOT NULL,
            question_text text NOT NULL,
            question_meaning text NOT NULL,
            creation_time text NOT NULL);
        """)

    cursor.execute(exists_query, ('CustomerData',))
    if len(cursor.fetchall()) == 0:
        cursor.execute("""
            CREATE TABLE CustomerData (  
            customer_id VARCHAR(32) NOT NULL PRIMARY KEY,  
            first_name text NOT NULL,  
            last_name text NOT NULL,  
            gender text NOT NULL,  
            age INTEGER NOT NULL);
        """)

    cursor.execute(exists_query, ('CustomerResponses',))
    if len(cursor.fetchall()) == 0:
        cursor.execute("""
            CREATE TABLE CustomerResponses (
            customer_id VARCHAR(32) NOT NULL,
            question_id VARCHAR(32) NOT NULL,
            response text NOT NULL);
        """)

    db_connection.commit() 
    db_connection.close() 


if __name__ == '__main__':
    initialize_db_tables()