from app.getdata import ReviewsDownloader
from app.dbload import DBLoadSetup
from app.queries import ReviewQueries
from configparser import ConfigParser
import logging

config = ConfigParser()
config.read('../config/config.ini')
url = config.get('URLS', 'URL')


def downloadfile():
    reviewsDownloader = ReviewsDownloader(url)
    reviewsDownloader.checkAndDownloadData()

def dbload():
    dbsetup = DBLoadSetup()
    dbsetup.loadrunner()

def dbqueries():
    rqueries = ReviewQueries()
    rqueries.queryrunner()

def main():
    logging.basicConfig(format='%(levelname)s %(asctime)s :: %(message)s',filename='../logs/myapp.log', level=logging.INFO)
    logging.info('Starting application...')
    downloadfile()
    dbload()
    dbqueries()
    logging.info('Application Finished.')


if __name__ == "__main__":
    main()