from mongoengine import connect


def init_db(app):
    """
    Initialize the database connection using the configuration from the
    Flask app
    """
    try:
        if 'MONGODB_SETTINGS' in app.config and \
           isinstance(app.config['MONGODB_SETTINGS'], dict) and \
           'host' in app.config['MONGODB_SETTINGS'] and \
           isinstance(app.config['MONGODB_SETTINGS']['host'], str) and \
           app.config['MONGODB_SETTINGS']['host'].startswith('mongodb+srv://'):
            
            connect(host=app.config['MONGODB_SETTINGS']['host'],
                    authentication_source='admin')
            print("Attempting to connect to MongoDB Atlas...")
        else:
            connect(
                db=app.config['MONGODB_DB'],
                host=app.config['MONGODB_HOST'],
                port=app.config['MONGODB_PORT'],
                username=app.config['MONGODB_USERNAME'],
                password=app.config['MONGODB_PASSWORD'],
                authentication_source='admin'
            )
            print(f"Attempting to connect to local/dev MongoDB: {app.config['MONGODB_HOST']}...")
        
        print("Connected to MongoDB successfully!") 
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise
