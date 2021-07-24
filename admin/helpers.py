from flask import Response, request, jsonify, send_from_directory, \
    make_response, render_template, redirect, g


class Store():
    def __init__(self):
        self.notices = []


store = Store()


class Notice:
    alert = "alert"
    success = "success"
    danger = "danger"
    warning = "warning"
    info = "info"

    def __init__(self, type, message):
        self.html_class = self.get_html_class_by_type(type)
        self.message = message

    def get_html_class_by_type(self, type):
        return {"alert": "alert alert-secondary",
                "success": "alert alert-success",
                "danger": "alert alert-danger",
                "warning": "alert alert-warning ",
                "info ": "alert alert-info "}[type]
