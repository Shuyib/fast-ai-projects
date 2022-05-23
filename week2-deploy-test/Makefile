install:
	#install commands
	pip install --upgrade pip &&\
		pip install -r requirements.txt

clean-dir:
	rm -rf /root/.cache

format:
	#format code
	black *.py mylib/*.py

lint:
	#flake8 or #pylint
	pylint --disable=R,C *.py mylib/*.py

test:
	#test
	#python -m pytest -vv --cov=mylib --cov=main test_*.py

scripts:
	# run scripts
	python main.py

build:
	#build container
    docker build -t generate_data:v0 .
	
run:
	#run docker

deploy:
	#deploy

all: install format lint test deploy