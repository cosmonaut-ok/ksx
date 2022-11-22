PYTHON ?= python
USE_VENV ?= "yes"
TMPDIR := $(shell if test -f .venvdir; then cat .venvdir; else mktemp -u /tmp/.ksx_XXXXXX; fi)
PYBIN := $(shell if test ${USE_VENV} = "yes"; then echo ${TMPDIR}/bin/python; else echo ${PYTHON}; fi)
THISDIRNAME=$(shell basename $(PWD))
DISTDIR := dist
TARGETDIR := target
PYTHONPATH := $(PYTHONPATH):$(shell realpath -P .)

## prepare python virtualenv
.venv:
	if test ${USE_VENV} = "yes"; then \
		echo $(TMPDIR) > .venvdir; \
		test -d $(TMPDIR) || $(PYTHON) -m venv $(TMPDIR); \
	fi

.deps:
	$(PYBIN) -m pip install nuitka orderedset

all: .venv .deps
	mkdir -p $(TARGETDIR)/ksx/bin $(TARGETDIR)/ksx/etc
	sed 's/^am_i_bin.*/am_i_bin\ =\ True/g' ksx > bin/ksx # change to True before compilation
	for i in `ls bin`; do \
		$(PYBIN) -m nuitka bin/$$i \
			--standalone \
			--follow-imports \
			--output-dir=$(TARGETDIR) \
			--remove-output \
			--plugin-disable=tk-inter \
			--include-module=site; \
		cp -r -f -n $(TARGETDIR)/$${i}.dist/* $(TARGETDIR)/ksx; \
		ln -sf ../$${i} $(TARGETDIR)/ksx/bin/; \
	done
	cp ksx.json $(TARGETDIR)/ksx/etc

dist:
	cd $(TARGETDIR) && tar -cvzpf ksx.tar.gz ksx
	mv $(TARGETDIR)/ksx.tar.gz .

# python:
# 	wget https://github.com/indygreg/python-build-standalone/releases/download/20210724/cpython-3.8.11-x86_64-unknown-linux-musl-noopt-20210724T1424.tar.zst -O /tmp/.cpython.tar.zst
# 	tar -xvf /tmp/.cpython.tar.zst

clean:
	rm -rf $(TARGETDIR) __pycache__

link:
	if test -d bin; then cd bin && for i in `ls`; do sudo echo ln -sf $$PWD/$$i /usr/local/bin/$$i; done; fi
