import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='tradingview_ta_v3',
    version='1.0.0',
    description="Unofficial TradingView technical analysis API wrapper.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nazguul512/python-tradingview-ta-v3',
    author='nazguul512',
    author_email='',
    packages=['tradingview_ta_v3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          'requests',
          'colorama'
    ],
    python_requires='>=3.6',
    project_urls={
        'Demo': 'https://tradingview.brianthe.dev',
        'Documentation': 'https://python-tradingview-ta.readthedocs.io',
        'Source': 'https://github.com/nazguul512/python-tradingview-ta-v3',
    },
)
