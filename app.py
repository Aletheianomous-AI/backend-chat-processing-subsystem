from flask import Flask, render_template, request, redirect, session, json
from datetime import datetime as dt
from response_gen_module.response_generator import ResponseGenerator

import datetime


app = Flask(__name__)


@app.route(/generate_response, methods=['POST'])
def generate_response():
    if request.method == "POST":
        json_data = request.get_json(silent=True)
        user_input = json_data['input']
        rg = ResponseGenerator()
        citations, ai_response = rg.generate(user_input)
        return json.dumps({'success': True, 'citations': citations, output': ai_response}), 201
    else:
        return json.dumps({'success': False}), 400

if __name__=="__main__":
    app.run()
