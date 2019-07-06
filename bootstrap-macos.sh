brew install python3
brew install pyenv
pyenv install 2.7.16
pyenv install 3.4.10
pyenv install 3.5.7
pyenv install 3.6.8
pyenv install 3.7.3
pyenv local 3.7.3 2.7.16 3.6.8 3.5.7 3.4.10
pip3 install -r dev-requirements.txt
tox
