# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
import openai

# OpenAI APIキーを設定する
openai.api_key = "YOUR_API_KEY" #発行したAPI Keyに置き換えてください

# chatGPTによって出力を生成する
def hachiware(input_text):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", 
            # "content": "これから今日の出来事を報告します。それに対して、それって〇〇....ってコト！？と返してください。コトはカタカナで出力してください。〇〇には報告された出来事を表した名詞が入ります。"+input_text},
            "content": "これから今日の出来事を報告します。それに対して、報告された出来事を表した名詞を1つ返してください。"+input_text},
        ]
    )
    output = "それって"+response["choices"][0]["message"]["content"]+"...ってコト！？"
    return output

app = Flask(__name__, static_folder='./static')

# getのときの処理
@app.route('/', methods=['GET'])
def get():
	return render_template('index.html', \
		title = 'ちいかわ構文ジェネレーター', \
		message = 'エッ...')

# postのときの処理	
@app.route('/', methods=['POST'])
def post():
	output = hachiware(request.form['name'])
    
	return render_template('index.html', \
		title = 'ちいかわ構文ジェネレーター', \
		message = output)

if __name__ == '__main__':
	app.run()
