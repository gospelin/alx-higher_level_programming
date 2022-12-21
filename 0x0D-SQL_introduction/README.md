# SQL Introduction

## Instructions

* All files were executed on Ubuntu 20.04 LTS using **MySQL 8.0 (version 8.0.31)**
* All files end with a new line.
* All SQL queries start with a comment describing the task
* All SQL keywords are in uppercase

## Installation

To install MySQL on **Ubuntu 20.04 LTS**

        $ sudo apt update && sudo apt install mysql-server
        $

To view the version installed

        $ mysql --version
        mysql  Ver 8.0.31-0ubuntu0.20.04.2 for Linux on x86_64 ((Ubuntu))
        $

To connect your MySQL Server:

        $ sudo mysql
        Welcome to the MySQL monitor.  Commands end with ; or \g.
        Your MySQL connection id is 11
        Server version: 8.0.31-0ubuntu0.20.04.2 (Ubuntu)

        Copyright (c) 2000, 2022, Oracle and/or its affiliates.

        Oracle is a registered trademark of Oracle Corporation and/or its
        affiliates. Other names may be trademarks of their respective
        owners.

        Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

        mysql>
        mysql> exit
        Bye
        $

## Files

| Filename | Description |
  --------   -----------
| 0-list_databases.sql | Script to List all databases in MySQL Server |
| 1-create_database_if_missing.sql | Script to Create a database without error |
