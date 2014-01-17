#!/usr/bin/env python

#Filename IrFunctions.py

import sys, os, re
sys.path.append(os.getcwd())
import requests as r
from random import sample

PNR_STATUS_URL="http://www.indianrail.gov.in/cgi_bin/inet_pnrstat_cgi.cgi"
TRN_BTW_IMP_STNS_URL="http://www.indianrail.gov.in/cgi_bin/inet_srcdest_cgi_time.cgi"
TRN_SCH_URL="http://www.indianrail.gov.in/cgi_bin/inet_trnnum_cgi.cgi"
SEAT_AVLBLTY_URL="http://www.indianrail.gov.in/cgi_bin/inet_accavl_cgi.cgi"
FAIR_ENQ_URL="http://www.indianrail.gov.in/cgi_bin/inet_frenq_cgi.cgi"
TRN_STN_CODE_MAP_URL="http://www.indianrail.gov.in/cgi_bin/inet_stncode_cgi.cgi"

headers = {
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
               ,'Accept-Encoding':'gzip, deflate'
               ,'Accept-Language':'en-US,en;q=0.5'
               ,'Connection':'keep-alive'
               ,'Host':'www.indianrail.gov.in'
               ,'Referer':''
               ,'User-Agent':'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:26.0) Gecko/20100101 Firefox/26.0'
           }


def get_5digit_random_number():
    return "".join(sample('1234567890',5))

def getPnrStatus(URL,lccp_cap_val,lccp_capinp_val,lccp_pnrno1,submit):
    headers['Referer'] = 'http://www.indianrail.gov.in/pnr_Enq.html'
    data = {
                'lccp_cap_val':lccp_cap_val
               ,'lccp_capinp_val':lccp_capinp_val
               ,'lccp_pnrno1':lccp_pnrno1
               ,'submit':submit
           }
    request = r.post(URL, data=data, headers=headers)
    return request
