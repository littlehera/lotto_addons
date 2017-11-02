// Copyright (c) 2017, littlehera and contributors
// For license information, please see license.txt

frappe.ui.form.on('Lotto Game', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Lotto Game", "draw_days",function(frm){
	frappe.call({
		method: "lotto_addons.lotto_addons.doctype.lotto_game.lotto_game.get_dates",
		args: {
			"start_date": frm.doc.start_date,
			"draw_days": frm.doc.draw_days
		},
		callback: function(r){
			console.log(r);
			cur_frm.clear_table("draw_dates");
			cur_frm.refresh_field("draw_dates");
			if (r.message){
				frm.set_value("draw_no",r.message[1]);
				var ctr = r.message[0].length;
				for (var i =0; i<ctr; i++){
					var new_row = cur_frm.add_child("draw_dates");
					new_row.day = r.message[0][i].day;
					new_row.date = r.message[0][i].date;
				}
				frm.refresh_field("draw_dates");
			}
		}
	});
});