Clone the Repo

`git clone https://github.com/statsig-io/python-flask-demo`

`cd python-flask-demo`

Install dependencies

`pip install -r requirements.txt`

Run the server

`gunicorn -w 4 main:app`

Run the tester

`python3 test.py`
