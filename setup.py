from setuptools import setup, find_packages

try:
  from setuptools import setup
  from setuptools.command.install import install
except ImportError:
  from distutils.core import setup
  from distutils.command.install import install
import os


class buildweb(install):
  def run(self):
    print("generate web application")
    cwd = os.getcwd()
    os.chdir("knobo/web");
    os.system('npm install')
    os.system('npm run build')
    os.chdir(cwd);
    install.run(self)

setup(
    name='knobo',
    version='0.0.4',
    cmdclass={'install': buildweb},  #Call the fuction buildweb
    packages=find_packages(include=['knobo']),
    install_requires=['cherrypy'],
    author='Knut Olav Bohmer',
    author_email='bohmer@gmail.com',
    entry_points = {
        'console_scripts':['jalla = knobo.knobo:main'],
        'telldus.plugins': ['c = knobo.knobo:Knobo [cREQ]']
    },
    include_package_data=True,
    extras_require = dict(cREQ = 'Base>=0.1\nTelldus>=0.1\nTelldusWeb>=0.1'),
    zip_safe = False
)
