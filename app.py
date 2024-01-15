from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
    
if __name__ == '__main__':
    app.run('0.0.0.0', 80, True) # port를 80으로
