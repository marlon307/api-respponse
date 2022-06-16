from flask import Flask
from datetime import datetime

app = Flask(__name__)

if __name__ == "__main__":
    app.run(debug=True)


@app.route("/")
def hello_world():
    return {
        "message": "Todos os serviços estão ativos no meomento.",
        "date": datetime.now(),
        "status": 200,
    }
