// Copyright (c) 2017, littlehera and contributors
// For license information, please see license.txt

frappe.ui.form.on('Weekly Invoice', {
	refresh: function(frm) {
	}
});
///home/littlehera/frappe-v9/apps/lotto_addons
frappe.ui.form.on("Weekly Invoice",{
	"to_date": function(frm){
		get_so_data(frm);
	},
	"from_date": function(frm){
		frappe.call({
		method: "lotto_addons.lotto_addons.doctype.weekly_invoice.weekly_invoice.get_to_date",
		args: {
			"date" : frm.doc.from_date
		},
		callback: function(r){
            if (r.message)
            	frm.set_value("to_date",r.message);
			}
	});
	}
});

function get_so_data(frm){
	frappe.call({
		method: "lotto_addons.lotto_addons.doctype.weekly_invoice.weekly_invoice.get_weekly_sales_orders",
		args: {
			"from_date" : frm.doc.from_date,
			"to_date" : frm.doc.to_date,
			"retailer": frm.doc.retailer
		},
		callback: function(r){
			cur_frm.clear_table("items");
            cur_frm.refresh_field("items");
            if (r.message)
            	var len = r.message.length;
				for (var i = 0; i< len; i++)
				{
					console.log(r.message[i]);
					var newrow = cur_frm.add_child("items");
					var prizes_row = cur_frm.add_child("items");
					newrow.draw_id = r.message[i].draw_id;
					newrow.date = r.message[i].date;
					newrow.tpm = r.message[i].tpm;
					newrow.so = r.message[i].so;
					newrow.sales = r.message[i].sales;
					newrow.discount = r.message[i].discount;
					newrow.prizes = 0;
					newrow.prizes_discount = 0;
					newrow.totals = r.message[i].sales_totals;

					prizes_row.draw_id = r.message[i].draw_id;
					prizes_row.date = r.message[i].date;
					prizes_row.tpm = r.message[i].tpm;
					prizes_row.so = r.message[i].so;
					prizes_row.sales = 0;
					prizes_row.discount = 0;
					prizes_row.prizes = r.message[i].prizes;
					prizes_row.prizes_discount = r.message[i].prizes_discount;
					prizes_row.totals = r.message[i].prizes_totals;
				}
				frm.refresh_field("items");
			}

	});
}