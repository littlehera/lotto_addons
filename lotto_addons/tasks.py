import frappe
from datetime import date, datetime, timedelta
import calendar, re

def renumbers_submit_so():
    sos= frappe.db.sql("""SELECT name from `tabSales Order` ORDER BY name asc""")
    for i, so in enumerate(sos):
        id = "SO-"+str(i+1).zfill(5)
        print "Count: " + str(i + 1) + "| ID: " + id + " | SO: " + so[0]
        if id != so[0]:
            print "RENAME!"
            frappe.db.sql("""UPDATE `tabSales Order` set name = %s where name = %s""",(id, so[0]))
            frappe.db.sql("""UPDATE `tabSales Order Item` set parent = %s where parent = %s""",(id, so[0]))
            frappe.db.commit()
            submit_doc("Sales Order", id)
            #frappe.get_doc("Sales Order",id)

def submit_doc(doctype, id):
    print "============SUBMIT==============="
    doc = frappe.get_doc(doctype, id)
    doc.submit()

def recompute_gross():
    sos = frappe.db.sql("""SELECT name from `tabSales Order` ORDER BY name asc""")
    for so in sos:
        doc = frappe.get_doc("Sales Order", so[0])
        print doc.name
        gross_sales = float(doc.net_sales + doc.cancels)
        frappe.db.sql("""UPDATE `tabSales Order` set gross_sales = %s where name = %s""",(gross_sales, so[0]))
        frappe.db.commit()

def set_lotto_dates():
    days_str = ""
    games = frappe.db.sql("""select name from `tabLotto Game`""")
    print "SET_LOTTO_DATES"
    for game in games:
        doc = frappe.get_doc("Lotto Game", game[0])
        start_date = doc.start_date
        day_str = str(calendar.day_name[start_date.weekday()])
        print "Start Day: "+day_str
        if day_str in ['Sunday', 'Monday', 'Tuesday']:
            days_str ='Sunday,Monday,Tuesday'
            dates = ['Sunday', 'Monday', 'Tuesday']
        elif day_str in ['Wednesday', 'Thursday']:
            days_str = "Wednesday,Thursday"
            dates = ['Wednesday', 'Thursday']
        else:
            days_str = 'Friday,Saturday'
            dates = ['Friday', 'Saturday']
        print dates
        end_date = start_date
        temp_date = start_date - timedelta(days=4)
        data = get_dates(temp_date, end_date, dates)
        print end_date, temp_date
        for row in data:
            print "ROW IN DATA"
            draw_dict = {
                "day": row["day"],
                "date": row["date"],
                "parent":doc.name,
                "parenttype":"Lotto Game",
                "parentfield": "draw_dates",
                "doctype":"Draw Dates"
            }
            draw_doc=frappe.get_doc(draw_dict)
            print draw_dict
            draw_doc.insert()
            doc.append("draw_dates", draw_doc)
        doc.start_date = data[0]["date"]
        doc.draw_days = days_str
        doc.save()


def get_dates(start_date,end_date, days):
    date_temp = start_date
    data = []
    print "=======+GET DATES+=========="
    print start_date, end_date
    while date_temp <= end_date:
        temp = dict()
        day_str = str(calendar.day_name[date_temp.weekday()])
        if day_str in days:
            temp["day"] = day_str
            temp["date"] = date_temp
            days.remove(day_str)
            data.append(temp)
        date_temp = date_temp + timedelta(days=1)
    return data