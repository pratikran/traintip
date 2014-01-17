#!/usr/bin/env python

#Filename parseStnCode.py

import sys, os, re
sys.path.append(os.getcwd())
import requests as r
from random import sample
from IrFunctions import TRN_STN_CODE_MAP_URL, getTrainStationCodeMap

def parseStnCodePage(stncode_html_text):
    #print stncode_html_text
    text_line = ''
    td_text = ''
    table_tag_flag = 0
    tr_tag_flag = 0
    td_tag_flag = 0
    stn_name_code_map = {}
    #sprint stncode_html_text
    for letter in stncode_html_text:
        text_line = text_line + letter
        #print text_line
        if letter == '\n':
            #print text_line
            text_line = text_line.strip()
            lower_text = text_line.lower()
            table_tag_open_pos = lower_text.find('<table ')
            table_tag_close_pos = lower_text.find('</table>')
            table_class_pos = lower_text.find('class=\"table_border_both\"')
            if table_tag_open_pos > -1 and table_class_pos > -1: table_tag_flag = 1
            if table_tag_close_pos > -1: table_tag_flag = 0
            if table_tag_flag == 1:
                #print "ABC"
                tr_tag_open_pos = lower_text.find('<tr>')
                tr_tag_close_pos = lower_text.find('</tr>')
                if tr_tag_open_pos > -1 and table_tag_open_pos == -1:
                    #print "XYZ"
                    tr_tag_flag = 1
                    td_seq_flag = 0
                    stn_name_code_pair = ['','']
                if tr_tag_close_pos > -1:
                    tr_tag_flag = 0
                    td_seq_flag = 0
                if tr_tag_flag == 1 and tr_tag_open_pos == -1:
                    #print text_line,
                    td_tag_open_pos = lower_text.find('<td')
                    td_tag_close_pos = lower_text.find('</td>')
                    if td_tag_open_pos > -1:
                        #print td_seq_flag
                        td_seq_flag += 1
                        #print td_seq_flag
                        td_tag_flag = 1
                        td_text = text_line[text_line.find('>')+1:]
                        #print td_text,'1'
                        if td_tag_close_pos > -1:
                            td_tag_flag = 0
                            #print td_seq_flag
                            #print td_text,'11'
                            td_text = td_text[0:td_text.find('<')].strip()
                            stn_name_code_pair[td_seq_flag-1] = td_text
                            #print td_text,'2',td_text.find('<')
                            if td_seq_flag == 2:
                                stn_name_code_map[stn_name_code_pair[1]] = stn_name_code_pair[0]
                                #print stn_name_code_pair
                    elif td_tag_open_pos == -1 and td_tag_close_pos > -1:
                        td_tag_flag = 0
                        td_text = td_text + text_line[0:text_line.find('<')].strip()
                        stn_name_code_pair[td_seq_flag-1] = td_text
                        if td_seq_flag == 2:
                            stn_name_code_map[stn_name_code_pair[1]] = stn_name_code_pair[0]
                            #print stn_name_code_pair
                    else:
                        td_text = td_text + text_lines
            text_line = ''
    return stn_name_code_map

##GLOBAL_DICT = {}
###print pnr_response_text                    
##for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
##    response = getTrainStationCodeMap(TRN_STN_CODE_MAP_URL,'START_STR','STN_NAME',letter,'Please Wait...')
##    pnr_response_text = response.text
##    GLOBAL_DICT.update(parseStnCodePage(pnr_response_text))
##
###print GLOBAL_DICT, 'GLOBAL_DICT: ',len(GLOBAL_DICT)
