import cx_Oracle
from sys import modules
import time

db = cx_Oracle.connect('itsm', 'itsm', '192.168.8.86:1521/ora10')
cursor = db.cursor()

create_table = """
CREATE TABLE sara_time (
  times DATE,
  timestamps TIMESTAMP
)
"""




