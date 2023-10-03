version := $(shell python -c 'import tomli; print(tomli.load(open("pyproject.toml", mode="rb"))["project"]["version"])')

.PHONY: activate db version upload-production upload-test build build-sdist sign check test clean console load devel docs

activate:
	@echo run this: source bin/activate

db: compile_commands.json

compile_commands.json:
	bear -- python setup.py build

version:
	@echo $(version)

upload-production: build sign
	python -m twine upload --repository pypi dist/*$(version)*
	git tag --sign $(version) -m $(version)
	git push origin $(version)

upload-test: build
	python -m twine upload --repository testpypi dist/*$(version)*

build:
	python -m build

build-sdist:
	python -m build --sdist

sign:
	gpg --detach-sign -a dist/*.tar.gz

check:
	python setup.py check

types:
	pyright --verifytypes getargv
	pyright

test: devel
	python tests/testgetargv.py

clean:
	rm -rf build dist getargv.egg-info src/getargv.egg-info MANIFEST src/_getargv.cpython-*-darwin.so

console load: devel
	python -ic 'import getargv'

devel:
	pip install --editable .

getargv.html: devel
	python -m pydoc -w getargv

docs: getargv.html
