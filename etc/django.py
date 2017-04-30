CONFIG = {
    'mode': 'wsgi',
    'working_dir': '/home/box/web/ask',
    'python': '/usr/bin/python',
    'args': (
        '--bind=0.0.0.0:8080',
        '--workers=16',
        '--timeout=60',
        'errorlog="/home/box/logs/error.log"',
        'loglevel = "degug"',
        'ask.wsgi:application',
    ),
}
