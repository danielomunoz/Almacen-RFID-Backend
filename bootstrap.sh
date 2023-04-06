curl --location --request POST '127.0.0.1:8000/api/persona' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nombre": "Danilo1",
    "email": "danilo1@danilo.com",
    "movil": "666555444",
    "dni": "45555522L",
    "codigo_rfid": "76464764674767",
    "imagen": "https://www.images.com/danilo1",
    "rol": "profesor",
    "usuario": "danilo1",
    "password": "danilo1",
    "estado": "activo",
    "token_sesion": ""
}'
curl --location --request POST '127.0.0.1:8000/api/persona' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nombre": "Danilo2",
    "email": "danilo2@danilo.com",
    "movil": "666555444",
    "dni": "45555523L",
    "codigo_rfid": "76464764674768",
    "imagen": "https://www.images.com/danilo2",
    "rol": "alumno",
    "usuario": "danilo2",
    "password": "danilo2",
    "estado": "activo",
    "token_sesion": ""
}'
curl --location --request POST '127.0.0.1:8000/api/persona' \
--header 'Content-Type: application/json' \
--data-raw '{
    "nombre": "Danilo3",
    "email": "danilo3@danilo.com",
    "movil": "666555444",
    "dni": "45555524L",
    "codigo_rfid": "76464764674769",
    "imagen": "https://www.images.com/danilo3",
    "rol": "alumno",
    "usuario": "danilo3",
    "password": "danilo3",
    "estado": "activo",
    "token_sesion": ""
}'
