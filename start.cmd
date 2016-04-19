@ECHO OFF

Set name=docker

CALL :machine %name%
CALL :environment %name%
CALL :start

docker ps
GOTO :eof

::----------------------------------
::-- Start docker-machine
::----------------------------------
:machine
docker-machine start %1 > ok.txt  2> temp.txt
set /p output=<temp.txt
del ok.txt
del temp.txt

ECHO.%output% | FIND /I "not exist" > Nul && (
  Echo Creating new machine %1
  docker-machine create -d virtualbox %1
  CALL :machine %1
)
::|| (
::  Echo Did not find "not exist"
::)
GOTO :eof

::----------------------------------
::-- Setup docker environment
::----------------------------------
:environment
docker-machine env --shell cmd %1 | findstr /v # >> temp_config.bat
echo exit /B >> temp_config.bat
call temp_config.bat
del temp_config.bat
GOTO :eof

::----------------------------------
::-- Start compose script
::----------------------------------
:start
SETLOCAL
copy .\src\bootcamp\env .\src\bootcamp\.env
docker-compose up -d
docker exec -it wedding_server_1 python3 manage.py migrate
docker exec -it wedding_server_1 python3 manage.py createsuperuser
docker-compose restart
ENDLOCAL
GOTO :eof
