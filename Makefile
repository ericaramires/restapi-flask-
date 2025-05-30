APP = restapi

dev:
	set FLASK_ENV=development && python wsgi.py

prod:
	@echo "Make sure you have created a .env file with MONGODB_URI=your_atlas_connection_string"
	set FLASK_ENV=production && python wsgi.py

test:
	pytest -v --disable-warnings

compose:
	docker-compose build
	docker-compose up


	

