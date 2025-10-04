from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__, template_folder='../FRONTEND')
CORS(app)

# ... (baaki saara code same rahega - routes, CAREER_DATA, etc.)

# REMOVE ye last line:
# if __name__ == '__main__':

# Vercel ke liye export karo
handler = app