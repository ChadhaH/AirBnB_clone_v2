#!/usr/bin/python3
"""
    a Fabric script that generates a .tgz archive
    from the contents of the web_static folder
"""
from datetime import datetime
from fabric.api import *

def do_pack():
    """
        create a tgz archive from web static folder
    """
    dte = datetime.now()
    file_arch = 'web_static_' + dte.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    creation = local('tar -cvzf versions/{} web_static'.format(file_arch))
    if creation is not None:
        return file_arch
    else:
        return None
