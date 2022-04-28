
import sys
sys.path.append("..")
from utils.db_utils import *

db_connect=create_connection("se","lbc","123456")#数据库连接
test=execute_read_query(db_connect,"select name,price from merchan2 where id=0")
print(type(test[0]))
