all: build

.PHONY: clean
clean:
	@rm -rf dist

.PHONY: build
build:
	python setup.py sdist

.PHONY: pack
pack: build
	@cp task.json dist/
	zip dist/sendmsg.zip dist/* -j
