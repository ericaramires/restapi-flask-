import os
from application import create_app

env_config = os.getenv('FLASK_ENV', 'development')

if env_config == 'production':
    config_object_name = 'config.ProdConfig'
elif env_config == 'testing':
    config_object_name = 'config.MockConfig'
else:
    config_object_name = 'config.DevConfig'

app = create_app(config_object_name)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)
