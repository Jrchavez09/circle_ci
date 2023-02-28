
test:
	virtualenv venv
  . venv/bin/activate
  pip3.11 install -r requirements.txt
  python3.11 -m pytest tests

