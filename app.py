from flask import Flask,jsonify
from routers import router

app = Flask(__name__)

router.router(app)

if __name__ == "__main__":
    app.run(debug=True)