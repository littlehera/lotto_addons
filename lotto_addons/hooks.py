# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "lotto_addons"
app_title = "Lotto Addons"
app_publisher = "littlehera"
app_description = "Zambian Lotto Addons"
app_icon = "octicon octicon-file-directory"
app_color = "#EF4836"
app_email = "villanuevahera@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/lotto_addons/css/lotto_addons.css"
# app_include_js = "/assets/lotto_addons/js/lotto_addons.js"

# include js, css files in header of web template
# web_include_css = "/assets/lotto_addons/css/lotto_addons.css"
# web_include_js = "/assets/lotto_addons/js/lotto_addons.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "lotto_addons.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "lotto_addons.install.before_install"
# after_install = "lotto_addons.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "lotto_addons.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"lotto_addons.tasks.all"
# 	],
# 	"daily": [
# 		"lotto_addons.tasks.daily"
# 	],
# 	"hourly": [
# 		"lotto_addons.tasks.hourly"
# 	],
# 	"weekly": [
# 		"lotto_addons.tasks.weekly"
# 	]
# 	"monthly": [
# 		"lotto_addons.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "lotto_addons.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "lotto_addons.event.get_events"
# }
fixtures = ["Report"]
#fixtures = ["Custom Field", "Custom Script", "Property Setter", "Print Format", "Report"]
