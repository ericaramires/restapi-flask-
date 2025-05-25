from app import app
import os 
from config import DevConfig

if os.getenv('FLASK_DEBUG') == '1': 
    app.config['MONGODB_SETTINGS'] = DevConfig.MONGODB_SETTINGS
else:
    app.config['MONGODB_SETTINGS'] = DevConfig.MONGODB_SETTINGS

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)