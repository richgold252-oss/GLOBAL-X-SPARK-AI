# GLOBAL X SPARK AI

**The World's Leading AI Business Intelligence Operating System**

[![Python 3.13](https://img.shields.io/badge/Python-3.13-blue)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-green)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-Latest-black)](https://nextjs.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Latest-336791)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-Latest-2496ED)](https://www.docker.com/)

---

## 🎯 Mission

GLOBAL X SPARK AI helps businesses discover opportunities, research companies, analyze markets, generate personalized outreach, automate business workflows, and accelerate revenue growth through enterprise-grade AI intelligence.

---

## 🏗️ Architecture Overview

This is a **production-ready, enterprise-scale AI SaaS platform** built with:

### Backend
- **Python 3.13** with **FastAPI**
- **SQLAlchemy ORM** for data persistence
- **Pydantic** for data validation
- **JWT & API Key** authentication
- **PostgreSQL** database
- **Redis** for caching
- **Alembic** for database migrations

### Frontend
- **Next.js** with React & TypeScript
- **Tailwind CSS** for styling
- **shadcn/ui** for enterprise components
- **Responsive design** for all devices

### Infrastructure
- **Docker & Docker Compose** for containerization
- **GitHub Actions** for CI/CD
- **Structured logging & error handling**
- **Security by default** (input validation, rate limiting, audit logs)

---

## 📁 Project Structure

```
global-x-spark-ai/
├── backend/                 # Python FastAPI application
│   ├── app/
│   │   ├── api/            # API endpoints (v1)
│   │   ├── core/           # Configuration, security, logging
│   │   ├── db/             # Database connection & session
│   │   ├── models/         # SQLAlchemy ORM models
│   │   ├── schemas/        # Pydantic schemas
│   │   ├── services/       # Business logic layer
│   │   ├── middleware/     # Auth, logging, error handling
│   │   └── main.py         # FastAPI application entry point
│   ├── migrations/         # Alembic database migrations
│   ├── tests/              # pytest test suite
│   ├── requirements.txt    # Python dependencies
│   ├── .env.example        # Environment variables template
│   └── Dockerfile          # Backend container
│
├── frontend/               # Next.js React application
│   ├── public/             # Static assets
│   ├── src/
│   │   ├── components/     # React components
│   │   ├── pages/          # Next.js pages
│   │   ├── hooks/          # Custom React hooks
│   │   ├── utils/          # Helper functions
│   │   ├── styles/         # Global styles
│   │   └── context/        # React context (auth, theme)
│   ├── next.config.js      # Next.js configuration
│   ├── tailwind.config.js  # Tailwind configuration
│   ├── package.json        # Node dependencies
│   └── Dockerfile          # Frontend container
│
├── database/               # Database schema & migrations
│   └── init.sql            # Initial schema
│
├── docker/                 # Docker configuration
│   ├── docker-compose.yml  # Multi-container orchestration
│   └── docker-compose.prod.yml  # Production configuration
│
├── .github/
│   └── workflows/          # CI/CD pipelines
│       ├── backend-test.yml
│       ├── frontend-test.yml
│       └── deploy.yml
│
├── docs/                   # Documentation
│   ├── ARCHITECTURE.md     # Technical architecture
│   ├── API.md              # API documentation
│   └── DEVELOPMENT.md      # Development guide
│
├── scripts/                # Utility scripts
│   ├── setup.sh            # Initial setup
│   ├── seed-db.py          # Database seeding
│   └── migrate.sh          # Database migrations
│
└── README.md               # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- Python 3.13 (for local development)
- Node.js 18+ (for frontend)
- PostgreSQL 15+ (if running locally)

### Using Docker Compose (Recommended)

```bash
# Clone the repository
git clone https://github.com/richgold252-oss/global-x-spark-ai.git
cd global-x-spark-ai

# Copy environment variables
cp backend/.env.example backend/.env

# Start all services
docker-compose -f docker/docker-compose.yml up -d

# Run migrations
docker-compose -f docker/docker-compose.yml exec backend python -m alembic upgrade head
```

**Access:**
- 🌐 Frontend: http://localhost:3000
- 🔌 API: http://localhost:8000
- 📚 API Docs: http://localhost:8000/docs
- 📊 ReDoc: http://localhost:8000/redoc

### Local Development (Backend)

```bash
cd backend

# Create virtual environment
python3.13 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup database
alembic upgrade head

# Start development server
uvicorn app.main:app --reload
```

### Local Development (Frontend)

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

---

## 🔐 Authentication

The platform supports multiple authentication methods:

### 1. JWT Authentication
```bash
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh
```

### 2. API Key Authentication
```bash
POST /api/v1/auth/api-key/generate
Header: Authorization: Bearer <api-key>
```

### 3. Role-Based Access Control (RBAC)
- **Admin**: Full system access
- **Manager**: Team management & resource creation
- **User**: Basic access to assigned resources
- **Guest**: Read-only access

---

## 📋 API Endpoints

### Health Check
```bash
GET /health
```

### Authentication
```bash
POST /api/v1/auth/register
POST /api/v1/auth/login
POST /api/v1/auth/refresh
POST /api/v1/auth/logout
POST /api/v1/auth/api-key/generate
```

### User Management
```bash
GET /api/v1/users/profile
PUT /api/v1/users/profile
GET /api/v1/users/{user_id}
DELETE /api/v1/users/{user_id}
```

### Organizations
```bash
POST /api/v1/organizations
GET /api/v1/organizations
GET /api/v1/organizations/{org_id}
PUT /api/v1/organizations/{org_id}
DELETE /api/v1/organizations/{org_id}
```

### Teams
```bash
POST /api/v1/teams
GET /api/v1/teams
GET /api/v1/teams/{team_id}
PUT /api/v1/teams/{team_id}
DELETE /api/v1/teams/{team_id}
```

### Business Intelligence
```bash
POST /api/v1/companies/research
GET /api/v1/executives/search
POST /api/v1/prospects/analyze
GET /api/v1/reports/{report_id}
```

For detailed API documentation, visit: http://localhost:8000/docs

---

## 🧪 Testing

### Backend Tests
```bash
cd backend

# Run all tests
pytest

# Run with coverage
pytest --cov=app tests/

# Run specific test
pytest tests/api/test_auth.py -v
```

### Frontend Tests
```bash
cd frontend

# Run tests
npm test

# Run with coverage
npm test -- --coverage

# E2E tests with Playwright
npm run test:e2e
```

---

## 📐 Database

### Models
- **User**: Authentication & profile
- **Organization**: Company/tenant
- **Team**: User groups
- **Role**: Permission definition
- **Permission**: Access control
- **APIKey**: Service authentication
- **Company**: Business intelligence target
- **Executive**: Contact management
- **Prospect**: Lead management
- **Report**: Analytics & insights
- **AuditLog**: Compliance & security

### Migrations
```bash
# Create migration
alembic revision --autogenerate -m "Add new table"

# Apply migrations
alembic upgrade head

# Rollback
alembic downgrade -1
```

---

## 🔒 Security

- ✅ Password hashing with bcrypt
- ✅ JWT token-based authentication
- ✅ API key authentication
- ✅ Role-based access control (RBAC)
- ✅ Input validation with Pydantic
- ✅ Rate limiting on endpoints
- ✅ CORS configuration
- ✅ Audit logging for compliance
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ HTTPS ready (Docker + reverse proxy)

---

## 📈 Deployment

### Docker Build
```bash
# Build all images
docker-compose -f docker/docker-compose.yml build

# Build specific service
docker-compose -f docker/docker-compose.yml build backend
```

### Production Deployment
```bash
# Using production compose file
docker-compose -f docker/docker-compose.prod.yml up -d

# Scale services
docker-compose -f docker/docker-compose.prod.yml up -d --scale backend=3
```

### Environment Configuration
Update `.env` file for production:
```env
DEBUG=False
ENVIRONMENT=production
SECRET_KEY=your-production-secret-key
DATABASE_URL=postgresql://user:pass@db:5432/prod_db
REDIS_URL=redis://cache:6379
```

---

## 📖 Documentation

- [Architecture](docs/ARCHITECTURE.md) - System design & patterns
- [API Documentation](docs/API.md) - Endpoint specifications
- [Development Guide](docs/DEVELOPMENT.md) - Local setup & workflow

---

## 🤝 Contributing

1. Create a feature branch: `git checkout -b feature/your-feature`
2. Commit changes: `git commit -am 'Add feature'`
3. Push to branch: `git push origin feature/your-feature`
4. Submit a pull request

---

## 📝 License

Copyright © 2024 GLOBAL X SPARK AI. All rights reserved.

---

## 💡 Support

For issues, questions, or feature requests, please open an issue on GitHub.

---

**Built with ❤️ for enterprise innovation**
