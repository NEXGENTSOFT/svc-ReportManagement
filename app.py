from flask import Flask
from src.ReportManagement.Infrastructure.Routes.ReportsRoute import report_routes
from src.ReportManagement.Infrastructure.Routes.ResourcesRoute import resources_routes
from src.ReportManagement.Infrastructure.Routes.DownloadableRoute import downloadable_routes

app = Flask(__name__)
app.register_blueprint(report_routes, url_prefix="/reports")
app.register_blueprint(resources_routes, url_prefix="/resources")
app.register_blueprint(downloadable_routes, url_prefix="/downloadable")

if __name__ == '__main__':
    app.run(debug=True, port=5000)

# No necesitamos start_report()
# start_report()


