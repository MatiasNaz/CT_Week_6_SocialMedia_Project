from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


from .models import User, db

###### bring in routes for registration here #######
from .post.routes import post
from .auth.routes import auth


app = Flask(__name__)
app.config.from_object(Config)
migrate = Migrate(app, db)


#### REGISTER BLUEPRINTS HERE


app.register_blueprint(auth)
app.register_blueprint(post)

login = LoginManager()

login.init_app(app)

## initialize db
db.init_app(app)


@login.user_loader
def load_user(user_id):
    return User.query.get(user_id)
