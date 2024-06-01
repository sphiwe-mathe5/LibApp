poetry add $(cat requirements.txt | tr '\n' ' ')


python3 manage.py collectstatic --no-input
python3 manage.py migrate