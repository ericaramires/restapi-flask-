# REST API with Flask, MongoDB, and ID Validation
A robust REST API built with Flask and MongoDB for user management, featuring an advanced CPF (Brazilian individual taxpayer registry) validation system. The application is fully containerized with Docker, has a CI/CD pipeline with GitHub Actions, and follows best practices for security and code organization.

### 🚀 Architecture and Technologies

* **Backend:** Flask, Flask-RESTful
* **Database:** MongoDB
* **ODM (Object-Document Mapper):** MongoEngine
* **Containerization:** Docker, Docker Compose
* **CI/CD0**: GitHub Actions
* **WSGI Server:** Gunicorn
* **Testing:** Pytest

### 🐳 How to Run Locally

Follow the steps below to get the application running on your machine.

**Prerequisites:**
Docker
Docker Compose

**Step-by-step guide:**

1. Clone the repository:

        git clone 
        cd restapi-flask

3. Create the environment variables file:
Create a file named .env in the project root and add the database credentials.

4. Launch the containers:
This command will build the images and start the services in the background.

        docker-compose up --build -d

5. Done!
The API will be accessible at http://localhost:5001.

### 🛠️ API Endpoints
| Method | Endpoint                | Description                               |
| :----- | :---------------------- | :---------------------------------------- |
| `GET`  | `/`                     | Welcome endpoint.                         |
| `GET`  | `/users`                | Lists all registered users.               |
| `POST` | `/users`                | Creates a new user.                       |
| `GET`  | `/user/<string:cpf>`    | Fetches a specific user by their CPF.     |

Example: Creating a new user with curl

        curl -X POST http://localhost:5001/users \
        -H "Content-Type: application/json" \
        -d '{
            "name": "Maria",
            "last_name": "Silva",
            "email": "maria.silva@example.com",
            "cpf": "123.456.789-00",
            "birth_date": "1990-01-15"
        }'

## ⚙️ Structure and Operation

### 🔧 Initialization Flow
The application uses the Factory Pattern (create_app):

1. wsgi.py is the entry point, which loads the environment variables.
2. The FLASK_ENV environment variable determines which configuration to load (DevConfig, ProdConfig, or MockConfig).
3. The create_app() function in application/__init__.py initializes the Flask instance, connects to the database, and registers the API routes.

### 🗄️ Data Model (UserModel)

User data is structured using MongoEngine as follows:

**cpf:** StringField (required, unique)

**name:** StringField (required)

**last_name:** StringField (required)

**email:** EmailField (required)

**birth_date:** DateField (required)


### 🔍 Advanced CPF Validation

The system implements a multi-layered CPF validation to ensure data integrity:

✅ Format: Checks the XXX.XXX.XXX-XX pattern.

✅ Digits: Ensures the CPF contains 11 digits.

✅ Exceptions: Rejects CPFs with all identical digits (e.g., 111.111.111-11).

✅ Algorithm: Validates the check digits using the standard calculation.

✅ Uniqueness: Prevents the registration of a CPF that already exists in the database.


### 🧪 Testing
The project has a complete test suite using pytest to ensure the API's quality and expected functionality.

* **Isolated Environment:** Tests run with MockConfig, using a separate database (users_test) to avoid interfering with development data.
* **Running the tests:** To run the tests manually, execute the following command after launching the containers:

        docker-compose exec api pytest -v

### 🚢 CI/CD Pipeline

The workflow in .github/workflows/other_main.yml automates testing on every push:

1. Sets up an environment with Ubuntu, Python 3.12, and a MongoDB 6.0 service.
2. Defines the necessary environment variables (MONGODB_HOST=localhost) for the test connection.
3. Installs dependencies and runs pytest.
4. The build status is reflected by the badge at the top of this README.

### 🔒 Security Features

* **Environment Variables:** Credentials and sensitive settings are managed outside the code.
* **DB Authentication:** Access to MongoDB is protected by a username and password.
* **Data Validation:** API inputs are strictly validated.
* **Environment Separation:** Distinct configurations for development, testing, and production.
