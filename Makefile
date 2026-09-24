
.PHONY: build run stop test clean

# Build the Docker image
build:
	docker build -t dice-roller .

# Run the Dice Roller container
run:
	docker run --rm -p 8000:8000 --name dice-roller-container dice-roller