import os
import multiprocessing

PORT = int(os.environ.get("PORT",8080))
DEBUG_MODE = int(os.environ.get("DEBUG_MODE",1))
bind = ":" + str(PORT)
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2 * multiprocessing.cpu_count()