from fabric.api import local, cd, put, lcd, env, run
import numpy as np
import os
env.hosts = ['parallels@10.211.55.10:22']


def local_deploy():
    local('python setup.py install')


def deploy():
    local('echo `pwd`')
    version_str = local(
        'python -c "import cmaps; print(cmaps.__version__)"', capture=True)
    local('python setup.py sdist')
    dist_fname = 'cmaps-' + version_str.stdout + '.tar.gz'

    remote_tmp = '/tmp/test' + str(int(np.random.randn() * 1000 + 5000))
    run('mkdir -p ' + remote_tmp)
    put('./dist/' + dist_fname, remote_tmp)

    with cd(remote_tmp):
        run('tar -xvf ' + dist_fname)
    with cd(os.path.join(remote_tmp, dist_fname.strip('.tar.gz'))):
        run('python setup.py install')
    run('rm -rf ' + remote_tmp)
