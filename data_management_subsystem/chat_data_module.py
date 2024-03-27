import pyodbc
import pandas as pd


class ChatData():
    def __init__(self, userId):
    
        self.conn = pyodbc.connect('DRIVER= {ODBC Driver 18 for SQL Server}; \
                        SERVER=.alethianomousserver.database.windows.net; \
                        DATABASE=alethianomousserver; \
                        Trusted_Connection=yes')
    
        self.userId = userId
        # if UserAccountManagement.user_exists(userId):
            #self.userId = userId
        # else:
            # raise NonExistentUserException(userId)
    
    
    def log_chat(chat_data, timestamp, is_from_bot):
        """Uploads the chat data to the SQL database.
    
            PARAMETERS:
            chat_data - The chat to upload.
            timestamp - The data which the chat is generated.
            is_from_bot - If true, the chat is from the AI chatbot. 
            Otherwise, the chat is from the AI.
        """
        #chat_id = get_new_chat_id()
    
        
        
        # CREATE SQL QUERY THAT UPLOADS CHAT DATA.
        upload_query = ("""
            WITH ins1 AS(
                INSERT INTO public.chat_history (chat_content, belongs_to_bot, time_of_output)
                VALUES (""" + chat_data + ", " + str(is_from_bot) + "," + str(timestamp)+""")
                RETURNING chat_id
            )
        INSERT INTO public.chat_user (chat_id, user_id)
        SELECT chat_id, """ + str(self.userId) + """ FROM ins1
        RETURNING chat_id;
        """
        )
    
        cursor = self.conn.cursor()
        cursor.execute(upload_query)
        chat_id = cursor.fetchone()
        del cursor
        return chat_id
    
    def return_chat_history(user_id):
        # USE SQL QUERY THAT RETURNS CHAT HISTORY OF FOR USER ID
        fetching_query = ("""
            WITH chat_id_table AS (
                SELECT chat_id
                FROM public.chat_user
                WHERE user_id = """ + str(user_id) + """
                ORDER BY chat_id DESC
            ),
            chat_history_table AS (
                SELECT *
                FROM public.chat_history
                ORDER BY chat_id DESC
            )
            SELECT *
            FROM chat_history_table
            INNER JOIN chat_id_table
            ON chat_id_table.chat_id = chat_history_table.chat_id;
        """)
        cursor = self.conn.cursor()
        cursor.execute(upload_query)
        row = cursor.fetchone()
        chat_hist = [row.copy()]
        while row is not None:
            row = cursor.fetchone()
            chat_hist.append(row.copy())
        print(chat_hist)
