# Habit Tracker API Documentation

**Production Server Endpoint:**
```
https://habit-tracker-879q.onrender.com
```

All API endpoints below are relative to this base URL.

## Authentication

### Register a New User
- **URL:** `/api/register/`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "username": "yourusername",
    "email": "your@email.com",
    "password": "yourpassword"
  }
  ```
- **Response:**
  ```json
  {
    "id": 1,
    "username": "yourusername",
    "email": "your@email.com"
  }
  ```

---

### Login (Obtain JWT Token)
- **URL:** `/api/login/`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "username": "yourusername",
    "password": "yourpassword"
  }
  ```
- **Response:**
  ```json
  {
    "refresh": "refresh_token",
    "access": "access_token"
  }
  ```

---

### Refresh JWT Token
- **URL:** `/api/token/refresh/`
- **Method:** `POST`
- **Body:**
  ```json
  {
    "refresh": "refresh_token"
  }
  ```
- **Response:**
  ```json
  {
    "access": "new_access_token"
  }
  ```

---

### Get Current User Info
- **URL:** `/api/me/`
- **Method:** `GET`
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  {
    "id": 1,
    "username": "yourusername",
    "email": "your@email.com"
  }
  ```

---

## Habits

### List All Habits
- **URL:** `/api/habits/`
- **Method:** `GET`
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  [
    {
      "id": 1,
      "user": 1,
      "name": "Workout",
      "description": "Morning exercise",
      "color": "blue",
      "icon": "heart",
      "created_at": "2024-07-16T08:00:00Z",
      "completed_dates": ["2024-07-16", "2024-07-17"]
    }
  ]
  ```

---

### Create a New Habit
- **URL:** `/api/habits/`
- **Method:** `POST`
- **Headers:** `Authorization: Bearer <access_token>`
- **Body:**
  ```json
  {
    "name": "Study",
    "description": "Read a book",
    "color": "purple",
    "icon": "book"
  }
  ```
- **Response:** Same as list, with the new habit.

---

### Retrieve, Update, or Delete a Habit
- **URL:** `/api/habits/{id}/`
- **Method:** `GET`, `PUT`, `PATCH`, `DELETE`
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:** Same as list, for the specific habit.

---

### Toggle Habit Completion for a Date
- **URL:** `/api/habits/{id}/toggle/`
- **Method:** `POST`
- **Headers:** `Authorization: Bearer <access_token>`
- **Body:** (optional, defaults to today)
  ```json
  {
    "date": "2024-07-16"
  }
  ```
- **Response:**
  ```json
  {
    "status": "completed",
    "date": "2024-07-16"
  }
  ```
  or
  ```json
  {
    "status": "unmarked",
    "date": "2024-07-16"
  }
  ```

---

## Statistics

### Get User Habit Statistics
- **URL:** `/api/habits/statistics/`
- **Method:** `GET`
- **Headers:** `Authorization: Bearer <access_token>`
- **Response:**
  ```json
  {
    "completed_today": 1,
    "total_habits": 2,
    "longest_streak": 1,
    "average_success": 15.0
  }
  ```

--- 