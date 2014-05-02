# -*- coding: utf-8 -*-
import os
import json
import bottle
import socket
import api

@bottle.route('/')
def index():
    return bottle.static_file('index.html', root=os.path.join(current_dir, 'ng-app'))


@bottle.route('/static/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root=os.path.join(current_dir, 'static'))

@bottle.route('/ng-app/<filepath:path>')
def server_static(filepath):
    return bottle.static_file(filepath, root=os.path.join(current_dir, 'ng-app'))

if __name__ == '__main__':
    current_dir = os.path.dirname(os.path.abspath(__file__))
    bottle.default_app().mount('/api/system',api.system_app)
    bottle.run(host='localhost', port=8080, reloader=False, debug=True)
