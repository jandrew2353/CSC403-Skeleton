# Dice Roller 🎲

A simple dice roller web service built with Python and FastAPI for the CSC 4033 Software Engineering project skeleton.

The application allows users to roll a die with a chosen number of sides and returns a randomly generated result.

## Features

* FastAPI web service with two endpoints.
* Roll a die with 2 to 100 sides.
* Error handling for invalid dice rolls.
* Automatic API documentation.
* Docker container support.
* Automated testing using GitHub Actions.

## Technologies Used

* Python
* FastAPI
* Docker
* GitHub Actions
* Pytest

## API Endpoints

### 1. Server Status

**GET /**

Checks whether the Dice Roller service is running.

Example response:

```json
{
  "service": "Dice Roller",
  "status": "running"
}
```

### 2. Roll Dice

**GET /roll?sides=6**

Rolls a die with the specified number of sides.

Example response:

```json
{
  "sides": 6,
  "result": 4
}
```

The result is a random number between 1 and the number of sides.

The number of sides must be between 2 and 100.

An invalid request, such as `/roll?sides=0`, returns HTTP status code 400 with the following response:

```json
{
  "detail": "Sides must be between 2 and 100"
}
```

## Running the Application Locally

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Start the FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Open your browser and visit:

http://localhost:8000

## Running with Docker

Build the Docker image:

```bash
docker build -t dice-roller .
```

Run the Docker container:

```bash
docker run --rm -p 8000:8000 dice-roller
```

Open http://localhost:8000 to access the application.

Press Ctrl + C in the terminal to stop the container.

## API Documentation

FastAPI automatically generates interactive API documentation.

Visit:

http://localhost:8000/docs

The documentation lists the available endpoints and allows users to test requests directly in their browser.

## Automated Testing

The project uses Pytest to test the Dice Roller service.

Run the tests locally:

```bash
python -m pytest test_main.py -v
```

The tests verify that:

* The server responds correctly.
* A six-sided die returns a result between 1 and 6.
* A twenty-sided die returns a result between 1 and 20.
* Invalid dice rolls return HTTP status code 400.

## GitHub Actions

GitHub Actions automatically runs the project's CI workflow whenever code is pushed to the repository or a pull request is opened or updated.

The workflow:

1. Checks out the repository.
2. Sets up Python.
3. Installs the required dependencies.
4. Runs the Dice Roller automated tests.
5. Builds the Docker image.

This helps verify that the Dice Roller application continues to work after code changes.

## Project Purpose

This project was created as a skeleton for CSC 4033 Software Engineering.

It demonstrates a working HTTP service, multiple API endpoints, error handling, API documentation, automated testing, and Docker containerization.
