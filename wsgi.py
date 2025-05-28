from application import create_app
import os 
from config import DevConfig

app = create_app('config.DevConfig')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5001)