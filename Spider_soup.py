import mysql.connector
import requests
from bs4 import BeautifulSoup
import sqlite3
import psycopg2


# Set up the connection parameters
# host = 'localhost'
# user = 'root'
# password = ''
# database = 'cranurage'

def sword_master(url, name_table):   
# Send a GET request to the website
        response = requests.get(url)

# Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

# Extract the table data
        table = soup.find('table')
        rows = table.find_all('tr')

# Connect to the SQLite database
        conn = psycopg2.connect("dbname=test_cranaruge user=postgres password=password port=1130")

        # conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Create the table in the database
        query_create = f"CREATE TABLE IF NOT EXISTS "+name_table+" (name TEXT,disgrade TEXT,upgrade TEXT,rarity TEXT,attack TEXT, attributes TEXT,affinity TEXT, sharpness TEXT, slots TEXT, rank TEXT, price TEXT, creation_mats TEXT, upgrade_mats TEXT, description TEXT)"
        cursor = conn.cursor()
        cursor.execute(query_create)

# extrate data
        for row in rows:
# find all "td" for all data
                cols = row.find_all('td')
                if cols:
# find all div for Upgarde and Disgrade
                        divs = row.find_all('div')
                        for div in divs:
                                Disgrade =""
                                Upgrade=""
                                a_tags = div.find_all('a')
                                if len(a_tags) ==1:
                                   Upgrade=a_tags[0].get_text().lower()
                                   Disgrade=None
                                if len(a_tags) > 1:
                                   Disgrade=a_tags[0].get_text().lower()
                                   for a_tag in a_tags[1:]:
                                           Upgrade += a_tag.get_text().lower()+"/"
# delete balise "a" in all html
                                for s in div('a'):
                                        if(s.find('←') != -1): 
                                                s.extract()
                            
# Insert the data into the table
                                name = cols[0].get_text().lower()
                                rarity = cols[1].get_text().strip().lower()
                                
                                
                                attributes = cols[2].get_text().strip().lower()
                                att_att= attributes.split(" ")[0]
                                
                                att_tab_aff= attributes.split(" ")
                                att_tab2_aff= att_tab_aff[1].split("%")
                                att_aff= att_tab2_aff[0]+"%"
                                
                                attribute = attributes.split("%")[1]
                                                               
                                print(attribute)                                
                                sharpness = cols[3].get_text().strip().lower()
                                slots = cols[4].get_text().strip().lower()
                                rank = cols[5].get_text().strip().lower()
                                price = cols[6].get_text().strip().lower()
                                creation_mats = cols[7].get_text().lower()
                                upgrade_mats = cols[8].get_text().lower()
                                description = cols[9].text.strip()
# Insert the data into the database
                                query_insert = """INSERT INTO """+name_table +""" (name,disgrade,upgrade,rarity,attack, attributes,affinity, sharpness, slots, rank, price, creation_mats, upgrade_mats, description) VALUES (%s,%s,%s,%s,%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"""
                                cursor.execute(query_insert, (name,Disgrade,Upgrade,rarity, att_att,attribute,att_aff, sharpness, slots, rank, price, creation_mats, upgrade_mats, description))
# Commit the changes and close the connection
        conn.commit()
        conn.close()
        
        
        
#*******************************************************************************************************************************************       
        
        

def gunner(url, name_table):   
# Send a GET request to the website
        response = requests.get(url)

# Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

# Extract the table data
        table = soup.find('table')
        rows = table.find_all('tr')

# Connect to the SQLite database
        conn = psycopg2.connect("dbname=test_cranaruge user=postgres password=password port=1130")
        # conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Create the table in the database
        query_create = f"CREATE TABLE IF NOT EXISTS "+name_table+" (name TEXT,previous_Level TEXT,upgrade TEXT, rarity TEXT, attack TEXT, attributes TEXT,affinity TEXT, Reload_Recoil_Bullet_Speed TEXT, ammo TEXT, slots TEXT, rank TEXT, price TEXT, creation_mats TEXT, upgrade_mats TEXT, description TEXT)"
        cursor = conn.cursor()
        cursor.execute(query_create)
        
# extrate data
        for row in rows:
# find all "td" for all data
                cols = row.find_all('td')
                if cols:
# find all div for Upgarde and Disgrade
                        divs = row.find_all('div')
                        for div in divs:
                                Disgrade =""
                                Upgrade=""
                                a_tags = div.find_all('a')
                                if len(a_tags) ==1:
                                   Upgrade=a_tags[0].get_text().lower()
                                   Disgrade=None
                                if len(a_tags) > 1:
                                   Disgrade=a_tags[0].get_text().lower()
                                   for a_tag in a_tags[1:]:
                                           Upgrade += a_tag.get_text().lower()+"/"
# delete balise "a" in all html
                                for s in div('a'):
                                        if(s.find('←') != -1): 
                                                s.extract()
