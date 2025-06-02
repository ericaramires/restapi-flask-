import os
from application import create_app

# Load environment variables from .env file if available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    # python-dotenv not installed, rely on system environment variables
    pass

env_config = os.getenv('FLASK_ENV', 'development')

if env_config == 'production':
    config_object_name = 'config.ProdConfig'
elif env_config == 'testing':
    config_object_name = 'config.MockConfig'
else:
    config_object_name = 'config.DevConfig'

app = create_app(config_object_name)

if __name__ == '__main__':
    # Get debug mode from environment variable for security
    debug_mode = os.getenv('FLASK_DEBUG', '0').lower() in ['1', 'true', 'yes']
    
    # Get port from environment variable
    port = int(os.getenv('API_PORT', 5001))
    
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
