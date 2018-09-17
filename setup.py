from setuptools import setup, find_packages

install_requires = ['aioredis']

setup(
    name='redisobjects',
    version='0.1.0',
    description='Object-oriented wrapper for aioredis. Meant for easy usage.',
    author='Jochem Barelds',
    author_email='barelds.jochem@gmail.com',
    url='https://gitlab.com/jchmb/redisobjects',
    packages=find_packages(exclude=['tests', 'examples']),
    install_requires=install_requires,
    include_package_data=True,
)
