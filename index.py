from flask import Flask, jsonify
from datetime import datetime
from routes.user import user_blueprint

# from middleware.m_user import valide_user

app = Flask(__name__)
# app.wsgi_app = valide_user(app.wsgi_app)


app.register_blueprint(user_blueprint)


# def teste():
#     print('sdkaskdjasdjkansbdkjasd')


# def teste1():
#     print("sdkaskdjasdjkansbdkjasd 9999999999999999--------------")


# app.before_request_funcs = {
#     "routes_user": [teste, teste1],
# }


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
