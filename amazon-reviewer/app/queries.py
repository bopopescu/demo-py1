import mysql.connector
from configparser import ConfigParser
from contextlib import closing
import logging
import csv
from app.dbload import DBLoadSetup

class ReviewQueries():
    conn = mysql.connector.connect()

    def __init__(self, tname="sample"):
        self.tname = tname

    def selectdata(self):
        conn = DBLoadSetup().dbConnect()
        try:
            if conn.is_connected():
                cursor = conn.cursor()
                select_query = "select * from {}".format('sample')
                result = cursor.execute(select_query)
                records = cursor.fetchall()
                if len(records) == 0:
                    logging.info("Table {} is selected from database with {} records".format(self.tname, len(records)))
                else:
                    logging.info("Table {} is selected from database with {} records".format(self.tname, len(records)))

                if records is not None:
                    try:
                        fp = open('../data/queries/sample_result.csv', 'w')
                        myFile = csv.writer(fp)
                        myFile.writerows(records)
                        logging.info("Record from {} query are successfully exported to {} file.".format(self.tname, fp.name))
                    except FileNotFoundError as err:
                        logging.error('Trying to download file {}'.format(str(err)))
                    except Exception as err:
                        logging.error('Exporting data to file failed due to {}'.format(str(err)))
                    finally:
                        fp.close()
                        logging.info("File {} is closed successfully.".format(fp.name))
                else:
                    logging.warning("Connection is not available. {} ".format(conn.is_connected()))
        except Exception as e:
            logging.error('Something went wrong... {} '.format(str(e)))


    def queryrunner(self):
        try:
            self.selectdata()
        except Exception as e:
            logging.error('Something went wrong... {}'.format(str(e)))
        finally:
            if (self.conn.is_connected()):
                self.conn.close()
                logging.info("Database connection is closed successfully.")