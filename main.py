# main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello from Flask!'

# Needed for vercel
if __name__ == "__main__":
    app.run()
