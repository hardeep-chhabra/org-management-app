# gpu-lab-backend-server

Main repo to manage GPU infra server

Install All Dependencies

## Migration & Backup


## Tool Stack

1. Python with Typing
2. SQL Alchemy[ORM]
3. Alembic[Data Migrations]
4. Postgres[DB]
6. Docker

## Data Backup

For importing data back to db

```
psql -U hardeepchhabra -h db -p 5432 -d organization_management -f ./alembic/backup/[backup_name].sql
```

## Data Migrations Command

For Adding Migration

```
alembic revision --autogenerate -m "Migration message"
alembic upgrade head
```

For Roll back:

``alembic downgrade -1``

## Database Access Command

```
psql -h db -U hardeepchhabra -d 12345;
```
