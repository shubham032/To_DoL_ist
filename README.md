# 📝  To_DoL_ist

A simple **Task Management System** built with Django that allows users to sign up, log in, create, update, and delete tasks. This project demonstrates the use of Django's authentication system and CRUD operations.

---

## 🚀 Features

- 🔐 **User Authentication**: 
  - Sign up, log in, and log out functionality.
  - Password validation and error handling.

- ✅ **Task Management**:
  - Add tasks with a name and description.
  - Update or delete tasks.
  - Tasks are user-specific.

- 🎨 **Responsive UI**:
  - Styled with basic HTML and inline CSS for simplicity.

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/shubham032/To_DoL_ist.git
   cd To_DoL_ist
2.Set up a virtual environment:
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install dependencies:
   pip install django
4.Run migrations:
   python manage.py makemigrations
   python manage.py migrate
5.Start the development server:
  python manage.py runserver

## 📂 Project Structure
todolist/
├── auth_system/
│   ├── templates/
│   │   ├── [login.html]
│   │   ├── [signup.html]
│   ├── [views.py]
│   ├── [urls.py]
├── Task/
│   ├── templates/
│   │   ├── [home.html]
│   │   ├── [update.html]
│   ├── [models.py]
│   ├── [views.py]
│   ├── [urls.py]
├── todolist/
│   ├── [settings.py]
│   ├── [urls.py]
│   ├── wsgi.py

## 🧑‍💻 Usage
1.Sign Up:

- Navigate to the sign-up page and create an account.
2.Log In:

- Log in with your credentials.
3.Manage Tasks:

- Add, update, or delete tasks.
4.Log Out:

- Click the logout button to end your session.

## ⚙️ Configuration
- Database: SQLite (default Django database).
- Static Files: Ensure STATIC_URL is configured in settings.py.

## 🤝 Contributing
Contributions are welcome! Feel free to fork the repository and submit a pull request.

## 📜 License
This project is licensed under the MIT License. See the LICENSE file for details.

## 💡 Acknowledgments
Django Documentation
Icons from Font Awesome

## 🛡️ Disclaimer
This project is for educational purposes only. Do not use it in production without proper security measures.

