import kerko
from flask import Flask
from flask_babel import Babel
from flask_bootstrap import Bootstrap4
from kerko.composer import Composer
from kerko.config_helpers import config_set, config_update, parse_config

app = Flask(__name__)

# Initialize app configuration with Kerko's defaults.
config_update(app.config, kerko.DEFAULTS)

# Update app configuration from environment variables.
app.config.from_prefixed_env(prefix='MYAPP')

# Make changes to the Kerko configuration here, if desired.
config_set(app.config, 'kerko.meta.title', 'My App')

# Validate configuration and save its parsed version.
parse_config(app.config)

# Initialize the Composer object.
app.config['kerko_composer'] = Composer(app.config)

# Make changes to the Kerko composer object here, if desired.

babel = Babel(app)
bootstrap = Bootstrap4(app)

app.register_blueprint(kerko.blueprint, url_prefix='/bibliography')
