from flask import Flask, jsonify
from datetime import datetime
from routes.user import user_blueprint
from middleware.m_valid_cnn_front import request_front


app = Flask(__name__)

app.before_request(request_front)
app.register_blueprint(user_blueprint)


@app.route("/")
def index():
    return (
        jsonify(
            message="Todos os serviços estão ativos no meomento.",
            date=datetime.now(),
            status=200,
        ),
        200,
    )


if __name__ == "__main__":
    app.run(debug=True)
