import psycopg2


def name_from(table, research):
# connection
    conn = psycopg2.connect("dbname=cranaruge user=postgres password=root")

# request
    cursor = conn.cursor()
    query_request = "SELECT * FROM "+table+" WHERE Name LiKE "+"'"+research+"%"+"'"
    
    cursor.execute(query_request)

# result
    res = cursor.fetchall() 

    print(res)
# connection close
    conn.commit()
    conn.close()
    return res


name_from("dual_swords", "T")