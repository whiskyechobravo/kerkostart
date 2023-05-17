import kerko
from flask import Flask
from flask_babel import Babel
from flask_bootstrap import Bootstrap4
from kerko.composer import Composer
from kerko.config_helpers import config_set, config_update, validate_config

app = Flask(__name__)
app.config.from_prefixed_env(prefix='MYAPP')
config_update(app.config, kerko.DEFAULTS)

# Make changes to the Kerko configuration here, if desired.
config_set(app.config, 'kerko.meta.title', 'My App')

validate_config(app.config)
app.config['kerko_composer'] = Composer(app.config)

babel = Babel(app)
bootstrap = Bootstrap4(app)

app.register_blueprint(kerko.blueprint, url_prefix='/bibliography')
