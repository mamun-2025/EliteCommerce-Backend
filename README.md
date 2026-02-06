
# EliteCommerce Backend API 🚀

EliteCommerce is a professional-grade, scalable, and decoupled E-commerce backend built with **Django REST Framework (DRF)**.This Project follows industry best practices, including custom user management, JWT authenthication, and a clean architecture.

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework (DRF)
- **Database:** PostgreSQL (Production-ready)
- **Authentication:** JWT (JSON Web Token) via `SimpleJWT`
- **Environment Management:** Pyhton-dotenv
- **Version Control:** Git & Github

## ✨ Core Features (Completed)

- [x] **Decoupled Architecture:** Built to serve data to any frontend (React, Vue, or Mobile).
- [x] **Custom User Model:** Email-based authentication instead of the default username.
- [x] **JWT Authentication:** Secure login system with Access and Refresh tokens.
- [x] **User Profiles:** Protected endpoints to manage user data.
- [x] **PostgreSQL Integration:** Robust and scalable database configuration.
- [x] **Product Management:** Models for Categories, Brands, and Products.
- [x] **Relational Database Design:** One-to-Manay relationships between Categories and Products.
- [x] **Django Admin Integration:** Customized admin panel for easy product entry.
- [x] **API Integration:** Successfully implemented Serializers and views to serve product data JSON format.
- [x] **Media Handling:** Configured django to handle and serve product images.

## ⚙️ Installation & Setup

Follow these steps to run the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mamun-2025/EliteCommerce-Backend
   cd EliteCommerce-Backend

2. **Create Virtual Environment:**
   python -m venv venv
   # activate it (windows)
   .\venv\Scripts\activate

3. **Install Dependencies:**
   pip install -r requirements.txt

4. **Environment Variables:**
   Create a `.env` file in the root directory and add your own credentials. 
   Never share your `.env` file or commit it to GitHub.
   Example `.env` content:
   SECRET_KEY=your_secret_key_here
   DEBUG=True
   DB_NAME=your_db_name
   DB_USER=your_db_user
   DB_PASSWORD=your_db_password
   DB_HOST=localhost
   DB_PORT=5432
      
5. **Run Migrations:**
   python manage.py makemigrations
   python manage.py migrate   

6. **Start the Server:**
   python manage.py runserver

## 📍 API Endpoints

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| POST | `/api/register/` | Register a new user |
| POST | `/api/login/` | Login & get JWT tokens |
| POST | `/api/token/refresh/` | Refresh the access token |
| GET | `/api/profile/` | Get logged-in user details (Required Token) |
| GET | `/api/products/` | List all Products |
| GET | `/api/products/categories/` | List all categories |

## 🏗️ Project Structure

├── apps/
│   └── users/          # Custom User & Auth logic
|   └── products/       # Category, Brand and Product Management
├── core/               # Project settings & URL routing
├── .env                # Secret environment variables (Ignored by Git)
├── .gitignore          # Files to exclude from Git
├── manage.py
└── requirements.txt    # List of dependencies

## 🛡️ Security Best Practices Followed

- Used .env for sensitive data.
- Password hashing using Django's default PBKDF2.
- JWT stateless authentication.
- Proper .gitignore to prevent sensitive data leaks.

Developed with ❤️ by [Mamun-Bepari]