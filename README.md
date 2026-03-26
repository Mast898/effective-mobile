# effective-mobile
Проверка задания. описание как запустить на своем арм. ТЕМА: Команда Effective Mobile

Для начало скачиваем себе на лок.арм 
git clone https://github.com/Mast898/effective-mobile.git


Описание. 
Обязательно обращаем внимание, какая установленна версия  docker-compose, у меня установленна версия Docker Compose version v5.1.1

Запустить 
переходим в директорию cd effective-mobile

Запустить сервисы
docker compose up -d --build
начнет собираться 

Проверить статус
docker compose ps
service@service-VirtualBox:~/effective-mobile$ docker compose ps

NAME                       IMAGE                      COMMAND                  SERVICE   CREATED          STATUS                    PORTS
effective-mobile-backend   effective-mobile-backend   "python app.py"          backend   23 seconds ago   Up 23 seconds (healthy)   8080/tcp
effective-mobile-nginx     nginx:1.25-alpine          "/docker-entrypoint.…"   nginx     23 seconds ago   Up 17 seconds (healthy)   0.0.0.0:80->80/tcp

Если хотим остановить, можно сднелать в самом конце, после просмотра !!
Остановка 
docker compose down

Проверка результата!!!
curl http://localhost
ВЫВОД:
service@service-VirtualBox:~/effective-mobile$ curl http://localhost
Hello from Effective Mobile!


Проверка health endpoint nginx

curl http://localhost/health
ВЫВОД:
service@service-VirtualBox:~/effective-mobile$ curl http://localhost/health
healthy

Проверка что backend не доступен напрямую
curl http://localhost:8080  
ВЫДАЛ ОШИБКУ !!

ЕЩЕ РАЗ: Проверка что nginx работает
curl http://localhost  
"Hello from Effective Mobile!"

curl http://localhost/health
ВЫВОД:
healthy



docker inspect effective-mobile-backend --format='{{.State.Health.Status}}'
ВЫВОД:
docker inspect effective-mobile-backend --format='{{.State.Health.Status}}'
healthy

ВЫВОД:
docker inspect effective-mobile-nginx --format='{{.State.Health.Status}}'
healthy



Проверка сети
docker network inspect effective-mobile-network