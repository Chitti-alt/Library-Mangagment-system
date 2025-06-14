# Library-Mangagment-system
# 📚 Library Management System

A **Library Management System** built in Python with MySQL database integration using the `mysql.connector` module. This system supports secure user login, book classification, and borrowing records.

---

## 🔧 Features

- ✅ **User Authentication**
  - Account-based login system
  - Passwords stored securely using hashing
  - Optional admin and regular user roles

- 📖 **Book Management**
  - Add, update, and delete books
  - Classify books by **Author**, **Genre**, and **Title**
  - View book availability

- 🔍 **Search and Filter**
  - Search by title, author, or genre
  - Sort and filter results

- 🧾 **Borrowing System**
  - Issue and return tracking
  - Borrowing history per user

- 🗄️ **Database Integration**
  - MySQL backend via `mysql.connector`
  - Modular and clean schema design

---

## 🗃️ Database Schema

### `books`
| Column      | Type      | Description             |
|-------------|-----------|-------------------------|
| `book_id`   | INT (PK)  | Unique book ID          |
| `title`     | VARCHAR   | Title of the book       |
| `author`    | VARCHAR   | Author name             |
| `genre`     | VARCHAR   | Genre or category       |
| `available` | BOOLEAN   | Book availability       |

### `users`
| Column      | Type      | Description             |
|-------------|-----------|-------------------------|
| `user_id`   | INT (PK)  | Unique user ID          |
| `username`  | VARCHAR   | Login username          |
| `password`  | VARCHAR   | Hashed user password    |

### `transactions`
| Column        | Type      | Description             |
|---------------|-----------|-------------------------|
| `trans_id`    | INT (PK)  | Unique transaction ID   |
| `user_id`     | INT (FK)  | User who borrowed       |
| `book_id`     | INT (FK)  | Book being borrowed     |
| `borrow_date` | DATE      | Date of issue           |
| `return_date` | DATE      | Date of return (nullable) |

---



