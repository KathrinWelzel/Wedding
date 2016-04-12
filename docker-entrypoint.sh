#!/bin/bash

#if [ -z "$DECOUPLE_DB" ]; then
#	sed "s|.*DATABASE_URL.*|DATABASE_URL=$DECOUPLE_DB|g" bootcamp/env > bootcamp/.env
#else
#	cp bootcamp/env bootcamp/.env
#fi

cp bootcamp/env bootcamp/.env
python3 manage.py migrate auth
python3 manage.py migrate                  # Apply database migrations
#python3 manage.py collectstatic --noinput  # Collect static files

# Prepare log files and start outputting logs to stdout
touch /usr/src/logs/gunicorn.log
touch /usr/src/logs/access.log
tail -n 0 -f /srv/logs/*.log &

if [ -f "$CERT/cert.pem" ] && [ -f "$CERT/key.pem" ]; then

	# Start Gunicorn processes
	echo Starting HTTPS Gunicorn.
	exec gunicorn bootcamp.wsgi:application \
		--name bootcamp \
		--bind 0.0.0.0:8000 \
		--workers 3 \
		--keyfile $CERT/key.pem \
		--certfile $CERT/cert.pem \
		--ssl-version 3 \
		--do-handshake-on-connect \
		--log-level=info \
		--log-file=/srv/logs/gunicorn.log \
		--access-logfile=/srv/logs/access.log \
		"$@"
else
	echo Starting HTTP Gunicorn.

	exec gunicorn bootcamp.wsgi:application \
		--name bootcamp \
		--bind 0.0.0.0:8000 \
		--workers 3 \
		--log-level=info \
		--log-file=/srv/logs/gunicorn.log \
		--access-logfile=/srv/logs/access.log \
		"$@"
fi
