import os
from setuptools import setup

setup(
    version="5.3.0",
    name="dcm-backend-api",
    description="specification of the DCM Backend API",
    author="LZV.nrw",
    license="MIT",
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
