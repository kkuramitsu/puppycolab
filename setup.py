from setuptools import setup
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent / 'tests'))

'''
python3 -m unittest
vim setup.py
rm -rf dist/
python3 setup.py sdist bdist_wheel
twine upload --repository pypi dist/*
'''

setup(
    name='puppy',
    version='0.0.1',
    url='https://github.com/kkuramitsu/puppycolab.git',
    license='MIT',
    author='Kimio Kuramitsu',
    description='Puppy for Colab',
    install_requires=['setuptools'],
        packages=['puppy'],
        package_data={'puppy': ['js/*.js']},
    entry_points={
        'console_scripts': [
            'puppy = puppy.main:main'
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing',
    ],
    test_suite='test_all.suite'
)
