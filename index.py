from flask import Flask, jsonify
from datetime import datetime
from routes.user import user_blueprint
from middleware.m_user import m_user


app = Flask(__name__)


app.register_blueprint(user_blueprint)

app.before_request_funcs = {
    "routes_user": [m_user],
}


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
