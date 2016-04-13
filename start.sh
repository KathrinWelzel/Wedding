#!/bin/bash

docker-compose up -d
docker exec -it wedding_server_1 cp bootcamp/env bootcamp/.env
docker exec -it wedding_server_1 python3 manage.py migrate
docker exec -it wedding_server_1 /bin/bash -c "echo \"from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')\" | python manage.py shell"
docker-compose restart
