.PHONY: flake8
flake8:
	flake8 . --config=setup.cfg --exit-zero

.PHONY: pip-compile
pip-compile:
	pip-compile requirements/requirements.in

.PHONY: pip-sync
pip-sync:
	pip-sync requirements/requirements.txt

.PHONY: pytest
pytest:
	pytest --cache-clear -vv --disable-pytest-warnings --tb=long --color=yes
