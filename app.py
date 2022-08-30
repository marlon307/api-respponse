from flask import Flask, jsonify
from flask_cors import CORS
import os, time
from datetime import datetime
from routes.init_route import routes
from middleware.m_valid_cnn_front import request_front

os.environ["TZ"] = "America/Sao_Paulo"
time.tzset()

app = Flask(__name__)
CORS(app)
routes(app)


@app.route("/")
def index():
    res = jsonify(
        {
            "message": "Todos os serviços estão ativos no meomento.",
            "date": datetime.now(),
            "status": 200,
        }
    )
    return res, 200


if __name__ == "__main__":
    app.run(debug=True)
