#Permitir conectarme a una base de datos PostgreSQl
import psycopg2
import psycopg2.extras
from psycopg2.extras import RealDictCursor
from ..general.config import Parametros
from ..general.logs import HandleLogs

def conn_db():
    return psycopg2.connect(host=Parametros.db_host,
                            port=int(Parametros.db_port),
                            user=Parametros.db_user,
                            password=Parametros.db_pass,
                            database=Parametros.db_name,
                            cursor_factory=RealDictCursor)

class DataBaseHandle:
    @staticmethod
    def getRecords(query, tamanio, record=()):
        try:
            with conn_db() as conn, conn.cursor() as cursor:
                if len(record) == 0:
                    cursor.execute(query)
                else:
                    cursor.execute(query, record)
                if tamanio == 0:
                    res = cursor.fetchall()
                elif tamanio == 1:
                    res = cursor.fetchone()
                else:
                    res = cursor.fetchmany(tamanio)
                return res
        except Exception as ex:
            HandleLogs.write_error(ex)

    @staticmethod
    def ExecuteNonQuery(query, record):
        try:
            with conn_db() as conn, conn.cursor() as cursor:
                if len(record) == 0:
                    cursor.execute(query)
                    conn.commit()
                else:
                    cursor.execute(query, record)
                    conn.commit()

                if query.find('INSERT') > -1:
                    cursor.execute('SELECT LASTVAL()')
                    ult_id = cursor.fetchone()['lastval']
                    conn.commit()
                    return ult_id
                else:
                    return 0
        except Exception as ex:
            HandleLogs.write_error(ex)
            return -1
