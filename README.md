# microBlogPython
MicroBlog created with python using Flask mega tutorial book as reference

## How to run it

### The Basics:
1. Install [Python 3.X](https://www.python.org/downloads/)  
2. (Optional) Once you have cloned the repository, create a virtual environment using this command  `python -m venv virtual`
3. Install flask using this command `pip install flask`
4. You need to have MySQL on your computer. You can use WAMP or LAMP for an easy installation
5. Create an Schema or DB in MySQL

### Dependencies:
In order to execute the code you will need to install some flask extensions
1. Flask WTF in order to work with forms: `pip install flask-wtf`
2. Flask SQLAlchemy is a ORM to manage DB using entities: `pip install flask-sqlalchemy`
3. Flask Migrate to update DB data structure: `pip install flask-migrate`
4. This Micloblog was created using Mysql instead of SQLite, so you will need to install mysql client: `pip install "mysqlclient==1.3.12`
5. Flask login in order to manage user login state: `pip install flask-login`

### How to run it (Area in construction):
1. `flask db init`
2. `flask db migrate`
3. `flask db upgrade`
3. `set FLASK_APP=microblog.py`
4. `flask run`

