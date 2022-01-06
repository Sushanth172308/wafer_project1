import shutil
import sqlite3
from os import listdir
import os
import csv
from application_logging.logger import App_Logger
import mysql.connector as connection

class dbOperation:
    '''
    This class shall be used for all the sql operation handeling

    Writeen By: Sushanth
    version: 1.0
    Revisions: None

    '''

    def __init__(self):
        self.path = 'Prediction_Database'
        self.badFilePath = 'Prediction_Raw_Files_Validated/Bad_Raw'
        self.goodFilePath = 'Prediction_Raw_Files_Validated/Good_Raw'
        self.logger = App_Logger()


        def dataBaseConnection(self,Databasename):
            '''
            Method name: dataBaseConnection
            Description:This method creates the datacase with the given name if the database already exists then opens the connection to the database
            Output: Connection to the DB
            on Failure: Raise connectionError

            Written by :Sushanth
            version:1.0
            Revisions :None

            '''

            try:
                conn = sqlite3.Connect(self.path+DatabaseName+'.db')
                file = open('Prediction_Logs/DataBaseConnectionLog.txt','a+')
                self.logger.log(file,'opened %s database successfully' %DatabaseNname)
                file.close()
            except ConnectionError:
                file = open('')
