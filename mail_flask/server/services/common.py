from server.services.db_service import DBConnect
from server.constants import *
import datetime



def get_kno_results(query, param =None):
    db_con = DBConnect(KNOWLEDGE_DB_HOST, KNOWLEDGE_DB_PORT, KNOWLEDGE_DB_USERNAME,
                        KNOWLEDGE_DB_PASSWORD,KNOWLEDGE_DATABASE_NAME)

    db_con.begin()
    res = db_con.select_all(query,param)
    db_con.close()
    return res


def execute_knowledge(query, param=None):
    db_con = DBConnect(KNOWLEDGE_DB_HOST, KNOWLEDGE_DB_PORT, KNOWLEDGE_DB_USERNAME,
                       KNOWLEDGE_DB_PASSWORD, KNOWLEDGE_DATABASE_NAME)

    db_con.begin()
    res = db_con.execute(query, param)
    db_con.commit()
    db_con.close()
    return res

def ledb_con(uname, pwd, dbname, hostname):
    hostname = ""
    uname = ""
    pwd = ""
    try:
        db_con =DBConnect(hostname,uname,pwd,dbname)
        return db_con
    except Exception as e:
        return None

def get_current_date_tz(tz_name):
    time_stamp = datetime.datetime.utcnow()
    return localize(time_stamp, tz_name).date()

def localize(time_stamp, tz_name):
    LOCAL_TIMEZONE = pytz.timezone(tz_name)
    local_dt  =LOCAL_TIMEZONE.localize(time_stamp)
    tzoffset = local_dt.utcoffset()
    local_dt = local_dt.replace(param = None)
    local_dt = local_dt +tzoffset
    return local_dt