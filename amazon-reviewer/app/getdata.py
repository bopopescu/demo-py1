import requests
import urllib3
from urllib3.exceptions import InsecureRequestWarning
import logging

logging.getLogger("urllib3").setLevel(logging.WARNING)


class ReviewsDownloader():
    def __init__(self,url):
        self.url = url

    def checkURL(self):
        if self.url is not None:
            response = requests.get(self.url)
            logging.info("URL {} to download data from.".format(self.url))
            logging.info("Checking status of given URL ...")
            if response.status_code == 200:
                logging.info("Success! {}".format( response.status_code))
            elif response.status_code == 404:
                logging.info("Not Found! ", response.status_code)
            else:
                logging.info("Something went wrong URL {} with status ".format(self.url,response.status_code))

    def downloadData(self):
        manager = urllib3.PoolManager()
        urllib3.disable_warnings(InsecureRequestWarning)
        response = urllib3.response.HTTPResponse()

        try:
            response = manager.request('GET', self.url, preload_content=False)
        except urllib3.exceptions.NewConnectionError as err:
            logging.error('Connection failed- {}'.format(str(err)))
        except urllib3.exceptions.MaxRetryError as err:
            logging.error('Connection failed, Maximum retry occured {}'.format(str(err)))

        if response is not None:
            try:
                with open('../data/downloads/sample_us.tsv', 'wb') as out:
                    while True:
                        data = response.read()
                        if not data:
                            break
                        out.write(data)
            except FileNotFoundError as err:
                logging.error('Trying to download file {}'.format(str(err)))
            except Exception as err:
                logging.error('Downloading file failed due to {}'.format(str(err)))
            finally:
                response.release_conn()
        response.release_conn()

    def checkAndDownloadData(self):
        self.checkURL()
        self.downloadData()