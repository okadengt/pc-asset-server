[Unit]
Description=PC Asset Server
After=network.target

[Service]
User=dengyo
WorkingDirectory=/home/dengyo/pc-asset-server
Environment="PATH=/home/dengyo/pc-asset-server/venv/bin"
ExecStart=/home/dengyo/pc-asset-server/venv/bin/python run.py --host 0.0.0.0 --port 5000
Restart=always

[Install]
WantedBy=multi-user.target