Flexible REST API Flask with MongoDB 🚀

📝 Quick Summary
A robust and flexible RESTful API built with Flask and Python, designed to manage user data. Its key feature is the ability to dynamically connect to different MongoDB instances based on environment configuration, making it ideal for development, testing, and production.

✨ Project Overview
This project demonstrates the creation of a complete RESTful API, from data modeling with MongoEngine to exposing endpoints with Flask-RESTful. It emphasizes good development practices, such as separating configurations by environment (allowing flexible MongoDB connections), using Docker for containerization, and writing automated tests with Pytest. The project serves as a practical example to showcase skills in backend development, working with NoSQL databases, and familiarity with the DevOps ecosystem.

🎯 Motivation
The main goal was to develop an API that not only fulfilled the functional requirements of a user CRUD but also served as a practical example of how to build Python applications ready for different stages of the development lifecycle. Flexibility in database configuration and integration with Docker were key points to simulate an environment closer to reality.

🛠️ Technologies Used
Backend: Python 3, Flask, Flask-RESTful

ORM/ODM: MongoEngine (for MongoDB)

Database: MongoDB

Containerization: Docker, Docker Compose

Testing: Pytest

🚀 Key Features
User Management:

Creation of new users with data validation, including CPF format (Cadastro de Pessoas Físicas, the individual taxpayer registry identification number in Brazil).

Listing of all registered users.

Search for a specific user by their CPF.

Multi-Environment Configuration:

Support for Development, Production, and Testing environments, controlled by the FLASK_ENV variable.

Dynamic connection to the MongoDB instance configured for each environment.

Containerization with Docker:

Dockerfile to build the application image.

docker-compose.yml to orchestrate the application and the MongoDB service in a development environment.

Automated Tests:

Test suite using Pytest to ensure API endpoint functionality.

⚙️ Configuration and Installation
Follow the steps below to configure and run the project.

Prerequisites
Python 3.9 or higher

Pip (Python package manager)

Docker and Docker Compose (Recommended, especially for the default development environment)

Access to a MongoDB instance (for the production environment, usually a cluster on MongoDB Atlas; for development/testing, it can be local or Docker).

1. Create and Activate a Virtual Environment (Recommended)
First, create the virtual environment:

python -m venv venv

Then, activate it based on your operating system:

On Linux/macOS:

source venv/bin/activate

On Windows (PowerShell):

.\venv\Scripts\Activate.ps1

On Windows (CMD):

venv\Scripts\activate.bat

2. Install Dependencies
With the virtual environment activated, install the project dependencies:

pip install -r requirements.txt

3. MongoDB Database Configuration
For Development (Docker): The docker-compose.yml already provisions a MongoDB service.

For Development (Local): Ensure you have a MongoDB instance running locally on port 27017 (or adjust DevConfig in config.py).

For Production (MongoDB Atlas):

Create a cluster on MongoDB Atlas.

Configure the "IP Access List" to allow connections from your IP or 0.0.0.0/0 (for testing, with caution).

Create a database user with the necessary permissions.

Obtain the connection string (URI) for your cluster.

Update the connection string in the ProdConfig class within the config.py file:

# config.py
class ProdConfig:
    MONGODB_SETTINGS = {
        'host': 'YOUR_FULL_ATLAS_CONNECTION_STRING_HERE'
    }
    # ... (other ProdConfig settings if any)

For Testing: MockConfig points to a local MongoDB on port 27018.

🔧 Detailed Environment Configurations
The application uses the FLASK_ENV environment variable to determine which set of configurations to load. The init_db function in application/db.py automatically detects whether to use the full Atlas URI (for production) or detailed settings (for development/testing).

FLASK_ENV

Configuration Used

Primary Database

Connection Details (Default)

development

DevConfig

Local/Docker MongoDB

db='users', host='mongodb' (Docker) or localhost, port=27017

(not set)

DevConfig

Local/Docker MongoDB

(Same as development)

production

ProdConfig

MongoDB Atlas

Full URI defined in ProdConfig

testing

MockConfig

Local MongoDB (for testing)

db='users_test', host='localhost', port=27018

Configuration Structure in config.py (Examples):

DevConfig (Development):

class DevConfig:
    MONGODB_DB = os.getenv('MONGODB_DB', 'users')
    MONGODB_HOST = os.getenv('MONGODB_HOST', 'mongodb') # 'mongodb' for Docker, 'localhost' for local
    MONGODB_PORT = int(os.getenv('MONGODB_PORT', 27017))
    MONGODB_USERNAME = os.getenv('MONGODB_USERNAME', 'admin')
    MONGODB_PASSWORD = os.getenv('MONGODB_PASSWORD', 'admin')

ProdConfig (Production):

class ProdConfig:
    MONGODB_SETTINGS = {
        'host': 'mongodb+srv://YOUR_USER:YOUR_PASSWORD@YOUR_CLUSTER.mongodb.net/YOUR_DB?retryWrites=true&w=majority'
    }

MockConfig (Testing):

class MockConfig:
    MONGODB_DB = 'users_test'
    MONGODB_HOST = 'localhost'
    MONGODB_PORT = 27018
    MONGODB_USERNAME = 'admin'
    MONGODB_PASSWORD = 'admin'

🚀 How to Run the Application
The application listens on port 5001 by default, as defined in wsgi.py and docker-compose.yml.

