from vertica_python import connect
from .constants import *
import pandas as pd

def executeQuery(query, columns=None, return_data=None):
    vertica_conn_info = {
        'host': DATABASE_HOST, 'port': DATABASE_PORT, 'user': DATABASE_UID,
        'password': DATABASE_PID,
        'database': DATABASE_DB_NAME}
    connection_vertica = connect(**vertica_conn_info)
    cursor_vertica = connection_vertica.cursor()

    cursor_vertica.execute(query)
    rows_vertica = cursor_vertica.fetchall()
    connection_vertica.close()

    if return_data:
        return pd.DataFrame(rows_vertica, columns=columns)
    else:
        return True