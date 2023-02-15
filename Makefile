dev:
	poetry run uvicorn app.main:app --port 8000 --reload

test:
	poetry run pytest -vv

generate_req:
	poetry export -f requirements.txt -o requirements.txt --without-hashes
