import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),os.pardir)))
from utils.db_utils import *
db_connect=create_connection("se","lbc","123456")#数据库连接

if __name__ == '__main__':
    test=execute_read_query(db_connect,"select name,price from merchan2 where id=0")
    print(type(test[0]))
