PYTHON ?= python
PINOCCHIO ?= $(PYTHON) -mpinocchio
EXAMPLE_SOURCES=$(filter-out %-test.c, $(wildcard examples/*.c))
EXAMPLE_OUTPUTS=$(subst examples/,build/,$(basename $(EXAMPLE_SOURCES)))


#######################################################################


all: $(addsuffix .arith,$(EXAMPLE_OUTPUTS))


#######################################################################


build:
	mkdir -p $@

build/%.dot: build/%.arith
	PYTHONPATH=. python -mpinocchio.drawcircuit --arith $< --out $@

build/%.arith: examples/%.c build
	$(PINOCCHIO) --cpparg _I $(dir $<) --arith $@ $<

build/%.json: examples/%.c build
	$(PINOCCHIO) --json $@ $<


#######################################################################


clean: python-clean

lint: python-pyflakes python-pylint

python-pyflakes:
	$(PYTHON) -mpyflakes pinocchio

python-clean:
	find . -name '*.pyc' -exec rm -f '{}' ';'
	find . -name '__pycache__' -exec rm -rf '{}' ';'

python-pylint:
	$(PYTHON) -mpylint pinocchio || true