"""
def getTrnsBtwImpStations(URL,CurrentDate,CurrentMonth,CurrentYear,lccp_ari_time,lccp_arib_time,lccp_classopt,lccp_day,lccp_dep_time,lccp_depb_time,lccp_dstn_stncode,lccp_month,lccp_ret_day,lccp_ret_month,lccp_src_stncode,lccp_trn_type,monitor,submit2):
    headers['Referer'] = 'http://www.indianrail.gov.in/between_Imp_Stations.html'
    data = {
             'CurrentDate':CurrentDate
            ,'CurrentMonth':CurrentMonth
            ,'CurrentYear':CurrentYear
            ,'lccp_ari_time':lccp_ari_time
            ,'lccp_arib_time':lccp_arib_time
            ,'lccp_classopt':lccp_classopt
            ,'lccp_day':lccp_day
            ,'lccp_dep_time':lccp_dep_time
            ,'lccp_depb_time':lccp_depb_time
            ,'lccp_dstn_stncode':lccp_dstn_stncode
            ,'lccp_month':lccp_month
            ,'lccp_ret_day':lccp_ret_day
            ,'lccp_ret_month':lccp_ret_month
            ,'lccp_src_stncode':lccp_src_stncode
            ,'lccp_trn_type':lccp_trn_type
            ,'monitor':monitor
            ,'submit2':submit2
            }
    response = r.post(URL, data=data, headers=headers)
    return response

def getTrnSchedule(URL,getIt,lccp_trnname):
    headers['Referer'] = 'http://www.indianrail.gov.in/train_Schedule.html'
    data = {
             'getIt':getIt
            ,'lccp_trnname':lccp_trnname
            }
    response = r.post(URL, data=data, headers=headers)
    return response

def getSeatAvailability(URL,lccp_class1,lccp_class2,lccp_class3,lccp_class4,lccp_class5,lccp_class6,lccp_class6_1,lccp_class7,lccp_class7_1,lccp_classopt,lccp_day,lccp_dstncode,lccp_month,lccp_quota,lccp_srccode,lccp_trnno,submit):
    headers['Referer'] = 'http://www.indianrail.gov.in/train_Schedule.html'
    data = {
                'lccp_class1':lccp_class1
                ,'lccp_class2':lccp_class2
                ,'lccp_class3':lccp_class3
                ,'lccp_class4':lccp_class4
                ,'lccp_class5':lccp_class5
                ,'lccp_class6':lccp_class6
                ,'lccp_class6':lccp_class6_1
                ,'lccp_class7':lccp_class7
                ,'lccp_class7':lccp_class7_1
                ,'lccp_classopt':lccp_classopt
                ,'lccp_day':lccp_day
                ,'lccp_dstncode':lccp_dstncode
                ,'lccp_month':lccp_month
                ,'lccp_quota':lccp_quota
                ,'lccp_srccode':lccp_srccode
                ,'lccp_trnno':lccp_trnno
                ,'submit':submit
            }
    response = r.post(URL, data=data, headers=headers)
    return response

def getTrainFair(URL,getIt,lccp_age,lccp_classopt,lccp_conc,lccp_day,lccp_disp_avl_flg,lccp_dstncode,lccp_enrtcode,lccp_frclass1,lccp_frclass2,lccp_frclass3,lccp_frclass4,lccp_frclass5,lccp_frclass6,lccp_frclass7,lccp_month,lccp_srccode,lccp_trnno,lccp_viacode):
    headers['Referer'] = 'http://www.indianrail.gov.in/fare_Enq.html'
    data = {
                'getIt':getIt
                ,'lccp_age':lccp_age
                ,'lccp_classopt':lccp_classopt
                ,'lccp_conc':lccp_conc
                ,'lccp_day':lccp_day
                ,'lccp_disp_avl_flg':lccp_disp_avl_flg
                ,'lccp_dstncode':lccp_dstncode
                ,'lccp_enrtcode':lccp_enrtcode
                ,'lccp_frclass1':lccp_frclass1
                ,'lccp_frclass2':lccp_frclass2
                ,'lccp_frclass3':lccp_frclass3
                ,'lccp_frclass4':lccp_frclass4
                ,'lccp_frclass5':lccp_frclass5
                ,'lccp_frclass6':lccp_frclass6
                ,'lccp_frclass7':lccp_frclass7
                ,'lccp_month':lccp_month
                ,'lccp_srccode':lccp_srccode
                ,'lccp_trnno':lccp_trnno
                ,'lccp_viacode':lccp_viacode
            }
    response = r.post(URL, data=data, headers=headers)
    return response
"""

