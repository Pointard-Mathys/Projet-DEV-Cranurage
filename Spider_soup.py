# import mysql.connector
# import requests
# from bs4 import BeautifulSoup
# import sqlite3


# # Set up the connection parameters
# host = 'localhost'
# user = 'root'
# password = ''
# database = 'cranurage'


# def sword_master(url):   
# # Send a GET request to the website
#         response = requests.get(url)

# # Parse the HTML content using BeautifulSoup
#         soup = BeautifulSoup(response.content, 'html.parser')

# # Extract the table data
#         table = soup.find('table')
#         rows = table.find_all('tr')

# # Connect to the SQLite database
#         conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# # Create the table in the database
#         query_create = f"CREATE TABLE IF NOT EXISTS weapons (name TEXT, rarity TEXT, attributes TEXT, sharpness TEXT, slots TEXT, rank TEXT, price TEXT, creation_mats TEXT, upgrade_mats TEXT, description TEXT) DEFAULT CHARACTER SET eucjpms COLLATE eucjpms_bin;"
#         cursor = conn.cursor()
#         cursor.execute(query_create)
        
# # Insert the data into the table
#         for row in rows:
#                 cols = row.find_all('td')
#                 if cols:
#                         name = cols[0].get_text().strip()
#                         rarity = cols[1].get_text().strip()
#                         attributes = cols[2].get_text().strip()
#                         sharpness = cols[3].get_text().strip()
#                         slots = cols[4].get_text().strip()
#                         rank = cols[5].get_text().strip()
#                         price = cols[6].get_text().strip()
#                         creation_mats = cols[7].get_text()
#                         upgrade_mats = cols[8].get_text()
#                         description = cols[9].text.strip()

# # Insert the data into the database
#                         query_insert = """INSERT INTO weapons (name,rarity, attributes, sharpness, slots, rank, price, creation_mats, upgrade_mats, description) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"""
#                         cursor.execute(query_insert, (name, rarity, attributes, sharpness, slots, rank, price, creation_mats, upgrade_mats, description))
# # Commit the changes and close the connection
#         conn.commit()
#         conn.close()

from Get_weapon import sword_master, artilleur, bows

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/tachi.htm", "Long_Sword")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/tachi_g.htm#t8", "Long_Sword")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/tachi_s.htm#t5", "Long_Sword")

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/taiken.htm", "Great_Sword")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/taiken_g.htm#t8", "Great_Sword")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/taiken_s.htm#t5", "Great_Sword")

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/katate.htm", "Sword_and_Shield")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/katate_g.htm#t8", "Sword_and_Shield")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/katate_s.htm#t5", "Sword_and_Shield")

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/souken.htm", "Dual_Swords")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/souken_g.htm#t8", "Dual_Swords")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/souken_s.htm#t5", "Dual_Swords")

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/hammer.htm", "Hammer")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/hammer_g.htm#t8", "Hammer")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/hammer_s.htm#t5", "Hammer")

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/horn.htm", "Hunting_Horn")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/horn_g.htm#t8", "Hunting_Horn")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/horn_s.htm#t5", "Hunting_Horn")

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/lance.htm", "Lance")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/lance_g.htm#t8", "Lance")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/lance_s.htm#t5", "Lance")

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/gunlance.htm", "Gunlance")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/gunlance_g.htm#t8", "Gunlance")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/gunlance_s.htm#t5", "Gunlance")

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/tonfa.htm", "Tonfa")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/tonfa_g.htm#t8", "Tonfa")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/tonfa_s.htm#t5", "Tonfa")

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/slaxe.htm", "Switch_axe")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/slaxe_g.htm#t8", "Switch_axe")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/slaxe_s.htm#t5", "Switch_axe")

# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/magspike.htm", "Magnet_spike")
# sword_master("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/magspike_s.htm#t5", "Magnet_spike")




artilleur("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/right.htm","Light_Bowgun")
artilleur("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/right_g.htm#t8","Light_Bowgun")
artilleur("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/right_s.htm#t5","Light_Bowgun")

# artilleur("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/heavy.htm","Heavy_Bowgun")
# artilleur("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/heavy_g.htm#t8","Heavy_Bowgun")
# artilleur("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/heavy_s.htm#t5","Heavy_Bowgun")




# bows("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/yumi.htm", "Bows")
# bows("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/yumi_g.htm#t8", "Bows")
# bows("https://xl3lackout.github.io/MHFZ-Ferias-English-Project/buki/yumi_s.htm#t5", "Bows")
