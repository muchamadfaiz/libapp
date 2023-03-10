build-prod:
	docker compose -f docker-compose-prod.yml build --no-cache

upd:
	docker compose -f docker-compose-prod.yml up -d

up:
	docker compose -f docker-compose-prod.yml up

shell-prod:
	docker compose -f docker-compose-prod.yml exec web bash

makemigrations:
	docker compose -f docker-compose-prod.yml exec web su -c "python manage.py makemigrations --settings=core.settings.production"

migrate:
	docker compose -f docker-compose-prod.yml exec web su -c "python manage.py migrate --settings=core.settings.production"

destroy:
	docker compose -f docker-compose-prod.yml down

createsuperuser:
	docker compose -f docker-compose-prod.yml exec web su -c "python manage.py createsuperuser --settings=core.settings.production"