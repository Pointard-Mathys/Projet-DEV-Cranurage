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
        conn = psycopg2.connect("dbname=cranaruge user=postgres password=root")

        # conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Create the table in the database
        query_create = f"CREATE TABLE IF NOT EXISTS "+name_table+" (name TEXT, rarity TEXT, attributes TEXT, sharpness TEXT, slots TEXT, rank TEXT, price TEXT, creation_mats TEXT, upgrade_mats TEXT, description TEXT)"
        cursor = conn.cursor()
        cursor.execute(query_create)
        
# Insert the data into the table
        for row in rows:
                cols = row.find_all('td')
                if cols:
                        name = cols[0].get_text().strip()
                        rarity = cols[1].get_text().strip()
                        attributes = cols[2].get_text().strip()
                        sharpness = cols[3].get_text().strip()
                        slots = cols[4].get_text().strip()
                        rank = cols[5].get_text().strip()
                        price = cols[6].get_text().strip()
                        creation_mats = cols[7].get_text()
                        upgrade_mats = cols[8].get_text()
                        description = cols[9].text.strip()

# Insert the data into the database
                        query_insert = """INSERT INTO """+name_table +""" (name,rarity, attributes, sharpness, slots, rank, price, creation_mats, upgrade_mats, description) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"""
                        cursor.execute(query_insert, (name, rarity, attributes, sharpness, slots, rank, price, creation_mats, upgrade_mats, description))
# Commit the changes and close the connection
        conn.commit()
        conn.close()
        
        
        
        
        
        

def artilleur(url, name_table):   
# Send a GET request to the website
        response = requests.get(url)

# Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

# Extract the table data
        table = soup.find('table')
        rows = table.find_all('tr')

# Connect to the SQLite database
        conn = psycopg2.connect("dbname=cranaruge user=postgres password=root")
        # conn = mysql.connector.connect(host=host, user=user, password=password, database=database)

# Create the table in the database
        query_create = f"CREATE TABLE IF NOT EXISTS "+name_table+" (name TEXT, rarity TEXT, attack TEXT, Reload_Recoil_Bullet_Speed TEXT, ammo TEXT, slots TEXT, rank TEXT, price TEXT, creation_mats TEXT, upgrade_mats TEXT, description TEXT)"
        cursor = conn.cursor()
        cursor.execute(query_create)
        
# Insert the data into the table
        for row in rows:
                cols = row.find_all('td')
                if cols:
                        name = cols[0].get_text().strip()
                        rarity = cols[1].get_text().strip()
                        attack = cols[2].get_text().strip()
                        Reload_Recoil_Bullet_Speed = cols[3].get_text().strip()
                        ammo = cols[4].get_text().strip()
                        slots = cols[5].get_text().strip()
                        rank = cols[6].get_text().strip()
                        price = cols[7].get_text()
                        creation_mats = cols[8].get_text()
                        upgrade_mats = cols[9].text.strip()
                        description = cols[10].text.strip()

# Insert the data into the database
                        query_insert = """INSERT INTO """+name_table +""" (name, rarity, attack , Reload_Recoil_Bullet_Speed , ammo, slots, rank, price, creation_mats, upgrade_mats, description) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"""
                        cursor.execute(query_insert, (name, rarity, attack, Reload_Recoil_Bullet_Speed, ammo,slots, rank, price, creation_mats, upgrade_mats, description))
# Commit the changes and close the connection
        conn.commit()
        conn.close()
        
        
        
        
        
        
        
def bows(url, name_table):   
# Send a GET request to the website
        response = requests.get(url)

# Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

# Extract the table data
        table = soup.find('table')
        rows = table.find_all('tr')

# Connect to the SQLite database
        conn = psycopg2.connect("dbname=cranaruge user=postgres password=root")

# Create the table in the database
        query_create = f"CREATE TABLE IF NOT EXISTS "+name_table+" (name TEXT, rarity TEXT, attack_attribute TEXT, charge_stage TEXT, coatings TEXT, slots TEXT, rank TEXT, price TEXT, creation_mats TEXT, upgrade_mats TEXT, description TEXT)"
        cursor = conn.cursor()
        cursor.execute(query_create)
        
# Insert the data into the table
        for row in rows:
                cols = row.find_all('td')
                if cols:
                        name = cols[0].get_text().strip()
                        rarity = cols[1].get_text().strip()
                        attack_attribute = cols[2].get_text().strip()
                        charge_stage = cols[3].get_text().strip()
                        coatings = cols[4].get_text().strip()
                        slots = cols[5].get_text().strip()
                        rank = cols[6].get_text().strip()
                        price = cols[7].get_text()
                        creation_mats = cols[8].get_text()
                        upgrade_mats = cols[9].text.strip()
                        description = cols[10].text.strip()

# Insert the data into the database
                        query_insert = """INSERT INTO """+name_table +""" (name, rarity, attack_attribute, charge_stage , coatings, slots, rank, price, creation_mats, upgrade_mats, description) VALUES (%s,%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)"""
                        cursor.execute(query_insert, (name, rarity, attack_attribute,charge_stage, coatings,slots, rank, price, creation_mats, upgrade_mats, description))
# Commit the changes and close the connection
        conn.commit()
        conn.close()