from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
from routes.user.user import user_blueprint
from routes.cms.color import color_cms_blueprint
from routes.cms.size import size_cms_blueprint
from routes.cms.category import category_cms_blueprint
from routes.cms.gender import gender_cms_blueprint
from middleware.m_valid_cnn_front import request_front


app = Flask(__name__)
CORS(app)
# CORS(app, supports_credentials=True) Acept cookie
# app.before_request(request_front)

# ROTAS CMS
app.register_blueprint(color_cms_blueprint)
app.register_blueprint(size_cms_blueprint)
app.register_blueprint(category_cms_blueprint)
app.register_blueprint(gender_cms_blueprint)

# ROTAS USERS
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
