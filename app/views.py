from flask import Blueprint, request, jsonify
from .models import get_db
import datetime

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/report', methods=['POST'])
def report():
    data = request.json
    db = get_db()
    now = datetime.datetime.utcnow().isoformat()
    row = db.execute('SELECT id FROM pc_assets WHERE hostname=?', (data.get('hostname'),)).fetchone()
    if row:
        db.execute('''
            UPDATE pc_assets SET os=?, cpu=?, memory=?, serial=?, mac=?, last_report=?
            WHERE hostname=?
        ''', (
            data.get('os'), data.get('cpu'), data.get('memory'),
            data.get('serial'), data.get('mac'), now, data.get('hostname')
        ))
    else:
        db.execute('''
            INSERT INTO pc_assets (hostname, os, cpu, memory, serial, mac, last_report)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (
            data.get('hostname'), data.get('os'), data.get('cpu'),
            data.get('memory'), data.get('serial'), data.get('mac'), now
        ))
    db.commit()
    return jsonify({"message": "OK"})

@bp.route('/assets', methods=['GET'])
def list_assets():
    db = get_db()
    assets = db.execute('SELECT * FROM pc_assets').fetchall()
    return jsonify([dict(asset) for asset in assets])