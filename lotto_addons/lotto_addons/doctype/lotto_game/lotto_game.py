# -*- coding: utf-8 -*-
# Copyright (c) 2017, littlehera and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import date, datetime, timedelta
import calendar, re

class LottoGame(Document):
	pass

@frappe.whitelist()
def get_dates(start_date, draw_days):
	start_date = datetime.strptime(start_date, '%Y-%m-%d')
	end_date = start_date + timedelta(days=6)
	date_temp = start_date
	data = []
	print "=======+GET DATES+=========="
	print start_date, end_date
	days = re.split(',', draw_days)
	while date_temp <= end_date:
		temp = dict()
		day_str = str(calendar.day_name[date_temp.weekday()])
		if day_str in days:
			temp["day"] = day_str
			temp["date"] = date_temp
			days.remove(day_str)
			data.append(temp)
		date_temp = date_temp + timedelta(days=1)
	draw_no = str(get_draw_no()).zfill(4)
	return data, draw_no


def get_draw_no():
	draws = frappe.db.sql("""SELECT name, draw_no from `tabLotto Game` ORDER BY name desc LIMIT 1""")
	for draw in draws:
		print draw[1]
