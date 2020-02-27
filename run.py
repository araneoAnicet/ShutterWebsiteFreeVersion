from flask import Flask
from flaskapp.site.routes import mod as site_routes
from flaskapp.rest.routes import mod as rest_routes


app = Flask(__name__)
app.register_blueprint(rest_routes, url_prefix='/api')
app.register_blueprint(site_routes, url_prefix='/')

if __name__ == '__main__':
    app.run(debug=True)
