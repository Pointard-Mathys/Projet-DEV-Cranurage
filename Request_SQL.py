import psycopg2


def global_search(table, element, affinity, materials, rarity, ):
# connection
    conn = psycopg2.connect("dbname=test_cranaruge user=postgres password=password port=1130")

    cursor = conn.cursor()
    query_request = "SELECT * FROM "+table
    if len(element) > 0:
        query_request += " WHERE attributes LIKE "+"'%"+element+"%"+"'"
        if affinity != 0:
            query_request += " AND affinity LIKE "+"'%"+str(affinity)+"%"+"'"
            if len(materials) > 0:
                query_request += " AND creation_mats LIKE "+"'%"+materials+"%"+"'"
                query_request += " AND upgrade_mats LIKE "+"'%"+materials+"%"+"'"
                if rarity > 0:
                    query_request += " AND rarity LIKE "+"'%"+str(rarity)+"%"+"'"
    
    elif affinity != 0:
        query_request += " WHERE affinity LIKE "+"'%"+str(affinity)+"%"+"'"
        if len(materials) > 0:
            query_request += " AND creation_mats LIKE "+"'%"+materials+"%"+"'"
            query_request += " AND upgrade_mats LIKE "+"'%"+materials+"%"+"'"
            if rarity > 0:
                query_request += " AND rarity LIKE "+"'%"+str(rarity)+"%"+"'"
    
    elif len(materials) > 0:
        query_request += " WHERE creation_mats LIKE "+"'%"+materials+"%"+"'"
        query_request += " AND upgrade_mats LIKE "+"'%"+materials+"%"+"'"
        if rarity > 0:
            query_request += " AND rarity LIKE "+"'%"+str(rarity)+"%"+"'"
    
    elif rarity > 0:
        query_request += " WHERE rarity LIKE "+"'%"+str(rarity)+"%"+"'"

    cursor.execute(query_request)

# result
    res = cursor.fetchall() 
    print(res)
    print(len(res))
# connection close
    conn.close()
    return res

def name_from(table, research):
# connection
    conn = psycopg2.connect("dbname=test_cranaruge user=postgres password=password port=1130")

# request
    cursor = conn.cursor()
    query_request = "SELECT * FROM "+table+" WHERE name LIKE "+"'%"+research+"%"+"'"
    
    print("Query : ", query_request)
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
    conn = psycopg2.connect("dbname=test_cranaruge user=postgres password=password port=1130")

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





def critical_from(table, element):
# connection
    conn = psycopg2.connect("dbname=test_cranaruge user=postgres password=password port=1130")

# request
    cursor = conn.cursor()
    query_request = "SELECT name, rarity, attributes, slots, price, creation_mats, upgrade_mats FROM "+table+" WHERE attributes LIKE '%"+element+"%"+"%'"
    
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
    conn = psycopg2.connect("dbname=test_cranaruge user=postgres password=password port=1130")
# request
    cursor = conn.cursor()
    query_request = "SELECT name, rarity, attributes, slots, price, creation_mats, upgrade_mats FROM "+table+" WHERE upgrade_mats LIKE '%"+materials+"%'"
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

