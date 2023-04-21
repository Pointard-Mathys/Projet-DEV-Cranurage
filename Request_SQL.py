import psycopg2


def name_from(table, research):
# connection
    conn = psycopg2.connect("dbname=cranaruge user=postgres password=root")

# request
    cursor = conn.cursor()
    query_request = "SELECT * FROM "+table+" WHERE Name LiKE "+"'%"+research+"%"+"'"
    
    cursor.execute(query_request)

# result
    res = cursor.fetchall() 
    print(res)
    print(len(res))
# connection close
    conn.close()
    return res







def element_from(table, element):
# connection
    conn = psycopg2.connect("dbname=cranaruge user=postgres password=root")

# request
    cursor = conn.cursor()
    query_request = "SELECT * FROM "+table+" WHERE attributes LIKE '%"+element+"%'"
    
# excution
    cursor.execute(query_request)
# result
    res = cursor.fetchall()
    print(res)
    print(len(res))

# close connection
    cursor.close()
    return res
    
    





def affinite_from(table, element):
# connection
    conn = psycopg2.connect("dbname=cranaruge user=postgres password=root")

# request
    cursor = conn.cursor()
    query_request = "SELECT * FROM "+table+" WHERE attributes LIKE '%"+element+"%"+"%'"
    
# excution
    cursor.execute(query_request)
# result
    res = cursor.fetchall()
    print(res)
    print(len(res))

# close connection
    cursor.close()
    return res






def materials_from(table, materials):
# connection
    conn = psycopg2.connect("dbname=cranaruge user=postgres password=root")
# request
    cursor = conn.cursor()
    query_request = "SELECT * FROM "+table+" WHERE upgrade_mats LIKE '%"+materials+"%'"
# excution
    cursor.execute(query_request)
# result
    res = cursor.fetchall()
    print(res)
# close connection
    cursor.close
    return res


name_from('bows', 'hunter bow iii')
# element_from('dual_swords', 'Fire')

