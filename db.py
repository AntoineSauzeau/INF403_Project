
def create_database(cur):
    interpret_sql_file(cur, "scripts/init.sql")

def delete_database(cur):
    pass

def interpret_sql_file(cur, filepath):
    
    file = open(filepath, "r")

    l_requests = file.read().split(";")
    for request in l_requests:
        cur.execute(request)

    file.close()