.PHONY: setup
setup:
	@echo "---- Installing Python Dependencies ----"
	@pip install -r requirements.txt

.PHONY: setup.dev
setup.dev:
	@cp contrib/env-sample .env
	@pip install -r requirements-dev.txt

.PHONY: run
run:
	@echo "---- Running Application ----"
	@PYTHONPATH=./app python ./app/app.py

.PHONY: test
test:
	@echo "---- Running Tests ----"
	@PYTHONPATH=./app python -m unittest tests

.PHONY: clean
clean:
	@echo "---- Cleaning up .pyc files ----"
	@find . -name '*.pyc' -delete
	@echo "---- Cleaned ----"
