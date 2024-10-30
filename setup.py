import os
from setuptools import setup

setup(
    version="0.1.0",
    name="dcm-backend-api",
    description="api for backend-containers",
    author="LZV.nrw",
    install_requires=[
    ],
    packages=[
        "dcm_backend_api"
    ],
    package_data={
        "dcm_backend_api": [
            "dcm_backend_api/openapi.yaml",
        ],
    },
    include_package_data=True,
)
