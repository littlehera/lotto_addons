// Copyright (c) 2016, littlehera and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["SO Sales Report"] = {
	"filters": [
		{
            "fieldname": "from_date",
            "label": __("From Date"),
            "fieldtype": "Date",
            "reqd": 1
        },
		{
            "fieldname": "to_date",
            "label": __("To Date"),
            "fieldtype": "Date",
            "reqd": 1
        },
		{
            "fieldname": "retailer",
            "label": __("Retailer"),
            "fieldtype": "Link",
            "options":"Customer",
			"reqd": 0
        }
	]
};
