
.PHONY: install run test

install:
	pip install -r requirements.txt

run:
	uvicorn src.main:app --reload

test:
	pytest tests/
