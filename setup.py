from setuptools import setup

setup(
    name='Block Ip',
    version='0.1.0',
    url='https://github.com/fabiano-teichmann/py_block_ip.git',
    license='MIT License',
    author='Fabiano Teichmann',
    author_email='fabiano.geek@gmail.com',
    keywords='block ip, protect attack',
    description=u'This tools has propose blocks ip suspects',
    packages=['py_block_ip'],
    install_requires=['python-iptables', 'python-decouple'],
)
