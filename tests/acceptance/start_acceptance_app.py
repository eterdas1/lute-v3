"""
Copy of main.py, running the server on port 9876.

This still connects to the test database etc.
"""

import sys
import logging
from waitress import serve

# Hack the path, or python can't find the lute package when this is run
# from the root dir using "python -m this.module.name"
#
# pylint: disable=wrong-import-position
sys.path.append("..")
from lute.main import init_db_and_app
from lute.app_config import AppConfig

logging.getLogger("waitress.queue").setLevel(logging.ERROR)

app_config = AppConfig.create_from_config()
app = init_db_and_app(app_config)

port = 9876
print(f'running at localhost:{port}')
serve(app, host="0.0.0.0", port=port)