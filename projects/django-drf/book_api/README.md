# Book Management API Practice Project

This project is a hands-on exercise to build a RESTful API for managing a collection of books. It's designed to help solidify understanding of Django, Django REST Framework (DRF), and related web development concepts.

## Technologies Used

- **Django:** A high-level Python web framework.
- **Django REST Framework (DRF):** A powerful and flexible toolkit for building Web APIs.
- **PostgreSQL:** As the database (though Django's default SQLite is sufficient for initial practice).
- **drf-spectacular:** For API documentation.
- **django-filter:** For API filtering.
- **djangorestframework-simplejwt:** For JWT authentic
- **Testing:** Using DRF's testing tools.

## Project Features (Currently Implemented)

- **CRUD Operations for Books:**
  - **Create:** Add new book records to the database (POST to `/api/books/`).
  - **Read (List):** Retrieve a list of all books (GET to `/api/books/`).
  - **Read (Detail):** Retrieve details of a specific book by its ID (GET to `/api/books/<id>/`).
  - **Update:** Modify existing book records (PUT/PATCH to `/api/books/<id>/`).
  - **Delete:** Remove book records from the database (DELETE to `/api/books/<id>/`).
- **Browsable API:** Django REST Framework's interactive web interface for easy API exploration and testing.
- **Custom Management Command:** `populate_books` command to add initial sample book data to the database (`python manage.py populate_books`).

## Future Features (Planned)

- **Filtering:** Allow filtering of books based on criteria like author, publication year, etc.
- **Pagination:** Implement pagination for the book list to handle large datasets.
- **Ordering:** Enable sorting of books based on different fields.
- **Search:** Add a search functionality for books.
- **Permissions:** Control access to API endpoints based on user roles or authentication status.
- **Book Reviews:** Implement a system for users to add and view reviews for books.
- **User Authentication:** Secure the API with user authentication.
- **API Documentation:** Generate automatic API documentation using `drf-spectacular`.
- **Testing:** Write unit and integration tests for the API.
- **Containerization:** Use Docker for easier setup and deployment.
- **Dependency Management:** Use Poetry for managing project dependencies.

## Setup Instructions

1.  **Clone the repository:**

    ```bash
    git clone <your_repository_url>
    cd <your_project_directory>
    ```

2.  **Create a virtual environment (recommended):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # On macOS/Linux
    venv\Scripts\activate  # On Windows
    ```

3.  **Install dependencies:**

    ```bash
    pip install django djangorestframework
    # (Install other dependencies as we add features, e.g., django-filter, drf-spectacular)
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for Django Admin):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**

    ```bash
    python manage.py runserver
    ```

7.  **Access the API:** Open your browser or a tool like `curl` to interact with the API endpoints (e.g., `http://127.0.0.1:8000/api/books/`).

## Custom Management Command

To populate the database with initial book data, run:

```bash
python manage.py populate_books
```
