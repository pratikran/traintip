#!/usr/bin/env python

#Filename dbinsert.py


import sys, os, re
sys.path.append(os.getcwd())
from parseStnCode import parseStnCodePage
from IrFunctions import TRN_STN_CODE_MAP_URL, getTrainStationCodeMap
import sqlite3

db_filename = 'stncodenamemap.db'

db_is_new = not os.path.exists(db_filename)
conn = sqlite3.connect(db_filename)
c = conn.cursor()

if db_is_new:
    print 'Need to create schema'

    # Create table
    c.execute('''CREATE TABLE stn_code_name_map
                 (stn_code text, stn_name text)''')

    GLOBAL_MAP = []

    for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        response = getTrainStationCodeMap(TRN_STN_CODE_MAP_URL,'START_STR','STN_NAME',letter,'Please Wait...')
        pnr_response_text = response.text
        GLOBAL_DICT = {}
        GLOBAL_DICT.update(parseStnCodePage(pnr_response_text))
        for stncode in GLOBAL_DICT:
            GLOBAL_MAP.append((stncode, GLOBAL_DICT[stncode]))

    #print GLOBAL_DICT, 'GLOBAL_DICT: ',len(GLOBAL_DICT)
    c.executemany('INSERT INTO stn_code_name_map VALUES (?,?)', GLOBAL_MAP)

else:
    print 'Database exists, assume schema does, too.'

    #print len(GLOBAL_MAP)
    c.execute("select * from stn_code_name_map")
    print c.fetchall()

conn.commit()
conn.close()


