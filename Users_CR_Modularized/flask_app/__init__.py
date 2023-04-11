from flask import Flask 
app = Flask(__name__)
app.secret_key = '073Berries'
# secret key is needed to use session