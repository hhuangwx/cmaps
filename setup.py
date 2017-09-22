from setuptools import setup
VERSION = '0.2.0'


def write_version_py(version=VERSION, filename='cmaps/_version.py'):
    cnt = """# THIS FILE IS GENERATED FROM SETUP.PY
__version__ = '%(version)s'
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': version})
    finally:
        a.close()


write_version_py()
setup(
    name='cmaps',
    author='Hao Huang',
    version=VERSION,
    author_email='hhuangmeso@gmail.com',
    packages=['cmaps', ],
    package_data={'cmaps': ['colormaps/*'], },
    url='',
    license='LICENSE.txt',
    description='',
    long_description='',
    install_requires=['matplotlib'],
)
