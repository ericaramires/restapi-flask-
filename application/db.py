from mongoengine import connect

def init_db(app):
    """
    Initialize the database connection using the configuration from the Flask app
    """
    try:
        connect(
            db=app.config['MONGODB_DB'],
            host=app.config['MONGODB_HOST'],
            port=app.config['MONGODB_PORT'],
            username=app.config['MONGODB_USERNAME'],
            password=app.config['MONGODB_PASSWORD'],
            authentication_source='admin'
        )
        print("Connected to MongoDB successfully!")
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise
