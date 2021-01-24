"""
Global settings and constants read by Flask and other
parts of the server.
"""
import logging
import os

# Server version
SERVER_VERSION = os.environ.get("NUNASERVER_VERSION") or "v1.0.0"

# settings for Flask
UPLOAD_FOLDER = os.environ.get("NS_UPLOAD_FOLDER") or "./uploads"
ALLOWED_EXTENSIONS = {"zip"}

# Celery
CELERY_RESULT_BACKEND = os.environ.get("NS_REDIS_RESULT") or "redis://localhost"
CELERY_BROKER_URL = os.environ.get("NS_REDIS_BROKER") or "redis://localhost:6379/0"

# Nunavut
OUT_FOLDER = os.environ.get("NS_WORK_FOLDER") or "./uploads"
OUT_FILE_FOLDER = os.environ.get("NS_STATIC_FOLDER") or "./static"
# ^^^ DO NOT SET THIS TO SAME/SUBDIR OF OUT_FOLDER OR UPLOAD_FOLDER!
# Will be insecure.
# Serves static files from this directory (so user can download generated code).
# In production there will likely be a production server (e.g. nginx)
# serving these files.
# Care should be taken when configuring as to not accidentally expose other people's
# generated code.
OUT_SERVER_URL = os.environ.get("NS_STATIC_SERVER_URL") or "http://localhost:8000"
# ^^ Set this to production static file server URL

# Misc.
LOG_LEVEL = logging.INFO
