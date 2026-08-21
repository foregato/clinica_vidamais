import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app, init_db

init_db()

# O Vercel procura por uma variável chamada "app"