def getPnrDetails(pnr_response_text):
    re_pnr_enquiry_record = re.compile('<td .*class=\"Enq_heading\"', re.IGNORECASE)
    re_table_tag_open = re.compile('<table .*class=\"table_border\"', re.IGNORECASE)
    re_table_tag_close = re.compile('</table>', re.IGNORECASE)
    re_td_tag_record = re.compile('<td .*?>.*?</td>', re.IGNORECASE)
    re_td_tag_record_content = re.compile('>[^><].+?<')

    table_counter = 0
    query_header_counter = 0
    journey_detail_counter = 0
    journey_detail_header_counter = 0
    booking_counter = 0
    booking_passenger_counter = 0
    charting_status_counter = 0

    text_line = ''    
    pnr = ''
    journey_detail_headers = []
    booking_header = []
    booking_data = []
    charting_header = ''
    pnr_details = {}
    
    for letter in pnr_response_text:
        text_line = text_line + letter
        if letter == '\n':
            text_line = re.sub('<br>|<BR>|</br>|</BR>','',text_line)
            
            if re_pnr_enquiry_record.search(text_line):
                query_header_counter += 1
            elif query_header_counter >= 1 and text_line.lower().find('</td>') == -1:
                pnr = re.sub('pnr|PNR|Number|number|NUMBER|:|[ ]*','',text_line.strip())
                pnr_details[unicode('pnr')] = pnr
                query_header_counter = 0
                
            if re_table_tag_open.search(text_line):
                table_counter = 1
            elif re_table_tag_close.search(text_line):
                table_counter = 0            

            if table_counter == 1:
                td_tag_record = re_td_tag_record.search(text_line)
                if td_tag_record:
                    value = re_td_tag_record_content.search(text_line).group().strip('>|<|\*').strip()
                    if value.lower().find('journey') > -1 and value.lower().find('details') > -1:
                        journey_detail_counter = 1
                    elif value.lower().find('s.') > -1 and value.lower().find('no.') > -1:
                        booking_counter = 1
                    elif value.lower().find('charting') > -1:
                        charting_status_counter = 1
                        charting_header = re.sub(r'[ ]+',r'',value).lower()
                        charting_status = {}

                    if journey_detail_counter == 1:
                        if journey_detail_header_counter >= 1 and journey_detail_header_counter < 9:
                            value = re.sub(r'[ ]+',r'_',value).lower()
                            if value.find('boarding_date') > -1: value = re.sub(r'[_][(]',r'(',value)
                            journey_detail_headers.append(value)
                            journey_detail_header_counter += 1
                        elif journey_detail_counter == 1 and journey_detail_header_counter >= 9 and journey_detail_header_counter < 17:
                            if journey_detail_headers[journey_detail_header_counter - 9].find('boarding_date') > -1: value = re.sub(r'[ ]+',r'',value)
                            pnr_details[journey_detail_headers[journey_detail_header_counter - 9]] = value
                            journey_detail_header_counter += 1
                        elif journey_detail_header_counter == 0:
                            journey_detail_header_counter = 1
                        else:
                            journey_detail_counter = 0
                    
                    if booking_counter >= 1:
                        if booking_counter <= 3 and booking_passenger_counter == 0:
                            booking_counter += 1
                            booking_header.append(re.sub(r'[ ]+',r'',value).lower())
                        elif value.lower().find('passenger') > -1 and booking_passenger_counter == 0:
                            booking_counter = 1
                            booking_passenger_counter += 1
                            booking_record = {}
                        elif booking_passenger_counter == 1 and booking_counter < 3:
                            booking_record[booking_header[booking_counter]] = value
                            booking_counter += 1                     
                            if booking_counter == 3:
                                booking_data.append(booking_record)
                                pnr_details[unicode('passengers')] = booking_data
                                booking_passenger_counter = 0
                                booking_counter = 4
                        else:
                            booking_passenger_counter = 0
                            booking_counter = 0


                    if charting_status_counter == 1:
                        pnr_details[charting_header] = value
                        charting_status_counter = 0
                        
            text_line = ''

    return pnr_details

def getTrainStationCodeMap(URL,lccp_SearchType,lccp_choice,lccp_stnname,submit):
    headers['Referer'] = 'http://www.indianrail.gov.in/stn_Code.html'
    data = {
                'lccp_SearchType':lccp_SearchType
               ,'lccp_choice':lccp_choice
               ,'lccp_stnname':lccp_stnname
               ,'submit':submit
           }
    request = r.post(URL, data=data, headers=headers)
    return request

random_num = get_5digit_random_number()
#response = getPnrStatus(PNR_STATUS_URL,random_num,random_num,4711817856,'Wait For PNR Enquiry!')
#response  = getTrnsBtwImpStations(TRN_BTW_IMP_STNS_URL,19,4,2006,0,24,'SL',20,0,24,'BCT',12,20,12,'NDLS','Z','ON','Please Wait...')
#reponse = getTrnSchedule(TRN_SCH_URL,'Please Wait...',12138)
#reponse = getSeatAvailability(SEAT_AVLBLTY_URL,'SL','ZZ','ZZ','ZZ','ZZ','ZZ','ZZ','ZZ','ZZ','ZZ',20,'CSTM',12,'GN','NDLS',12138,'Please Wait...')
#response = getTrainFair(FAIR_ENQ_URL,'Please Wait...',30,'SL','ZZZZZZ',20,1,'CSTM','NONE','ZZ','ZZ','ZZ','ZZ','ZZ','ZZ','ZZ',12,'NDLS',12138,'NONE')
#response = getTrainStationCodeMap(TRN_STN_CODE_MAP_URL,'START_STR','STN_NAME','A','Please Wait...')

#pnr_response_text = response.text
#print pnr_response_text
#print getPnrDetails(pnr_response_text)
