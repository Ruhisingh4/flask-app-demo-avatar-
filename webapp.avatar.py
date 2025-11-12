from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "🚀 Flask app is live permanently on Render!"

if __name__ == '__main__':
    app.run()

