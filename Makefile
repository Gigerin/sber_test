pylint:
	poetry run pylint .

pytest:
	poetry run pytest --cov=. .

build:
	docker build -t sber_image .

up:
	docker run --name sber_test -p 5000:5000 sber_image