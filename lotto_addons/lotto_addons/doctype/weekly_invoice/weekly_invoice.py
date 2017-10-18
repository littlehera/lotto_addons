# -*- coding: utf-8 -*-
# Copyright (c) 2017, littlehera and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

class WeeklyInvoice(Document):
	pass

@frappe.whitelist()
def get_weekly_sales_orders(date, retailer):
	data = []
	date = datetime.strptime(date, '%Y-%m-%d')
	start = date - timedelta(days = date.weekday())
	date = start + timedelta (days = 6)
	print start.day, start, date.day, date
	for so in frappe.db.sql("""Select name from 	`tabSales Order` where customer = %s and transaction_date <= %s
		and transaction_date >= %s""", (retailer, date, start)):
		so_dict = dict()
		doc = frappe.get_doc("Sales Order", so[0])
		so_dict["so"] = doc.name
		so_dict["date"] = doc.transaction_date
		so_dict["tpm"] = doc.pos_no
		so_dict["sales"] = doc.grand_total
		data.append(so_dict)
	return data