Option 1: Using Docker Compose (Recommended for Easy Development)
For Development Environment (MongoDB via Docker):
The docker-compose.yml is configured by default for the development environment.

docker-compose up --build

The API will be accessible at http://localhost:5001.

For Production Environment (MongoDB Atlas via Docker):

Ensure your ProdConfig in config.py is correct.

Edit the docker-compose.yml file and change the environment variable for the api service:

services:
  api:
    # ... other configurations ...
    environment:
      - FLASK_DEBUG=0 # Recommended for production
      - FLASK_ENV=production # Change to production
      # The MONGODB_* variables below are for DevConfig and will not be used by ProdConfig
      # - MONGODB_DB=users
      # - MONGODB_HOST=mongodb
      # ...

Run:

docker-compose up --build

(Optional: You can remove the mongodb service and depends_on from docker-compose.yml if you plan to exclusively use Atlas in this mode).

Option 2: Local Execution (Without Docker)
For Development Environment:

On Linux/macOS:

export FLASK_ENV=development # or can be omitted, as it's the default
python wsgi.py

On Windows (PowerShell):

$env:FLASK_ENV="development"
python wsgi.py

On Windows (CMD):

set FLASK_ENV=development
python wsgi.py

For Production Environment:

On Linux/macOS:

export FLASK_ENV=production
python wsgi.py

On Windows (PowerShell):

$env:FLASK_ENV="production"
python wsgi.py

On Windows (CMD):

set FLASK_ENV=production
python wsgi.py

For Testing Environment:

On Linux/macOS:

export FLASK_ENV=testing
python wsgi.py # Or run tests directly

On Windows (PowerShell):

$env:FLASK_ENV="testing"
python wsgi.py

On Windows (CMD):

set FLASK_ENV=testing
python wsgi.py

🧪 Running Tests
To run the automated test suite with Pytest:

pytest

(Ensure the testing environment (FLASK_ENV=testing) is configured to use the correct test database, usually on port 27018, as per MockConfig).

📖 API Endpoints
GET /

Description: API welcome message.

Response (200 OK): {"message": "Welcome to the API!"}

GET /users

Description: Returns a list of all registered users.

Response (200 OK): Array of user objects. Ex: [{"_id": {"$oid": "..."}, "cpf": "...", "name": "...", ...}]

POST /users

Description: Creates a new user.

Request Body (JSON):

{
  "name": "User Name",
  "last_name": "Lastname",
  "cpf": "123.456.789-00",
  "email": "user@example.com",
  "birth_date": "YYYY-MM-DD"
}

Responses:

200 OK: {"message": "User <user_id> successfully created!"}

400 Bad Request: If CPF is invalid ({"message": "CPF invalid"}) or if CPF already exists ({"message": "CPF already exists in database"}).

GET /user/<string:cpf>

Description: Returns data for a specific user, searched by CPF.

URL Parameter: cpf (Ex: http://localhost:5001/user/123.456.789-00)

Responses:

200 OK: User object.

404 Not Found: {"message": "User not found"}

(Note: The PUT and DELETE endpoints are not implemented in the provided application/app.py code. This README reflects the currently available endpoints.)

🧠 Challenges and Learnings
Dynamic Environment Configuration: One of the main challenges was implementing a configuration system that allowed easy switching between different databases and other environment-specific settings. This was solved with Flask configuration classes and the use of the FLASK_ENV variable.

Integration with MongoEngine and Flask-RESTful: Learning the best way to model data with MongoEngine and expose it efficiently following RESTful patterns with Flask-RESTful was an important part of the learning process.

Data Validation: Implementing CPF validation, including the verifier digit logic, directly in the API.

Dockerization: Configuring Dockerfile and docker-compose.yml to create a consistent development environment and facilitate deployment.

Automated Testing: Developing the habit of writing tests for API endpoints using Pytest, ensuring code reliability.

📈 Next Steps / Future Improvements
Implement authentication and authorization (e.g., JWT) to protect endpoints.

Add endpoints to update (PUT) and delete (DELETE) users.

Improve error handling and feedback to the API client.

Expand test coverage, including more complex integration tests.

Create more interactive API documentation using Swagger/OpenAPI.

Set up a CI/CD (Continuous Integration/Continuous Delivery) pipeline to automate tests and deployments.

Add pagination and filters to the GET /users endpoint.

⚙️ Key Environment Variables
Variable

Possible Values

Description

FLASK_ENV

development, production, testing

Defines which Flask configuration object will be loaded (DevConfig, ProdConfig, MockConfig).

FLASK_DEBUG

0 (off), 1 (on)

Activates or deactivates Flask's debug mode. 0 is recommended for production.

MONGODB_DB, MONGODB_HOST, MONGODB_PORT, MONGODB_USERNAME, MONGODB_PASSWORD

(strings, int)

Used by DevConfig and MockConfig to connect to MongoDB, can be overridden by environment variables with the same name.

📝 Important Notes
The default application port is 5001, aligned with the docker-compose.yml configuration.

The init_db function in application/db.py is designed to automatically detect whether to use the Atlas connection string (for ProdConfig) or individual host/port settings (for DevConfig/MockConfig).

For a real production environment, it is crucial to set FLASK_DEBUG=0.

The mongodb service in docker-compose.yml can be removed if you plan to exclusively use MongoDB Atlas, even in development via Docker (by setting FLASK_ENV=production in docker-compose.yml).
