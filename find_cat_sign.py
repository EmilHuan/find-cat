### find_cat 註冊、登入頁面

# 匯入套件
from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request

# 初始化 (讓 flask 知道 root 在哪裡)
app = Flask(__name__)

# 最初網址 (設定導向首頁)
@app.route("/")
def index():
    return redirect(url_for("home"))

# 首頁
@app.route("/find_cat")
def home():
    return render_template("cat_first.html")

# 註冊頁面
@app.route("/find_cat/signup")
def signup():
    return render_template("cat_signup.html")

# 登入頁面
@app.route("/find_cat/login")
def login():
    return render_template("cat_login.html")



if __name__ == "__main__":
    app.debug = True # 網頁開發、測試時除錯用，正式版本不要用
    app.run() # 啟動伺服器


