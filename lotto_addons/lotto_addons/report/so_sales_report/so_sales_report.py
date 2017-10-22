# Copyright (c) 2013, littlehera and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe

def execute(filters=None):
	print "==========EXECUTE============"
	data = []
	columns = [{"label": "Date", 'width': 100, "fieldname": "date"},
			   {"label": "POS No.", 'width': 80, "fieldname": "pos_no"},
			   {"label": "Retailer", 'width': 200, "fieldname": "retailer"},
			   {"label": "Tickets", 'width': 80, "fieldname": "tickets", "fieldtype":"Int"},
			   {"label": "Gross Sales", 'width': 150, "fieldname": "gross_sales", "fieldtype":"Currency", "precision": 2},
			   {"label": "Cancels", 'width': 80, "fieldname": "cancels"},
			   {"label": "Payout", 'width': 80, "fieldname": "payout"},
			   {"label": "Net Sales", 'width': 130, "fieldname": "net_sales", "fieldtype":"Currency", "precision": 2},
			   {"label": "Net Due", 'width': 130, "fieldname": "net_due", "fieldtype":"Currency", "precision": 2}
			   ]
	if( filters.get('retailer')!=None ) and ( filters.get('retailer')!="" ):
		data = get_retailer_data(filters.get("from_date"), filters.get("to_date"), filters.get('retailer'))
	else:
		data = get_data(filters.get("from_date"), filters.get("to_date"))
	return columns, data

def get_retailer_data(from_date, to_date, retailer):
	data = []
	print "===========get_data!========"
	t_gross, t_tickets, t_cancels, t_payout, t_netsales, t_netdue = 0, 0, 0, 0, 0, 0
	print from_date, to_date
	rows = frappe.db.sql(
		"""SELECT name from `tabSales Order` where transaction_date>=%s and transaction_date<=%s and docstatus != 2 and customer = %s""",
		(from_date, to_date, retailer))
	for row in rows:
		print row
		so = frappe.get_doc("Sales Order", row[0])
		so_item = frappe.get_doc("Sales Order", row[0]).items[0]
		temp = {"date": so.transaction_date, "pos_no": so.pos_no, "retailer": so.customer, "tickets": so_item.qty,
				"gross_sales": so.grand_total, "cancels": so.cancels, "payout": so.payout, "net_sales": so.net_sales,
				"net_due": so.net_due}
		data.append(temp)
		t_tickets += so_item.qty
		t_gross += so.grand_total
		t_cancels += so.cancels
		t_payout += so.payout
		t_netsales += so.net_sales
		t_netdue += so.net_due
	temp = {"date": "", "pos_no": "", "retailer": "TOTALS", "tickets": t_tickets,
			"gross_sales": t_gross, "cancels": t_cancels, "payout": t_payout, "net_sales": t_netsales,
			"net_due": t_netdue}
	data.append(temp)
	return data

def get_data(from_date, to_date):
	data = []
	print "===========get_data!========"
	t_gross, t_tickets, t_cancels, t_payout, t_netsales, t_netdue = 0,0,0,0,0,0
	print from_date, to_date
	rows = frappe.db.sql("""SELECT name from `tabSales Order` where transaction_date>=%s and transaction_date<=%s and docstatus != 2 """,(from_date, to_date))
	for row in rows:
		print row
		so = frappe.get_doc("Sales Order", row[0])
		so_item = frappe.get_doc("Sales Order", row[0]).items[0]
		temp = {"date":so.transaction_date, "pos_no":so.pos_no, "retailer":so.customer, "tickets":so_item.qty,
				"gross_sales":so.grand_total, "cancels":so.cancels, "payout":so.payout, "net_sales":so.net_sales,
				"net_due":so.net_due}
		data.append(temp)
		t_tickets+=so_item.qty
		t_gross+=so.grand_total
		t_cancels+=so.cancels
		t_payout+=so.payout
		t_netsales+=so.net_sales
		t_netdue+=so.net_due
	temp = {"date": "", "pos_no": "", "retailer": "TOTALS", "tickets": t_tickets,
			"gross_sales": t_gross, "cancels": t_cancels, "payout": t_payout, "net_sales": t_netsales,
			"net_due": t_netdue}
	data.append(temp)
	return data