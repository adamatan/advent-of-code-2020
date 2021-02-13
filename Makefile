.PHONY: check-% test-% test-verbose-% run-% lint-%

check-%: run-% lint-% test-%
	echo

test-%:
	@python -m doctest $*.py

test-verbose-%:
	@python -m doctest -v $*.py

run-%:
	@python $*.py

lint-%:
	@pylint --rcfile .pylintrc $*.py
