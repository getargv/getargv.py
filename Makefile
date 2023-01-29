.PHONY: activate upload-test upload-production build-local build-sdist build test clean sign check load

activate:
	@echo run this: source bin/activate

upload-production: build sign
	python -m twine upload --repository pypi dist/*

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

build-local:
	python setup.py build
	python setup.py install

test:
	python tests/testgetargv.py

clean:
	rm -rf build dist getargv.egg-info src/getargv.egg-info MANIFEST

load: build-local
	python -i src/getargv/load.py

devel:
	pip install --editable .
