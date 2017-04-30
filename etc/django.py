CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask',
    'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=16',
        '--timeout=60',
        '--error-logfile=/home/box/logs/gunicorn_error.log',
        '--log-file=/home/box/logs/gunicorn_error.log"',
        '--log-level=debug'
        'ask.wsgi:application',
    ),
}
