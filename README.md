# 🛡️ Rate Limiting & Security Middleware (Django)

A Django-based backend security project that implements middleware for request logging, rate limiting, and authentication protection.

This project demonstrates how APIs can be secured using custom middleware, authentication, and request monitoring techniques.

---

## 🚀 Features

### 📊 Request Logging Middleware
- Logs every incoming API request
- Captures IP address, endpoint, HTTP method, and timestamp
- Helps analyze API usage patterns and detect abnormal behavior

---

### ⚡ Rate Limiting Middleware
- Limits number of requests per IP/user
- Prevents API abuse and excessive traffic
- Applied globally across API endpoints

---

### 🔐 JWT Authentication
- Token-based authentication system
- Protects sensitive endpoints like `/api/dashboard/`
- Stateless authentication using JWT

---

### ❌ Failed Login Tracking (Model)
- `FailedLogin` model created
- Stores failed login attempts
- Used as a base for detecting brute-force attacks (logic integration in progress)

---

## 🏗️ Tech Stack

- Django  
- Django REST Framework (if used)  
- JWT Authentication (SimpleJWT / PyJWT)  
- Custom Middleware  
- SQLite (default) / PostgreSQL (optional)  

---

## ⚙️ How It Works

1. Every incoming request passes through middleware  
2. Request data is logged (IP, endpoint, timestamp, method)  
3. Rate limiting rules are applied per user/IP  
4. JWT authentication validates protected endpoints  
5. Failed login attempts are stored for future analysis  

---

## 📁 Project Structure
security_engine/
│
├── security/                # Main app (rate limiting, logging, failed login tracking, etc.)
│   ├── middleware/          # Request logging + rate limiting middleware
│   ├── migrations/          # Database migrations
│   ├── models.py            # FailedLogin model and other DB models
│   ├── views.py             # API endpoints
│   ├── urls.py              # App routes
│   ├── admin.py             # Django admin configuration
│   └── apps.py              # App configuration
│
├── security_engine/         # Project configuration folder
│   ├── settings.py          # Django settings
│   ├── urls.py              # Project-level routing
│   ├── asgi.py
│   ├── wsgi.py
│   └── __init__.py
│
├── manage.py                # Django project entry point
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

---

## ▶️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Gowrilakshmir12/Rate_limiting_security_middleware.git

# Move into project directory
cd Rate_limiting_security_middleware

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver
```

## 📌 Current Scope

This project is currently in a foundation stage focused on building backend security infrastructure using Django middleware.

### Implemented Features:
- Middleware-based request logging
- IP-based rate limiting system
- JWT authentication for protected routes
- Failed login tracking model (structure implemented)

### Key Focus:
- Understanding how backend security layers work
- Learning middleware flow in Django
- Building reusable security components for APIs

## 🔮 Future Improvements

This project is designed to be extensible and can be enhanced into a full-scale security system.

### Planned Features:
- Smart brute-force attack detection system
- Automatic IP blacklisting and unblocking mechanism
- Redis-based distributed rate limiting for scalability
- Real-time security alerts (Email / Slack integration)
- Admin dashboard for monitoring API traffic and threats
- Behavioral anomaly detection system for suspicious activity

## 🎯 Purpose of This Project

The purpose of this project is to understand and implement backend security concepts in real-world API systems using Django.

It demonstrates how modern backend systems handle:

- API request monitoring
- Traffic control using rate limiting
- Authentication and authorization (JWT)
- Logging and auditing of requests
- Basic security and abuse prevention mechanisms

This project acts as a foundation for building production-level security systems and scalable backend architectures.
