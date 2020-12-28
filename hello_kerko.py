import pathlib

from flask import Flask
from flask_babel import Babel
from flask_bootstrap import Bootstrap

from kerko import blueprint as kerko_blueprint
from kerko.composer import Composer

app = Flask(__name__)
app.config['SECRET_KEY'] = '_5#y2L"F4Q8z\n\xec]/'  # Replace this value.
app.config['KERKO_ZOTERO_API_KEY'] = 'xxxxxxxxxxxxxxxxxxxxxxxx'  # Replace this value.
app.config['KERKO_ZOTERO_LIBRARY_ID'] = '9999999'  # Replace this value.
app.config['KERKO_ZOTERO_LIBRARY_TYPE'] = 'group'  # Replace this value if necessary.
app.config['KERKO_DATA_DIR'] = str(pathlib.Path(__file__).parent / 'data' / 'kerko')
app.config['KERKO_COMPOSER'] = Composer()

babel = Babel(app)
bootstrap = Bootstrap(app)

app.register_blueprint(kerko_blueprint, url_prefix='/bibliography')
