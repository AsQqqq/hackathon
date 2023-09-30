# Скачивание

- `sudo apt update`
- `sudo apt install postgresql`
- `sudo systemctl is-active postgresql`
    - Должно вернуть `activate`

---
# Настройка

Открыть терминал и ввести `sudo su - postgres`

Далее `psql`

В postgresql вводим
- `CREATE USER hackathon PASSWORD 'toor';`
- `CREATE DATABASE hackathon;`
- `GRANT ALL PRIVILEGES ON DATABASE hackathon to hackathon;`
