from setuptools import setup

setup(
    name="flagon",
    version="0.1",
    description="A small flask wrapper",
    url="http://github.com/samakj/flagon",
    author="Sam Jones",
    author_email="samakj@live.co.uk",
    license="MIT",
    package_dir={"": "src"},
    packages=["flagon"],
    install_requires=["flask", "flask_caching"],
    zip_safe=False
)
