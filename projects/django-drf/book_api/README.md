# Book Management API Practice Project

This project is a hands-on exercise to build a RESTful API for managing a collection of books. It's designed to help solidify understanding of Django, Django REST Framework (DRF), and related web development concepts.

## Technologies Used

- **Django:** A high-level Python web framework.
- **Django REST Framework (DRF):** A powerful and flexible toolkit for building Web APIs.
- **(Potentially) PostgreSQL:** As the database (though Django's default SQLite is sufficient for initial practice).
- **drf-spectacular:** For API documentation.
- **django-filter:** For API filtering.
- **djangorestframework-simplejwt:** For JWT authentication.
- **Testing:** Using DRF's testing tools.

## Project Features (Currently Implemented)

- **CRUD Operations for Books:**
  - **Create:** Add new book records (POST to `/api/v1/books/` - requires authentication).
  - **Read (List):** Retrieve a list of all books (GET to `/api/v1/books/`). Supports pagination and filtering.
  - **Read (Detail):** Retrieve details of a specific book by its ID (GET to `/api/v1/books/<id>/`).
  - **Update:** Modify existing book records (PUT/PATCH to `/api/v1/books/<id>/` - requires authentication).
  - **Delete:** Remove book records (DELETE to `/api/v1/books/<id>/` - requires authentication).
- **Browsable API:** Django REST Framework's interactive web interface for easy API exploration and testing.
- **Custom Management Command:** `populate_books` command to add initial sample book data to the database (`python manage.py populate_books`).
- **Filtering:** Ability to filter books by `title`, `author`, `publication_year`, `publication_date` (greater than/less than), `isbn`, and presence of `publication_date`.
- **Pagination:** Results for the book list are paginated (default page size: 10, configurable via `?page=<number>` and optionally `?size=<number>`).
- **Search:** Ability to search books by keywords in `title` and `summary` using the `?search=<term>` query parameter.
- **Permissions:** Only authenticated users can create, update, and delete books. Read operations are allowed for everyone.
- **JWT Authentication:** Secure API access using JSON Web Tokens.

## API Endpoints

- `/api/v1/books/`:
  - `GET`: List all books (supports filtering, search, and pagination).
  - `POST`: Create a new book (requires a valid JWT token in the `Authorization` header).
- `/api/v1/books/<id>/`:
  - `GET`: Retrieve details of a specific book.
  - `PUT`, `PATCH`: Update a specific book (requires a valid JWT token).
  - `DELETE`: Delete a specific book (requires a valid JWT token).
- `/api/token/`:
  - `POST`: Obtain a new access and refresh token by providing valid username and password in the request body (JSON format: `{"username": "your_username", "password": "your_password"}`).
- `/api/token/refresh/`:
  - `POST`: Obtain a new access token using a valid refresh token in the request body (JSON format: `{"refresh": "your_refresh_token"}`).

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
    pip install django djangorestframework django-filter djangorestframework-simplejwt
    ```

4.  **Apply migrations:**

    ```bash
    python manage.py migrate
    ```

5.  **Create a superuser (for Django Admin and initial API testing):**

    ```bash
    python manage.py createsuperuser
    ```

6.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Interacting with the API

### Obtaining JWT Tokens

1.  Use a tool like `curl`, Postman, or Insomnia.
2.  Send a `POST` request to `http://127.0.0.1:8000/api/token/` with the following JSON body:
    ```json
    {
      "username": "your_username",
      "password": "your_password"
    }
    ```
    (Replace `your_username` and `your_password` with the credentials of a user you created).
3.  The response will contain `access` and `refresh` tokens.

### Making Authenticated Requests

1.  For requests that require authentication (creating, updating, deleting books), you need to include the `access` token in the `Authorization` header of your HTTP request.
2.  The header should be in the format: `Authorization: Bearer <your_access_token>` (replace `<your_access_token>` with the actual token you obtained).

**Example using `curl` to create a book (requires authentication):**

```bash
curl -X POST \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflflzJ6zF1iVYGzGT4-9q1j9-zJ7z-zJ7z-zJ7z-zJ7z' \
  -d '{
    "title": "New Book Title",
    "author": "New Author"
  }' \
  [http://127.0.0.1:8000/api/v1/books/](http://127.0.0.1:8000/api/v1/books/)
```
