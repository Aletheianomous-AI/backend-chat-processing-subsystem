import pyodbc
import pandas as pd

class ChatData():
	def __init__(self, userId):
		# if UserAccountManagement.user_exists(userId):
			self.userId = userId
		# else:
			# raise NonExistentUserException(userId)

		raise NotImplementedError()

	def log_chat(chat_data, timestamp, is_from_user):
		"""Uploads the chat data to the SQL database.

			PARAMETERS:
			chat_data - The chat to upload.
			timestamp - The data which the chat is generated.
			is_from_user - If true, the chat is from the user. 
			Otherwise, the chat is from the AI.
		"""
		chat_id = get_new_chat_id()
		
		# CREATE SQL QUERY THAT UPLOADS CHAT DATA.
		raise NotImplementedError()

	def return_chat_history(chat_session_id):
		# USE SQL QUERY THAT RETURNS CHAT HISTORY OF CHAT SESSION ID
		# FOR USER ID

		raise NotImplementedError()

