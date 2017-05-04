from setuptools import setup

setup(
    name='admix',

    version='0.1.dev1',

    description='An admixture analysis tool that supports raw data from 23andme, AncestryDNA, etc.',
    long_description=open('admix/README.rst','r').read(),

    url='https://github.com/stevenliuyi/admix',

    author='Steven Liu',
    author_email='stevenliuyi@gmail.com',

    license='GNU General Public License v3.0',

    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='bio DNA SNP ancestry admixture',

    install_requires=['numpy','scipy'],

    packages=['admix'],

    package_data={
        'admix':['data/*', 'README.rst']
    },

    entry_points={
        'console_scripts': ['admix=admix.admix:main'],
    },
)
