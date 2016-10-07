from setuptools import setup, find_packages

with open('/ws/upadhyay/myplugin/requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='MyFirstPlugin',
    version='1.0',
#    packages=find_packages(),
    packages=['plugin',],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.txt').read(),
    install_requires=requirements,
    dependency_links=[
      'file:/ws/upadhyay/myplugin',
    ],
    url='https://github.com/payalupadhyaya/myplugin',
    keywords='myplugin',
    entry_points = {
        'pytest11': ['plugin=plugin.myentrypoint'],
        'ting': ['ting=plugin.secondentrypoint:secondentryPoint']
    }
)


