import kerko
from flask import Flask
from flask_babel import Babel
from flask_bootstrap import Bootstrap4
from kerko.composer import Composer
from kerko.config_helpers import config_set, config_update, parse_config
from kerko.hooks import create_plugin_manager

app = Flask(__name__)

# Initialize the plugin system.
app.plugin_manager = create_plugin_manager()

# Initialize app configuration with Kerko's defaults.
config_update(app.config, kerko.DEFAULTS)

# Update app configuration from environment variables.
app.config.from_prefixed_env(prefix="MYAPP")

# Make changes to the Kerko configuration here, if desired.
config_set(app.config, "kerko.meta.title", "My App")

# Validate configuration and save its parsed version.
parse_config(app.config)

# Initialize the Composer object.
app.config["kerko_composer"] = Composer(app.config)

# Make changes to the Kerko composer object here, if desired.

babel = Babel(app)
bootstrap = Bootstrap4(app)

app.register_blueprint(kerko.make_blueprint(), url_prefix="/bibliography")

# Call init_app hook implementations in plugins.
app.plugin_manager.hook.init_app(app=app)
