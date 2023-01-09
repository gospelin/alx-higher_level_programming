# PYTHON: OBJECT RELATIONAL MAPPING (ORM)

## Technologies

* **Ubuntu 20.04 LTS**
* **Python (version 3.8.5)**
* **MySQLdb (Version 2.1.1)**
* **SQLAlchemy (version 1.4.46)**
* **Pycodestyle (version 2.8.0)**
* **MySQL (Version 8.0.31)**
  
---

## Documentations | Resources

---
---
>
>* **[MySQLdb Docs](https://mysqlclient.readthedocs.io/)**
>* **[pycodestyle Guide](https://pypi.org/project/pycodestyle/)**
>* **[SQLAlchemy Tutorial](https://docs.sqlalchemy.org/en/13/orm/tutorial.html)**
>
>
---
---

## Installations

### Install MySQL 8

    sudo apt update && sudo apt install mysql-server

### To view MySQL version installed

    mysql --version

### To connect your MySQL Server

    sudo mysql

### Install MySQLdb Module

    sudo apt-get install python3-dev &&\
    sudo apt-get install libmysqlclient-dev &&\ 
    sudo apt-get install zlib1g-dev && \
    sudo pip3 install mysqlclient

### To view MySQLdb version installed

    $ python3
    >>> import MySQLdb
    >>> MySQL.version_info
    ((2, 1, 1, 'final', 0)

### Install SQLAlchemy Module

    sudo pip3 install SQLAlchemy

### SQLAlchemy Version

    $ python3
    >>> import sqlalchemy
    >>> sqlalchemy.__version__
    '1.4.22'
