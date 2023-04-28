# chiikawa_generator
「ちいかわ」に登場するハチワレの口調を生成してくれます。chatGPTを使います。
ハチワレは手描きです。

<img width="752" alt="スクリーンショット 2023-03-29 8 32 03" src="https://user-images.githubusercontent.com/74520178/228389927-97249eb1-4a84-4f27-bee5-5baf44d7d735.png">

<img width="752" alt="スクリーンショット 2023-03-29 8 37 37" src="https://user-images.githubusercontent.com/74520178/228390280-4ea3547e-2447-43cb-a1d4-b06ce40e29ed.png">

#### 使い方
1. [Open AIのサイト](https://platform.openai.com/overview)からユーザ登録を行い、API　Keyを発行
2. app.pyの6行目を発行したAPIに書き換える
3. `pip install openai`
4. `pip install flask`
5. `cd chiikawa_generator`
6. `python app.py`
7. ブラウザで[http://127.0.0.1:5000/](http://127.0.0.1:5000/)にアクセス
