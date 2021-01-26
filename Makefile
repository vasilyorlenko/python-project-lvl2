install:
	poetry install

gendiff:
	poetry run gendiff

build:
	rm -rf dist
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python -m pip install --user dist/*.whl

test:
	poetry run python -m pytest

test-coverage:
	poetry run python -m pytest --cov=gendiff tests/ --cov-report xml

lint:
	poetry run flake8 gendiff