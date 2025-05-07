import setuptools  # type: ignore
from setuptools import setup

setup(
    name="test_dependabot",
    author="yao",
    author_email="test_dependabot@support.com",
    python_requires=">=3.10",
    description="test dependabot",
    license="Apache 2",
    packages=setuptools.find_packages(),
    install_requires=[
        "pytket >= 2.1.0, < 2.2.0",
    ],
    classifiers=[
        "Environment :: Console",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
    ],
    include_package_data=True,
    package_data={"pyqubit_reuse": ["py.typed"]},
    zip_safe=False,
    version="0.0.10",
)
