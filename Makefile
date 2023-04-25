# Define the Python interpreter to use
PYTHON_INTERPRETER = python3

# Define the name of the virtual environment
VENV_NAME = venv

# Define the name of the Flask app module
FLASK_APP = app.py

# Define the port number to use
PORT = 8080

# Create a virtual environment
install:
	pip install -r requirements.txt

# Start the Flask app
run:
	. FLASK_APP=$(FLASK_APP) flask run --port $(PORT)

# Run the unit tests
# test:
	# . $(VENV_NAME)/bin/activate && python -m unittest discover -s tests

# Start the load test
# load_test:
	# . $(VENV_NAME)/bin/activate && locust -f locustfile.py --host=http://localhost:$(PORT)

# Clean up
# clean:
	# rm -rf $(VENV_NAME) __pycache__ .pytest_cache

# .PHONY: venv run test load_test clean