# Insert the data into the table                            
                                name = cols[0].get_text().lower()
                                rarity = cols[1].get_text().strip().lower()
                                
                                
                                
                                attributes = cols[2].get_text().strip().lower()
                                att_att= attributes.split(" ")[0]
                                
                                att_tab_aff= attributes.split(" ")
                                att_tab2_aff= att_tab_aff[1].split("%")
                                att_aff= att_tab2_aff[0]+"%"
                                
                                attribute = attributes.split("%")[1]
                                
                                Reload_Recoil_Bullet_Speed = cols[3].get_text().strip().lower()
                                ammo = cols[4].get_text().strip().lower()
                                slots = cols[5].get_text().strip().lower()
                                rank = cols[6].get_text().strip().lower()
                                price = cols[7].get_text().lower()
                                creation_mats = cols[8].get_text().lower()
                                upgrade_mats = cols[9].text.strip().lower()
                                description = cols[10].text.strip()

# Insert the data into the database
                                query_insert = """INSERT INTO """+name_table +""" (name, previous_Level, upgrade, rarity, attack, attributes, affinity, Reload_Recoil_Bullet_Speed , ammo, slots, rank, price, creation_mats, upgrade_mats, description) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                                cursor.execute(query_insert, (name,Disgrade,Upgrade, rarity, att_att,attribute,att_aff, Reload_Recoil_Bullet_Speed, ammo,slots, rank, price, creation_mats, upgrade_mats, description))
# Commit the changes and close the connection
        conn.commit()
        conn.close()
        
        
        
#******************************************************************************************************************************************* 
        
        
        
def bows(url, name_table):   
# Send a GET request to the website
        response = requests.get(url)

# Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

# Extract the table data
        table = soup.find('table')
        rows = table.find_all('tr')

# Connect to the SQLite database
        conn = psycopg2.connect("dbname=test_cranaruge user=postgres password=password port=1130")

# Create the table in the database
        query_create = f"CREATE TABLE IF NOT EXISTS "+name_table+" (name TEXT,previous_Level TEXT,upgrade TEXT, rarity TEXT,attack TEXT, attributes TEXT,affinity TEXT, charge_stage TEXT, coatings TEXT, slots TEXT, rank TEXT, price TEXT, creation_mats TEXT, upgrade_mats TEXT, description TEXT)"
        cursor = conn.cursor()
        cursor.execute(query_create)
        
# extrate data
        for row in rows:
# find all "td" for all data
                cols = row.find_all('td')
                if cols:
# find all div for Upgarde and Disgrade
                        divs = row.find_all('div')
                        for div in divs:
                                Disgrade =""
                                Upgrade=""
                                a_tags = div.find_all('a')
                                if len(a_tags) ==1:
                                   Upgrade=a_tags[0].get_text().lower()
                                   Disgrade=None
                                if len(a_tags) > 1:
                                   Disgrade=a_tags[0].get_text().lower()
                                   for a_tag in a_tags[1:]:
                                           Upgrade += a_tag.get_text().lower()+"/"
# delete balise "a" in all html
                                for s in div('a'):
                                        if(s.find('←') != -1): 
                                                s.extract()
# Insert the data into the table                            
                                name = cols[0].get_text().strip().lower()
                                rarity = cols[1].get_text().strip().lower()
                                
                                name = cols[0].get_text().lower()
                                rarity = cols[1].get_text().strip().lower()
                                
                                
                                attributes = cols[2].get_text().strip().lower()
                                att_att= attributes.split(" ")[0]
                                
                                att_tab_aff= attributes.split(" ")
                                att_tab2_aff= att_tab_aff[1].split("%")
                                att_aff= att_tab2_aff[0]+"%"
                                
                                attribute = attributes.split("%")[1]
                                
                                
                                attack_attribute = cols[2].get_text().strip().lower()
                                charge_stage = cols[3].get_text().strip().lower()
                                coatings = cols[4].get_text().strip().lower()
                                slots = cols[5].get_text().strip().lower()
                                rank = cols[6].get_text().strip().lower()
                                price = cols[7].get_text().lower()
                                creation_mats = cols[8].get_text().lower()
                                upgrade_mats = cols[9].text.strip().lower()
                                description = cols[10].text.strip()
                        

# Insert the data into the database
                                query_insert = """INSERT INTO """+name_table +"""(name,previous_Level,upgrade, rarity, attack, attributes,affinity, charge_stage , coatings, slots, rank, price, creation_mats, upgrade_mats, description) VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s,%s,%s)"""
                                cursor.execute(query_insert, (name,Disgrade,Upgrade,  rarity,att_att,attribute,att_aff,charge_stage, coatings,slots, rank, price, creation_mats, upgrade_mats, description))
# Commit the changes and close the connection
        conn.commit()
        conn.close()