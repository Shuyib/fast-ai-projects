venv:
	# create a virtual environment adjust it to a particular python version if you want
	conda create -n fastai-env python=3.9 anaconda

configure-mamba:
	# use the fastsetup do speed this up
	bash setup-conda.sh

activate:
	# activate venv run this manually
	conda activate name_of_path_where

deactivate:
	# deactivate venv run this manually
	conda deactivate 

install:
	# install commands
	# review pytorch website for your distribution
	conda update -n base -c defaults conda &&\
		mamba install pytorch torchvision torchaudio cudatoolkit=11.6 -c pytorch -c conda-forge &&\
		mamba install -c fastchan fastai

start-venv:
	# if the environment.yml is available
	conda env create --file environment.yml --prefix ./venv --quiet

build:
	# build the container: More important for the CI/CD
	docker build -t fastai-env:v1 .
	
run:
	# run the container
	docker run fastai-env:v1
