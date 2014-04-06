## Overview

This is a RSS Reader wrote by Python Flask, build on top of SQLAlchemy, Twitter Bootstrap and feedparser

Check the ```requirements.txt``` in top level directory.

```bash
Flask==0.10
Flask-OAuth==0.12
Flask-SQLAlchemy==0.16
Flask-WTF==0.8.2
Jinja2==2.6
SQLAlchemy==0.8.0
WTForms==1.0.3
Werkzeug==0.8.3
distribute==0.6.31
facepy==0.8.4
feedparser==5.1.3
httplib2==0.7.7
oauth2==1.5.211
pysqlite==2.6.3
requests==1.1.0
tweepy==2.0
wsgiref==0.1.2
```

```Profile``` was used to deploy in heroku
```bash
web: python run.py
```

## Quick start 
### Clone and install requirement

Assume that you have Python 2.7+ as well as pip. 
First install virtualenv for Python. 
```bash
sudo pip install virtualenv
```

Clone this repo and install requirements as below
```bash
git clone git@github.com:DTVD/PyRSSReader.git
cd PyRSSReader
virtualenv venv
source venv/bin/active
pip install -r requirements.txt
```

### Create the database
Once the environment is ready, you can go ahead to create database with ```python shell.py```
```python
>>> db.create_all()
```

You should see a sqlite database ```app.db``` is created under top level directory.
Check it's table with ```sqlite3 app.db``` and you should see 
```sql
SQLite version 3.7.13 2012-07-17 17:46:21
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .tables
facebook  feed      feeduser  star      twitter   user
sqlite>

```

### Run the application
Run the application in localhost is quite easy, just ```python run.py``` 
```bash
(venv)DTVD@DTVD-Air :: ~/PyRSSReader (master)-->> python run.py
 * Running on http://0.0.0.0:5000/
 * Restarting with reloader
```
Congratz! Open your browser at ```127.0.0.1:5000``` and test everything out!




