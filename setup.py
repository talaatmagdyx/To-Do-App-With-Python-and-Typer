from setuptools import setup

setup(
    name='rptodo',
    version='0.0.1',
    packages=['rptodo'],
    entry_points={
        'console_scripts': [
            'rptodo = rptodo.cli:app'
        ]
    })
