import mysql.connector
from configparser import ConfigParser
from contextlib import closing
import logging
import csv


class DBLoadSetup():
    conn = mysql.connector.connect()

    def __init__(self, tname="sample"):
        self.tname = tname

    def dbConnect(self):
        config = ConfigParser()
        config.read('../config/config.ini')
        host = config.get('DATABASE', 'HOST')
        username = config.get('DATABASE', 'USERNAME')
        password = config.get('DATABASE', 'PASSWORD')
        db = config.get('DATABASE', 'DB')
        logging.info("Initializing database connection... ")
        try:
            self.conn = mysql.connector.connect(host=host, user=username, passwd=password, database=db, pool_size=5)
            logging.info("Database connection is established with {}".format(self.conn))
        except mysql.connector.Error as error:
            logging.error("Failed to connect database {}".format(error))

        logging.info("Connection is available. {} ".format(self.conn))
        return self.conn

    def dropTableIfExist(self):
        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor()
                drop_query = "DROP TABLE IF EXISTS {}".format('sample')
                result = cursor.execute(drop_query)
                logging.info("Table {} is dropped from database. {} ".format(self.tname, result))
                self.conn.commit()
            else:
                logging.warning("Connection is not available. {} ".format(self.conn.is_connected()))
        except Exception as e:
            logging.error('Something went wrong... {}'.format(str(e)))



    def createTable(self):
        if self.conn.is_connected():
            cursor = self.conn.cursor()
            create_query = """create table IF NOT EXISTS {} (
                                            marketplace varchar (25),
                                            customer_id varchar (30),
                                            review_id varchar (255),
                                            product_id varchar (100),
                                            product_parent varchar (50),
                                            product_title text,
                                            product_category varchar (25),
                                            star_rating varchar (50),
                                            helpful_votes varchar (50),
                                            total_votes varchar (25),
                                            vine varchar (50),
                                            verified_purchase  varchar (50),
                                            review_headline varchar (100),
                                            review_body text,
                                            review_date varchar (25))""".format(self.tname)
            result = cursor.execute(create_query)
            logging.info("Table {} is created in database. {} ".format(self.tname, result))
            self.conn.commit()
        else:
            logging.warning("Connection is not available. {} ".format(self.conn.is_connected()))


    def loadData(self):
        records_to_insert = list()
        if self.conn is None:
            self.conn = self.dbConnect()

        try:
            if self.conn.is_connected():
                cursor = self.conn.cursor()
                insert_query = """INSERT INTO sample(marketplace,	
                                                        customer_id,	
                                                        review_id,	
                                                        product_id,	
                                                        product_parent,	
                                                        product_title,	
                                                        product_category,	
                                                        star_rating	,
                                                        helpful_votes,	
                                                        total_votes,	
                                                        vine,	
                                                        verified_purchase,	
                                                        review_headline,	
                                                        review_body,	
                                                        review_date) 
                VALUES (%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s,%s) """
                cursor = self.conn.cursor()

                with open("../data/downloads/sample_us.tsv") as fd:
                    rd = csv.reader(fd, delimiter="\t")
                    for row in rd:
                        logging.info("Row to be inserted {}".format(row))
                        records_to_insert.append(tuple(row))

                logging.info("Records to be inserted {}".format(records_to_insert))
                cursor.executemany(insert_query, records_to_insert)

                self.conn.commit()
                logging.info("{} record inserted successfully into Sample table ".format(cursor.rowcount))
        except mysql.connector.Error as error:
            logging.error("Failed to insert record into MySQL table {}".format(error))


    def loadrunner(self):
        try:
            self.dbConnect()
            self.dropTableIfExist()
            self.createTable()
            self.loadData()
        except Exception as e:
            logging.error('Something went wrong... {}'.format(str(e)))
        finally:
            if (self.conn.is_connected()):
                self.conn.close()
                logging.info("Database connection is closed successfully.")
