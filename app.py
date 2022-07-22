from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
from routes.user.user import user_blueprint
from routes.cms.color import product_blueprint
from middleware.m_valid_cnn_front import request_front


app = Flask(__name__)
CORS(app)
# CORS(app, supports_credentials=True) Acept cookie

# app.before_request(request_front)
app.register_blueprint(product_blueprint)
app.register_blueprint(user_blueprint)

msg = {
    "message": "Todos os serviços estão ativos no meomento.",
    "date": datetime.now(),
    "status": 200,
}


@app.route("/")
def index():
    res = jsonify(**msg)
    return res, 200


if __name__ == "__main__":
    app.run(debug=True)
