.PHONY: help test

help:
	@echo "make test    - run pytest"

test:
	python -m pytest -q
