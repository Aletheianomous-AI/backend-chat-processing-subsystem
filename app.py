from flask import Flask, render_template, request, redirect, session, json
from datetime import datetime as dt
from response_gen_module.response_generator import ResponseGenerator

import datetime
import traceback

app = Flask(__name__)


@app.route("/generate_response/", methods=['POST'])
def generate_response():
    try:
        if request.method == "POST":
            json_data = request.get_json(silent=False)
            user_input = json_data['input']
            print("Generating response")
            rg = ResponseGenerator()
            citations, ai_response = rg.generate(user_input)
            return json.dumps({'success': True, 'citations': citations, 'output': ai_response}), 201
        else:
            return json.dumps({'success': False}), 400
    except Exception as e:
            traceback.print_exc()
            return json.dumps({'success': False, 'exception_details': str(e)}), 500

if __name__=="__main__":
    app.run()
