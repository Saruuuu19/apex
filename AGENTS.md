# Apex development guide

## Commands

Use Python 3.15+ and `uv`. Run these commands from `backend/`:

- **Install:** `uv sync --locked`
- **Dev server:** `uv run fastapi dev app/main.py` (docs at `http://localhost:8000/docs`)
- **Smoke test:** `uv run python -c 'from fastapi.testclient import TestClient; from app.main import app; assert TestClient(app).get("/openapi.json").status_code == 200'`
- **Organize imports:** `uv run ruff check --select I --fix .`
- **Fix lint:** `uv run ruff check --fix .`
- **Apply migrations to the configured database:** `uv run alembic upgrade head`
- **Inspect migrations:** `uv run alembic heads` and `uv run alembic current`

Run both Ruff commands in that order after every change, even a one-line edit. There is no configured test suite, type checker, or frontend build yet. The smoke test checks that the API starts and serves OpenAPI; it does not validate feature behavior.

For schema changes, apply the migrations and check for drift on a fresh SQLite database:

```sh
(
  set -e
  scratch=$(mktemp -d)
  trap 'rm -f "$scratch/apex.db"; rmdir "$scratch"' EXIT
  export DATABASE_URL="sqlite:///$scratch/apex.db"
  uv run alembic upgrade head
  uv run alembic check
)
```

Run Docker Compose commands from the repository root:

- **Validate Compose config:** `docker compose config --quiet`
- **Build the backend image:** `docker compose build backend`
- **Run in Docker:** `docker compose up --build -d`
- **Stop without deleting data:** `docker compose down`

## Project structure

- `backend/app/main.py` is the FastAPI entry point. Add feature routes under `backend/app/routers/` and register them in `main.py`. There are no feature routers yet.
- `backend/app/schemas/` is for Pydantic request and response models. SQLAlchemy models and shared domain enums live in `backend/app/models/`.
- `backend/app/models/__init__.py` imports all ORM models. Export new models there so Alembic sees them when `backend/migrations/env.py` loads the metadata.
- `backend/migrations/versions/` contains committed schema revisions. Review newly generated revisions before committing them. `backend/uv.lock` is tracked but managed by `uv`; `.venv/` and caches are generated and should not be edited.

## Code style and conventions

- Use English for all project work, including identifiers, comments, documentation, commit messages, pull requests, and user-facing text.
- Follow the existing domain layout: keep ORM models, API schemas, and routers separate. Prefer direct code over new helpers or abstractions unless they solve a concrete problem.
- Use `app.*` imports in the backend. For new UUID columns, use Python's `UUID` in type annotations and SQLAlchemy's portable `Uuid` as the column type.
- Routine sets store planned targets; workout sets record actual results in separate rows. Each set belongs to exactly one parent, and draft workout reps can be null.

## Boundaries

- Never create a Git commit unless the user explicitly asks you to commit.
- Never edit a merged migration. Add a new revision for later schema changes.
- Never commit `.env` files, credentials, local SQLite databases, or `DEV.md`/`DEV.MD`. Version only sanitized environment templates.
- Do not add dependencies without approval. For approved changes, use `uv` and update both `pyproject.toml` and `uv.lock`.
- Do not run destructive database commands against existing data or remove Docker volumes without explicit approval.

## Definition of done

- Both Ruff commands pass. Run the API smoke test for backend behavior changes and verify the behavior changed, not just that the app imports.
- Cover new or changed behavior with a focused test or reproducible check. Run any relevant existing tests and report what could not be verified.
- For schema changes, include the revision and verify `alembic upgrade head` followed by `alembic check` on fresh SQLite.
- Update documentation when API behavior or setup commands change. Validate Compose and build the image when changing Docker configuration.

## Gotchas

- The local default is `backend/apex.db`. Compose uses `/data/apex.db` inside its named volume, so a local migration does not migrate the container's database.
- Use the application engine for Alembic and app database work so SQLite foreign-key enforcement stays enabled. Do not use SQLAlchemy's uppercase `UUID` column type: SQLite reflects it as `NUMERIC`, causing false migration diffs.
- Docker images include the migrations present at build time. Rebuild after changing migration files. `docker compose down -v` deletes the SQLite volume.
