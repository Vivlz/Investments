from flask import Flask 

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hallo isch bin de Viv'

app.run()