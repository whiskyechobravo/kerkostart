import pathlib

import kerko
from environs import Env
from flask import Flask
from flask_babel import Babel
from flask_bootstrap import Bootstrap4
from kerko.composer import Composer

env = Env()
env.read_env()

app = Flask(__name__)
app.config['SECRET_KEY'] = env.str('SECRET_KEY')
app.config['KERKO_ZOTERO_API_KEY'] = env.str('KERKO_ZOTERO_API_KEY')
app.config['KERKO_ZOTERO_LIBRARY_ID'] = env.str('KERKO_ZOTERO_LIBRARY_ID')
app.config['KERKO_ZOTERO_LIBRARY_TYPE'] = env.str('KERKO_ZOTERO_LIBRARY_TYPE')
app.config['KERKO_DATA_DIR'] = str(pathlib.Path(__file__).parent / 'data' / 'kerko')
app.config['KERKO_COMPOSER'] = Composer()

babel = Babel(app)
bootstrap = Bootstrap4(app)

app.register_blueprint(kerko.blueprint, url_prefix='/bibliography')
