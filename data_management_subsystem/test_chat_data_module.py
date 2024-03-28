from chat_data_module import ChatData
from datetime import datetime as dt


if __name__ == '__main__':
    test_chat = ChatData(1)
    test_chat.log_chat("Michael! Don't leave me here!", dt.now() , 1)
    history = test_chat.return_chat_history()
    print(history)
