# OBSCENITY_ZERO

This Flask application analyzes web pages for offensive content by fetching the HTML content of a specified URL, processing the text, and checking for predefined offensive keywords.

## Features

- Fetch and analyze web content in real time.
- Simple web interface for submitting URLs for analysis.
- Indicates whether the analyzed content is considered safe or not based on predefined criteria.
- Used Natural Language Tool Kit

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Docker (optional for containerized deployment)

### Installing

1. Clone the repository to your local machine:

    ```sh
    git clone https://github.com/regiin09/OBSCENITY_ZERO.git
    ```

2. We have given both flask and docker




### With Flask :

1. Change your directory

    ```sh
	cd OBSCENITY_ZERO
    ```

2. Install requirements:

    ```sh
	pip install -r requirements.txt
    ```

3. Set the Flask application environment variable:

- In Windows:

	```sh
    set FLASK_APP=app.py
	```

- In Mac/Linux:

	```sh
    export FLASK_APP=app.py
	```

4. Run the Flask application:

	```sh
    flask run
    ```

### Using Docker :

1. Change your directory

    ```sh
	cd OBSCENITY_ZERO
    ```

2. Build the Docker image:

    ```sh
    docker build -t OBSCENITY_ZERO .
    ```

3. Run the application in a Docker container:

	```sh
    docker run -p 5000:5000 OBSCENITY_ZERO
    ```

## Usage

Navigate to `http://localhost:5000` in your web browser.
Enter the URL of the web page you wish to analyze in the provided input field.
Click "Submit" to analyze the web page. You will be redirected to a page indicating whether the content is safe or not.

## Acknowledgments

- Flask for the web framework.
- Python community for the invaluable libraries.
