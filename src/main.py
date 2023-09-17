import logging

from flask import Flask

from config import database_connection
from core.infra.database.init_database_tables import init_database_tables
from web.views import api

# configure root logger
logging.basicConfig(level=logging.DEBUG)

init_database_tables(database_connection)

app = Flask(__name__)
api.init_app(app)


@app.before_request
def create_session():
    database_connection.init_session()


@app.teardown_appcontext
def shutdown_session(exception=None):
    database_connection.remove_session()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5151, debug=True)
