"""This file contains your country package's metadata and dependencies."""

from setuptools import find_packages, setup

setup(
    name="policyengine-us",
    version="0.196.0",
    author="PolicyEngine",
    author_email="hello@policyengine.org",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: POSIX",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    description="PolicyEngine tax and benefit system for the US",
    keywords="benefit microsimulation social tax",
    license="http://www.fsf.org/licensing/licenses/agpl-3.0.html",
    url="https://github.com/PolicyEngine/policyengine-us",
    include_package_data=True,  # Will read MANIFEST.in
    data_files=[
        (
            "share/openfisca/openfisca-country-template",
            ["CHANGELOG.md", "LICENSE", "README.md"],
        ),
    ],
    install_requires=[
        "h5py==3.7.0",
        "microdf_python==0.3.0",
        "policyengine-core==1.10.23",
        "pandas==1.5.2",
        "pathlib==1.0.1",
        "pytest==5.4.3",
        "pytest-dependency==0.5.1",
        "pyyaml==6.0",
        "requests==2.28.1",
        "synthimpute==0.1",
        "tables==3.8.0",
        "tqdm==4.62.3",
        "click==8.1.3",
        "tabulate==0.9.0",
    ],
    extras_require={
        "dev": [
            "autopep8==1.7.0",
            "black==22.12.0",
            "coverage==6.5.0",
            "jupyter-book==0.13.1",
            "plotly==5.11.0",
            "setuptools==65.6.3",
            "wheel==0.38.4",
            "yaml-changelog==0.3.0",
            "linecheck==0.1.0",
            "furo==2022.9.29",
            "markupsafe==2.0.1",
            "sphinx==4.5.0",
            "sphinx-argparse==0.4.0",
            "sphinx-math-dollar==1.2.1",
        ],
    },
    python_requires=">=3.7,<3.10",
    entry_points={
        "console_scripts": [
            "policyengine-us = policyengine_us.tools.cli:main",
        ],
    },
    packages=find_packages(),
)
