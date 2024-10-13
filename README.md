# Org Management Project


## Step By Step DB Migrations and Running the FastAPI Project


## Tool Stack

1. Python & FastAPI
2. SQL Alchemy[ORM]
3. Alembic[Data Migrations]
4. Postgres[DB]
5. Docker
6. Docker Compose

## Data Migrations Command

Just Do

```
alembic upgrade head
```

And the rest is all taken care of. This will automatically reflect changes in the postgres DB, as the migrations file are available already


## Running the FastAPI Application inside the Root Project Directory

```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
uvicorn app.main:app --reload --port 3754
```


## For Running Everything Inside Docker Container, Just Run

```
docker-compose up --build
```

And then access All APIs via the Documentation provided via Postman or FastAPI Docs