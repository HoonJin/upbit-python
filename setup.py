from setuptools import setup

setup(
    name='upbit-python',
    packages=['upbit'],
    version='0.0.1',
    description='upbit API wrapper for Python',
    url='http://github.com/Hoonjin/upbit-python/',
    author='Daniel Ji',
    author_email='bwjhj1030@gmail.com',
    install_requires=['requests', 'PyJWT'],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ],
    license='MIT',
)
