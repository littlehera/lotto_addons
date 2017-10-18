// Copyright (c) 2017, littlehera and contributors
// For license information, please see license.txt

frappe.ui.form.on('Weekly Invoice', {
	refresh: function(frm) {

	}
});
///home/littlehera/frappe-v9/apps/lotto_addons
frappe.ui.form.on("Weekly Invoice", "date", function(frm){
	frappe.call({
		method: "lotto_addons.lotto_addons.doctype.weekly_invoice.weekly_invoice.get_weekly_sales_orders",
		//method: "lotto_addons.lotto_addons.doctype.weekly_invoice.weekly_invoice.get_weekly_sales_order",
		args: {
			"date" : frm.doc.date,
			"retailer": frm.doc.retailer
		},
		callback: function(r){
			cur_frm.clear_table("items");
            cur_frm.refresh_field("items");
            console.log(r.message)
            if (r.message)
            	var len = r.message.length
				for (var i = 0; i< len; i++)
				{
					console.log(r.message[i]);
					var newrow = cur_frm.add_child("items");
					newrow.date = r.message[i].date;
					newrow.tpm = r.message[i].tpm;
					newrow.so = r.message[i].so;
					newrow.sales = r.message[i].sales;
				}
				frm.refresh_field("items");
			}

	});
});