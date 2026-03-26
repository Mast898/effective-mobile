# effective-mobile


Веб-приложение с nginx reverse proxy в Docker-контейнерах.

### Схема работы

| Компонент | Описание |
|-----------|----------|
| **Nginx** | Reverse proxy, принимает запросы на порту 80, проксирует на backend |
| **Backend** | Python HTTP сервер, слушает порт 8080, доступен только внутри Docker-сети |

### Поток запроса

1. Клиент отправляет HTTP-запрос на `http://localhost`
2. Nginx принимает запрос и проксирует на сервис `backend:8080`
3. Backend обрабатывает запрос и возвращает ответ
4. Nginx передаёт ответ клиенту

---

## 📁 Структура проекта

 ├── backend/
│ ├── Dockerfile # Dockerfile для Python приложения
│ └── app.py # HTTP сервер на Python
├── nginx/
│ └── nginx.conf # Конфигурация nginx reverse proxy
├── docker-compose.yml # Оркестрация сервисов
├── .gitignore # Исключения для Git
└── README.md # Документация


---

## 🚀 Быстрый старт

### Требования

| Компонент | Минимальная версия |
|-----------|-------------------|
| Docker | 20.10+ |
| Docker Compose | V2 (плагин) |

### Проверка версий

```bash
docker --version
docker compose version

# Клонировать репозиторий
git clone https://github.com/Mast898/effective-mobile.git
cd effective-mobile

# Запустить сервисы
docker compose up -d --build

# Проверить статус
docker compose ps


Остановка
docker compose down

# Все логи
docker compose logs -f

# Только backend
docker compose logs -f backend

# Только nginx
docker compose logs -f nginx

-------------Проверка работоспособности

curl http://localhost
ВЫВОД:
Hello from Effective Mobile!


Health endpoint
curl http://localhost/health
ВЫВОД:
healthy


Проверка изоляции backend
curl http://localhost:8080
ВЫВОД:
curl: (7) Failed to connect to localhost port 8080: Connection refused


Диагностика

docker compose ps

service@service-VirtualBox:~/effective-mobile$ docker compose ps

NAME                       IMAGE                      COMMAND                  SERVICE   CREATED          STATUS                    PORTS
effective-mobile-backend   effective-mobile-backend   "python app.py"          backend   23 seconds ago   Up 23 seconds (healthy)   8080/tcp
effective-mobile-nginx     nginx:1.25-alpine          "/docker-entrypoint.…"   nginx     23 seconds ago   Up 17 seconds (healthy)   0.0.0.0:80->80/tcp




# Backend
 
docker inspect effective-mobile-backend --format='{{.State.Health.Status}}'
ВЫВОД:
healthy

# Nginx
 
docker inspect effective-mobile-nginx --format='{{.State.Health.Status}}'
ВЫВОД:
healthy

Сеть
docker network inspect effective-mobile-network


Проверка пользователя в backend

service@service-VirtualBox:~/effective-mobile$ docker exec effective-mobile-backend whoami
ВЫВОД:
appuser
