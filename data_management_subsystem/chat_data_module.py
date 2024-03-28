from pytz import timezone

import pyodbc
import pandas as pd


class ChatData():
    def __init__(self, userId):
        server = "alethianomousserver.database.windows.net"
        db_name = "Alethianomous AI"
        uname = "sp15"
        passwrd = "200322927eE!"

        con_str = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={db_name};UID={uname};PWD={passwrd}'
        self.conn = pyodbc.connect(con_str)
    
        self.userId = userId
        # if UserAccountManagement.user_exists(userId):
            #self.userId = userId
        # else:
            # raise NonExistentUserException(userId)
    
    
    def log_chat(self, chat_data, timestamp, is_from_bot):
        """Uploads the chat data to the SQL database.
    
            PARAMETERS:
            chat_data - The chat to upload.
            timestamp - The data which the chat is generated.
            is_from_bot - If true, the chat is from the AI chatbot. 
            Otherwise, the chat is from the AI.
        """
       
        chat_data = chat_data.replace("'", "''")
        print("Parsed chat data: " + chat_data)

        timestamp = timestamp.astimezone(timezone('America/New_York'))
        timestamp = timestamp.strftime("%Y%m%d %I:%M:%S %p")
        print(timestamp)

        # CREATE SQL QUERY THAT UPLOADS CHAT DATA.
        upload_query = ("""
        BEGIN TRANSACTION
            DECLARE @ChatID int;
    		SELECT @ChatID = (MAX(Chat_ID) + 1)
            FROM dbo.Chat_History;
            INSERT INTO dbo.Chat_History (Chat_ID, Chat_Content, Belongs_To_Bot, Time_Of_Output)
            VALUES (@ChatID, '""" + chat_data + """', 1, '""" + timestamp+ """');
            INSERT INTO dbo.Chat_User (Chat_ID, UserID) VALUES (@ChatID, 1);
        COMMIT

        """
        )
    
        cursor = self.conn.cursor()
        cursor.execute(upload_query)
        del cursor

        cursor = self.conn.cursor()
        chat_id_qry = ("""
            SELECT MAX(Chat_ID) FROM dbo.Chat_History;
        """
        )
        cursor.execute(chat_id_qry)
        chat_id = cursor.fetchall()
        return chat_id
    
    def return_chat_history(self):

        fetching_query = """
            SELECT *
            FROM dbo.Chat_History AS ch
            INNER JOIN dbo.Chat_User AS cu
                ON (cu.Chat_ID = ch.Chat_ID)
            WHERE cu.UserId = """ + str(self.userId) + """
            ORDER BY cu.Chat_ID DESC
        """
        

        cursor = self.conn.cursor()
        cursor.execute(fetching_query)
        row = cursor.fetchone()
        chat_hist = [row]
        while row is not None:
            row = cursor.fetchone()
            chat_hist.append(row)
        return chat_hist
