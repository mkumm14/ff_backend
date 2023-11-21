 #!/bin/bash

echo "Create Migrations"
python3 manage.py makemigrations
echo "==================="


echo "Migrate"
python3 manage.py migrate
echo "==================="

echo "start server"

python3 manage.py runserver 0.0.0.0:8000

