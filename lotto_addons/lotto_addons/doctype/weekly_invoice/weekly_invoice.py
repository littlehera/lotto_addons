# -*- coding: utf-8 -*-
# Copyright (c) 2017, littlehera and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from datetime import date, datetime, timedelta
from dateutil.relativedelta import relativedelta

class WeeklyInvoice(Document):
	def validate(self):
		items = self.items
		self.net_due, self.t_sales, self.t_discounts, self.t_prizes, self.t_pdiscounts= 0,0,0,0,0
		for item in items:
			self.net_due += item.totals
			self.t_sales += item.sales
			self.t_discounts += item.discount
			self.t_prizes += item.prizes
			self.t_pdiscounts += item.prizes_discount

	pass

@frappe.whitelist()
def get_weekly_sales_orders(from_date, to_date, retailer):
	data = []
	from_date = datetime.strptime(from_date, '%Y-%m-%d')
	to_date = datetime.strptime(to_date, '%Y-%m-%d')
	for so in frappe.db.sql("""Select name from `tabSales Order` where customer = %s and transaction_date >= %s
		and transaction_date <= %s""", (retailer, from_date, to_date)):
		so_dict = dict()
		doc = frappe.get_doc("Sales Order", so[0])
		so_dict["so"] = doc.name
		so_dict["date"] = doc.transaction_date
		print "========+RETAILER=============="
		print retailer
		disc = frappe.get_doc("Customer", retailer).retailer_discount
		#discount = retailer.discount
		print disc

		#Discount = (net sales / 1.16) x .09 or .07
		so_dict["tpm"] = doc.pos_no
		so_dict["sales"] = doc.net_sales
		so_dict["discount"] = (doc.net_sales/1.16) * (disc/100)
		so_dict["sales_totals"] = (float(doc.net_sales) - (doc.net_sales/1.16 * disc))
		so_dict["prizes"] = doc.payout
		so_dict["prizes_discount"] = (doc.payout * 0.02)
		so_dict["prizes_totals"]= -1*(float(doc.payout)+(doc.payout * 0.02))
		draw = frappe.db.sql("""SELECT parent from `tabDraw Dates` where date = %s LIMIT 1""", doc.transaction_date)
		so_dict["draw_id"] = draw[0][0]

		data.append(so_dict)
	return data

@frappe.whitelist()
def get_to_date(date):
	date = datetime.strptime(date, '%Y-%m-%d')
	return (date + timedelta (days = 6))