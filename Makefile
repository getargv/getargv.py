.PHONY: activate upload-test upload-production build-local build test

activate:
	@echo run this: source bin/activate

upload-production: build sign
	python -m twine upload --repository pypi dist/*

upload-test: build
	python -m twine upload --repository testpypi dist/*

build:
	python -m build

sign:
	gpg --detach-sign -a dist/*.tar.gz

build-local:
	python setup.py build
	python setup.py install

test:
	python tests/testgetargv.py
