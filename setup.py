import setuptools

setuptools.setup(
    name="enkanetwork.py",
    version="4.2",
    author="Trum-ok",
    author_email="artamarkan@gmail.com",
    description="Library for fetching JSON data from site https://enka.network/",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Trum-ok/EnkaNetwork.py",
    keywords=['enkanetwork.py', 'enkanetwork', 'enka.network', 'genshinapi'],
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "pydantic",
        "aiohttp",
        "cachetools"
    ],
    python_requires=">=3.11",
    include_package_data=True
)
