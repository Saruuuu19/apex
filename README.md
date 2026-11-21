<div align="center">

# 🏋️ Apex

**Your gym, your numbers. Train, log, and understand your progress.**

![Status](https://img.shields.io/badge/status-in%20development-orange)
![Python](https://img.shields.io/badge/Python-3.15+-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)

</div>

---

## ⚡ What is Apex?

Apex is a **gym tracker in development**. It's designed to make training easier by helping you log sets, weights, and RPE, track personal records, and see how your strength and training volume change over time.

It's also the **project that ties together everything I'm learning**: FastAPI backends, databases, real authentication, and a modern frontend.

## 🎯 Planned Features

- 📋 **Exercise catalog** with filters by muscle group and equipment
- 🗂️ **Routines** with planned exercises and sets
- 🔥 **Workout logging** in real time: reps, weight, and RPE per set
- 📈 **History and progress**: max weight and volume per exercise
- 🔐 **Sign-in** with username and password or Google, using `HttpOnly` session cookies
- 📱 **PWA**: install it on your phone and use it at the gym

## 🧱 Stack

| Layer | Current | Planned |
|-------|---------|---------|
| **Backend** | FastAPI · SQLAlchemy · Pydantic · Alembic migrations | API routes for core features |
| **Database** | SQLite configured | PostgreSQL |
| **Frontend** | — | React PWA |
| **Auth** | — | Username/password · Google OAuth · Opaque database-backed sessions |
| **Tooling** | uv · Ruff · Docker | — |

## 🚀 Getting Started

### Run locally

With Python 3.15+ and [uv](https://docs.astral.sh/uv/), run these commands from the repository root:

```bash
cd backend
uv sync --locked
uv run fastapi dev app/main.py
```

### Run with Docker

With Docker and Docker Compose installed, run this from the repository root:

```bash
docker compose up --build
```

The backend has MVP database models, Alembic migrations, and request and response schemas for exercises, routines, workout sessions, sets, and user profiles. Session validation is implemented, but sign-in does not issue cookies yet. The [interactive docs](http://localhost:8000/docs) are available, but feature routes and the frontend are not implemented yet.

## 🗺️ Roadmap

- [x] SQLite configuration
- [x] Database models (MVP)
- [x] Initial Alembic migration
- [x] Schemas for exercises, routines, workout sessions, sets, and user profiles
- [ ] Username/password and Google OAuth authentication
- [ ] API routes for exercises, routines, workout sessions, and user profiles
- [ ] Frontend bootstrap (PWA)
- [ ] History, PRs, and per-exercise progress
- [ ] Migration to PostgreSQL

**Out of MVP scope (for now):** email/password login, AI-generated plans, social features, and push notifications.

## 🧠 Design Decisions

These design decisions describe planned behavior:

- **RPE** is stored as `Numeric(3, 1)`, with one decimal place (for example, `8.5`).
- **Routines** will be publicly readable, but only their owners will be able to modify them.
- **Workout sessions** will be private because they contain personal training data.
- **Workout duration** is `completed_at - started_at`. The server records `completed_at` when the user finishes the workout; individual sets track only whether they are completed.
- **Routine sets** can store planned reps, weight, and RPE. A routine needs at least one exercise, and every exercise needs at least one set, even if its targets are blank. Starting a routine will create separate workout sets so you can log what you actually did without changing the plan.

## 🤝 Contributing

This is a personal project under construction, but if you'd like to suggest improvements, please open an issue before sending a pull request.

---

<div align="center">

*Built in the gym, one set at a time.* 💪

</div>
