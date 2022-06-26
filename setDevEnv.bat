:: Basic Environment variables for dev work
SETX FLASK_ENV development
:: Setup database
SETX DATABASE_URL postgresql://postgres:postgres@localhost/template-repo-database
SETX SECRET_KEY someSecret
