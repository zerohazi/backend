# Python 3.5.2 にて動作を確認
# sqlite3 標準モジュールをインポート
import sqlite3, os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# データベースファイルのパス
dbpath = BASE_DIR + '/app1/sample_db.sqlite'

#DBを書き込む関数
def write(text,text1):
    # データベース接続とカーソル生成
    connection = sqlite3.connect(dbpath)
    # 自動コミットにする場合は下記を指定（コメントアウトを解除のこと）
    # connection.isolation_level = None
    cursor = connection.cursor()

    # エラー処理（例外処理）
    try:
        # INSERT
        
        cursor.execute("INSERT INTO test (name,comment) VALUES(?,?)", (text,text1))
    
    except sqlite3.Error as e:
        print('sqlite3.Error occurred:', e.args[0])

    # 保存を実行（忘れると保存されないので注意）
    connection.commit()

    # 接続を閉じる
    connection.close()

    return None
   
   
#DBを読み込む関数    
def read(text):
    
    
    
    return None