
from app.app import create_app as create_dash_1
from flask import (
    Flask
    )

def create_app():

    server = Flask(__name__)

    dashboard = create_dash_1(server=server)

    @server.route("/")
    def home():
        page = """
        <html>
            <h1>Hello wsgi</h1>
            <a href="/dashboard">Dashboard</a>
        </html>
        """

        return page


    @server.route("/dashboard/")
    def dashboard_page():

        return dashboard.index
    
    return server

if __name__=='__main__':
    app = create_app()
    app.run(port=5001)
