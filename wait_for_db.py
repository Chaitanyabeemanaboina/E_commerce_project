# import time
# import MySQLdb
# import os
#
# db_config = {
#     'host': os.getenv('DB_HOST'),
#     'user': os.getenv('DB_USER'),
#     'password': os.getenv('DB_PASSWORD'),
#     'database': os.getenv('DB_NAME'),
#     'port': int(os.getenv('DB_PORT')),
# }
#
# while True:
#     try:
#         conn = MySQLdb.connect(**db_config)
#         conn.close()
#         break
#     except MySQLdb.OperationalError:
#         print("Waiting for the database to be ready...")
#         time.sleep(3)
