from setuptools import setup, find_packages

with open('/ws/upadhyay/myplugin/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='MySecondPlugin',
    version='2.0',
#    packages=find_packages(),
    packages=['secondplugin',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    install_requires=requirements,
    dependency_links=[
      'file:/ws/upadhyay/secondplugin',
    ],
<<<<<<< HEAD
    url='https://github.com/payalupadhyaya/secondplugin',
    keywords='secondplugin',
    entry_points = {
        'console_scripts':
        ['ting=secondplugin.secondentrypoint:externalPoint']
=======
    url='https://github.com/payalupadhyaya/myplugin',
    keywords='myplugin',
    entry_points = {
        'pytest11': ['plugin=plugin.myentrypoint'],
        'ting': ['ting=plugin.secondentrypoint:secondentryPoint']
>>>>>>> c4fc193bdd659d853c45a2a223b4cf607585821d
    }
)


