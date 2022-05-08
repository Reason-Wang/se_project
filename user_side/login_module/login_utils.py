from utils.db_utils import create_connection, execute_read_query, execute_query


connection = create_connection(db_name='se', db_user='shy', db_password='123456')
connection.autocommit = True

def get_user_info(user_name):
    sql_select_users = f" select * from customer where cus_name = '{user_name}' "
    print(sql_select_users)
    users = execute_read_query(connection, sql_select_users) # should be list with only one element
    print(users)
    user_info = {}
    if len(users) != 0:
        user_info['name'] = users[0][2]
        user_info['password'] = users[0][1]
        user_info['phone'] = users[0][3]
        user_info['address'] = users[0][4]

    return user_info

def register_user_info(user_info):
    sql_insert_user = f"""
    insert into customer
    values ('{user_info['name']}', '{user_info['password']}', '{user_info['name']}', '{user_info['phone']}', '{user_info['address']}')
    """
    print(sql_insert_user)
    execute_query(connection, sql_insert_user)

