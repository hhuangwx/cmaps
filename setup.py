from setuptools import setup
VERSION = '0.1.0'


def write_version_py(version=VERSION, filename='easycmaps/_version.py'):
    cnt = """# THIS FILE IS GENERATED FROM SETUP.PY
version = '%(version)s'
"""
    a = open(filename, 'w')
    try:
        a.write(cnt % {'version': version})
    finally:
        a.close()

write_version_py()
setup(
    name='easycmaps',
    author='Hao Huang',
    version=VERSION,
    author_email='hhuangmeso@gmail.com',
    packages=['easycmaps', ],
    package_data={'easycmaps': ['colormaps/*'], },
    url='',
    license='LICENSE.txt',
    description='',
    long_description='',
)
