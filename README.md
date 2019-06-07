## Setting up

- Clone project
- pip install -r requirements.txt
- Create a .env file from .env.example and edit it appropriately
- Run the following to update and refresh your .bashrc:
 echo "source `which activate.sh`" >> ~/.bashrc
 $ source ~/.bashrc
 source .env
- Create Database flask_api
- Run migrations:
python manage.py db init
python manage.py db migrate
- run test by running python test_bucketlist.py
- Serve the application: flask run

You are good to go :)


