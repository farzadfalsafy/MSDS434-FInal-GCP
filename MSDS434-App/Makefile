install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py


lint:
	pylint --disable=R,C main.py

All: install lint test
