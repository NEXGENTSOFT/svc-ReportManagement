from flask import Flask
from src.ReportManagement.Infrastructure.Routes.ReportsRoute import start_report, callback, report_routes
app = Flask(__name__)
app.register_blueprint(report_routes, url_prefix="/reports")

start_report()

if __name__ == '__main__':
    app.run(debug=True, port=3001)