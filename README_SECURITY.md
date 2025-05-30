# Security Configuration

## ⚠️ IMPORTANT: Environment Variables Setup

This project uses environment variables to protect sensitive credentials. Before running in production:

### 1. Create a `.env` file (never commit this file)

```bash
# Create .env file in project root
touch .env
```

### 2. Add your MongoDB Atlas credentials to `.env`

```env
FLASK_ENV=production
MONGODB_URI=mongodb+srv://your_username:your_password@your_cluster.mongodb.net/your_database?retryWrites=true&w=majority&appName=YourApp
```

### 3. Load environment variables

For production deployment, you can use a package like `python-dotenv`:

```bash
pip install python-dotenv
```

Then add to your `wsgi.py` (optional):
```python
from dotenv import load_dotenv
load_dotenv()
```

### 4. Running the application

```bash
# Development (uses local MongoDB)
make dev

# Production (uses MongoDB Atlas - requires .env file)
make prod
```

## 🔒 Security Checklist

- ✅ `.env` files are in `.gitignore`
- ✅ No hardcoded credentials in source code
- ✅ Use environment variables for all sensitive data
- ✅ Never commit real credentials to version control

## 🚨 If you accidentally committed credentials

1. **Immediately rotate/change your MongoDB Atlas password**
2. **Remove the commit from git history** (if possible)
3. **Update your `.env` file** with new credentials 