sudo apt-get update;
sudo apt-get upgrade -y;
sudo apt-get install python3 \
		     python3-pip \
		     python3-dev \
		     libpq-dev \
		     postgresql \
		     postgresql-contrib \
		     nginx \
		     curl

sudo systemctl restart postgresql
sudo -u postgres psql -f scripts/db.sql

sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv

virtualenv intrassistantenv
sudo source intrassistantenv/bin/activate
pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

echo "Everything is ready. Don't forget to deactivate to exit virtualenv."
