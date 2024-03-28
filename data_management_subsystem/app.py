from flask import Flask, render_template, request, redirect, session, json
import datetime

app = Flask(__name__)

@app.route('/post_chat', methods=['POST'])
def post_chat():
    if request.method == "POST":
        print(request.get_json(silent=True))
        return json.dumps({'success': True}), 201
    else:
        return json.dumps({'success': False}), 400

@app.route('/get_chat/<user_id>', methods=['GET'])
def get_chat(user_id):
    
    if request.method == "GET":
        test_data = [(3, "Michael! Don't leave me here!", True, datetime.datetime(2024, 3, 28, 14, 50, 14), 3, 1), (2, 'It is going well. Thanks for asking!', True, datetime.datetime(2024, 3, 27, 13, 36), 2, 1), (1, 'Hello, this is Alethianomous AI! How are you?', True, datetime.datetime(2024, 3, 27, 13, 18), 1, 1), None]
       
        test_data.remove(None)
        i = 0
        for row in test_data:
            test_data[i] = list(test_data[i])
            test_data[i][3] = test_data[i][3].strftime("%m/%d/%Y, %I:%M:%S %p")
            i+=1

        content_json = []
        for row in test_data:
            row_json = {'time_in_edt': row[3], 'content': row[1], 'is_from_bot': row[2]}
            content_json.append(row_json)

        return json.dumps({'success': True, 'chat_history': content_json, 'user_id': int(user_id)}), 201
    else:
        return json.dumps({'success': False, 'content': "You didnt ask to get it!"}), 400

if __name__=="__main__":
    app.run()
