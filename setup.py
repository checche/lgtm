from setuptools import find_packages, setup

setup(
    name='lgtm',
    version='0.0.1',
    packages=find_packages(exclude=('tests',)),
    install_requires=[
        'Click~=7.0',
        'Pillow~=6.2.0',
        'requests~=2.22.0',
    ],
    entry_points={
        'console_scripts': [
            'lgtm=lgtm.core:cli'
        ]
    }
)
