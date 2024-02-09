# Django Age Guesser API

This Django project is an API that guesses the age of a person by their name using the Agify API. It provides an endpoint `/api/human-age` to fetch the age and date of birth of a person based on their name.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Temitopesam1/django-age-guesser.git

2. Navigate to the project directory:
    ```bash
    cd django-age-guesser

3. Install dependencies using pip:
    ```bash
    pip install -r requirements.txt

## Usage

1. Start the Django development server:
    ```bash
    python manage.py runserver

2. Make POST requests to the /api/human-age endpoint with the name parameter to fetch the age and date of birth of a person.

    Example request:
        ```bash
        curl -X POST http://localhost:8000/api/human-age -d '{"name": "Michael"}' -H 'Content-Type: application/json'

    Example response:
        ```bash
        {
            "name": "Michael",
            "age": 63,
            "date_of_birth": "1958-01-01"
        }

## Testing

Run tests for the project:
    ```bash
    python manage.py test

## Deployment

1. Build the Docker image:
    ```bash
    docker-compose build

2. Start the Docker containers:
    ```bash
    docker-compose up

## Contributing

Contributions are welcome! Please fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
