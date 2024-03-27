from flask import Flask, render_template, request, redirect, session, json

app = Flask(__name__)

@app.route('/post_chat', methods=['POST'])
def post_chat():
    if request.method == "POST":
        return json.dumps({'success': True}), 201
    else:
        return json.dumps({'success': False}), 400

@app.route('/get_chat', methods=['GET'])
def get_chat():
    if request.method == "GET":
        return json.dumps({'success': True, 'content': "Hello world"}), 201
    else:
        return json.dumps({'success': False, 'content': "You didnt ask to get it!"}), 400

if __name__=="__main__":
    app.run()