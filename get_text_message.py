#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
from collections import Counter

FILENAME = r'e:\16722145022.txt'
RESULT = {}
CARDID = 2555

def get_text():
	RESULT['data'] = []
	
	with open(FILENAME, 'r')as f:
		for line in f:
			message = {}
			line_message = line.strip('\n').split()
			number = line_message[0]
			time = line_message[1] + ' ' + line_message[2]
			text = line_message[3].replace('"', '')
			if len(line_message) > 5:
				location = line_message[4]
			if len(line_message) > 6:
				type = line_message[5]
			if len(line_message) == 7:
				status = line_message[6]
				
			message['number'] = number
			message['time'] = time
			message['text'] = text
			message['location'] = location
			message['type'] = type
			message['status'] = status
			RESULT['data'].append(message)

def print_result():
	# title
	print('卡尾号\t日期\t时间\t类别\t金额\t余额\t备注')
	print('-' * 57)
	
	# data
	for msg in RESULT['data']:
		# get message year, month, day and time
		id = CARDID
		date = msg['time'].split()[0]
		time = msg['time'].split()[1]
		type = None
		cost = None
		total = None
		comment = ''
		
		if '余额' in msg['text'] and ('支出' in msg['text'] or '收入' in msg['text']):
			# get remaining count
			tmp = re.findall(r'余额.*元', msg['text'])[0]
			total = tmp.replace('余额', '').replace('元', '')
			
			# get type and cash number
			tmp = re.findall(r'[收入|支出].*元', msg['text'])[0].replace(',', '')
			if '支出' in tmp:
				type = '支出'
				tmp = tmp.replace('支出', '')
			if '收入' in tmp:
				type = '收入'
				tmp = tmp.replace('收入', '')
			cost = re.findall(r'\d+', tmp)[0]
			print(str(id) + '\t' + date + '\t' + time + '\t' + type + '\t' + cost + '\t' 
			+ total + '\t' + comment)

def main():
	get_text()
	print_result()

if __name__ == '__main__':
	main()