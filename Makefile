version := $(shell python -c 'import tomli; print(tomli.load(open("pyproject.toml", mode="rb"))["project"]["version"])')

.PHONY: activate upload-test upload-production build-sdist build test clean sign check load devel

activate:
	@echo run this: source bin/activate

version:
	@echo $(version)

upload-production: build sign
	python -m twine upload --repository pypi dist/*
	git tag --sign $(version) -m $(version)
	git push origin $(version)

upload-test: build
	python -m twine upload --repository testpypi dist/*

build:
	python -m build

build-sdist:
	python -m build --sdist

sign:
	gpg --detach-sign -a dist/*.tar.gz

check:
	python setup.py check

test:
	python tests/testgetargv.py

clean:
	rm -rf build dist getargv.egg-info src/getargv.egg-info MANIFEST

load:
	python -i src/getargv/load.py

devel:
	pip install --editable .
