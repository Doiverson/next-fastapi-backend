```
___________                __     _____ __________.___ 
\_   _____/____    _______/  |_  /  _  \\______   \   |
 |    __) \__  \  /  ___/\   __\/  /_\  \|     ___/   |
 |     \   / __ \_\___ \  |  | /    |    \    |   |   |
 \___  /  (____  /____  > |__| \____|__  /____|   |___|
     \/        \/     \/               \/              
```
# Backend Project

This is the backend for our application, built with Python and FastAPI.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.8+
- Docker
- Docker Compose

### Additional Tools
We recommend installing [Postman](https://www.postman.com/)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/Doiverson/next-fastapi-backend.git
    ```

2. Navigate to the `backend` directory:
    ```bash
    cd backend
    ```

3. Build and run the Docker containers:
    ```bash
    docker-compose up --build
    ```

The application should now be running at `http://localhost:8000`.
pgAdmin should now be running at `http://localhost:5433`

## API Documentation

You can view the API documentation at `http://localhost:8000/docs` when the server is running.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.
