pip install -r requirements.txt

python3 manane.py collectstatic --no-input
python3 manage.py migrate