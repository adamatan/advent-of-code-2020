.PHONY: check-% test-% test-verbose-% run-% lint-%

check-%: run-% test-% lint-%
	echo

test-%:
	@python -m doctest $*.py

test-verbose-%:
	@python -m doctest -v $*.py

run-%:
	@python $*.py

lint-%:
	@pylint --rcfile .pylintrc $*.py
