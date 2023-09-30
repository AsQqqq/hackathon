# Скачивание

Скачать и установить postgresql
- <https://www.postgresql.org/download/windows/>

---
# Настройка

Открыть файл папку в "пуск" `PostgreSQL` и запустить `SQL Shell`

Зайти в пользователя `postgresql` и выполнить следующие команды
- `CREATE USER hackathon PASSWORD 'toor';`
- `CREATE DATABASE hackathon;`
- `GRANT ALL ON DATABASE hackathon TO hackathon;`
