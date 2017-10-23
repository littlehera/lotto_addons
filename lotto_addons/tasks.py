import frappe

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