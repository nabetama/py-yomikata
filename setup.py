from setuptools import setup, find_packages


with open("README.rst",  "rt") as f: readme = f.read()


setup(
    name='yomikata',
    version="0.1",
    description="How do you read this?",
    long_description=__doc__,
    author='Mao Nabeta',
    author_email='mao.nabeta@gmail.com',
    url='https://github.com/nabetama/py-yomikata',
    packages=find_packages(),
    include_package_data=True,
    install_requires=['requests'],
    provides=["yomikata"],
    keywords=["yomikata"],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Communications :: Chat',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],
    entry_points='''
        [console_scripts]
        yomikata=yomikata.cli:main
    '''
    )
