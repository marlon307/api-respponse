from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
from routes.user import user_blueprint
from middleware.m_valid_cnn_front import request_front
import os


app = Flask(__name__)
CORS(app, supports_credentials=True)

# app.before_request(request_front)
app.register_blueprint(user_blueprint)

msg = {
    "message": "Todos os serviços estão ativos no meomento.",
    "date": datetime.now(),
    "status": 200,
}


@app.route("/")
def index():
    res = jsonify(**msg)
    res.set_cookie("user", "user")
    return res, 200


if __name__ == "__main__":
    app.run(debug=False, port=3333)
