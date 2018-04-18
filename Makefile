.PHONY: setup
setup:
	@echo "---- Installing Python Dependencies ----"
	@pip install -r requirements.txt

.PHONY: setup.dev
setup.dev:
	@cp contrib/env-sample .env
	@pip install -r requirements-dev.txt

.PHONY: test
test:
	@echo "---- Running Tests ----"
	@PYTHONPATH=./app python -m unittest tests

.PHONY: clean
clean:
	@echo "---- Cleaning up .pyc files ----"
	@find . -name '*.pyc' -delete
	@echo "---- Cleaned ----"

.PHONY: run
run:
	@echo "---- Running Application ----"
	@PYTHONPATH=./app python ./app/app.py

.PHONY: run.docker
run.docker:
	@echo "---- Running Application With Docker ----"
	@docker swarm init
	@docker stack deploy -c docker-compose.yml apptornadoskeleton

.PHONY: run.docker
kill.docker:
	@echo "---- Kill Application With Docker ----"
	@docker swarm leave --force
	@docker stack rm apptornadoskeleton

.PHONY: conn.postgres.dev
conn.postgres.dev:
	@echo "---- Connect Dev PostgreSQL ----"
	@psql -h 127.0.0.1 -U postgres postgres

.PHONY: migrations
migrations:
	alembic upgrade head
