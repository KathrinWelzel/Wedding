@echo off

copy .\src\bootcamp\env .\src\bootcamp\.env

docker-compose up -d
docker exec -it wedding_server_1 python3 manage.py migrate
docker exec -it wedding_server_1 python3 manage.py createsuperuser
docker-compose restart
