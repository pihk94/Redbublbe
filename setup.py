from setuptools import setup, find_packages

setup(
    name="redbubble",
    version="0.1.0",
    packages=find_packages(),
    scripts=[
        "./redbubble/bin/redbubble"
    ],
    install_requires=[
        "selenium",
        "click",
        "bs4",
    ],
    author="Melchior P.",
    entry_points='''
        [console_scripts]
        redbubble=redbubble.cli.cli:cli
    ''',
    author_email="melchior.prugniaud@gmail.com",
    description="A package to do some redbubble activities",
    include_package_data=True
)