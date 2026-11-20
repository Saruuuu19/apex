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
- 🔐 **Google login** (OAuth) with secure sessions stored in `httpOnly` cookies
- 📱 **PWA**: install it on your phone and use it at the gym

## 🧱 Stack

| Layer | Current | Planned |
|-------|---------|---------|
| **Backend** | FastAPI · SQLAlchemy · Pydantic · Alembic configuration | Initial database migration |
| **Database** | SQLite configured | PostgreSQL |
| **Frontend** | — | React PWA |
| **Auth** | — | Google OAuth + opaque database-backed sessions |
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

The API skeleton exposes [interactive docs](http://localhost:8000/docs). It does not yet have workout endpoints, database migrations, or a frontend.

## 🗺️ Roadmap

- [x] SQLite configuration
- [ ] Database models (MVP)
- [ ] Initial Alembic migration
- [ ] Google OAuth authentication
- [ ] Routers and schemas: exercises, routines, sessions
- [ ] Frontend bootstrap (PWA)
- [ ] History, PRs, and per-exercise progress
- [ ] Migration to PostgreSQL

**Out of MVP scope (for now):** email/password login, AI-generated plans, social features, and push notifications.

## 🧠 Design Decisions

These design decisions describe planned behavior:

- **RPE** will be stored as a scaled integer (8.5 → 85) to avoid precision issues in SQLite.
- **Routines** will be publicly readable, but only their owners will be able to modify them.
- **Workout sessions** will be private because they contain personal training data.
- **Starting a routine** will copy its structure into a session and leave reps, weight, and RPE blank for you to fill in at the gym.

## 🤝 Contributing

This is a personal project under construction, but if you'd like to suggest improvements, please open an issue before sending a pull request.

---

<div align="center">

*Built in the gym, one set at a time.* 💪

</div>
