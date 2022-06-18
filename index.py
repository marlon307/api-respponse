from flask import Flask
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return {
        "message": "Todos os serviços estão ativos no meomento.",
        "date": datetime.now(),
        "status": 200,
    }


if __name__ == "__main__":
    app.run(debug=True)
