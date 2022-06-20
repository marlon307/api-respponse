from flask import Flask
from datetime import datetime

from routes.user import user_blueprint

app = Flask(__name__)

# import declared routes

app.register_blueprint(user_blueprint)


@app.route("/")
def index():
    return {
        "message": "Todos os serviços estão ativos no meomento.",
        "date": datetime.now(),
        "status": 200,
    }, 200


if __name__ == "__main__":
    app.run(debug=True)
