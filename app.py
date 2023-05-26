from logging import root
import mariadb
from dbcreds import host, port, user, password, database


conn = mariadb.connect(
    host=localhost,
    port=3306,
    user=root,
    password=password,
    database=python2
)


cursor = conn.cursor()
