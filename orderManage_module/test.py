from cgi import test
import os, sys
p = os.path.abspath('.')
sys.path.insert(1, p)
from utils.db_utils import*
connect=create_connection("se","lhd","123456")
message=execute_read_query(connect,"select * from merchan")
for i in message:
    print(i)