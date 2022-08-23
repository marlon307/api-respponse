from ..cms.color import color_cms_blueprint
from ..cms.size import size_cms_blueprint
from ..cms.category import category_cms_blueprint
from ..cms.gender import gender_cms_blueprint
from ..cms.status import status_cms_blueprint


def blue_print_cms(app):
    app.register_blueprint(color_cms_blueprint)
    app.register_blueprint(size_cms_blueprint)
    app.register_blueprint(category_cms_blueprint)
    app.register_blueprint(gender_cms_blueprint)
    app.register_blueprint(status_cms_blueprint)
