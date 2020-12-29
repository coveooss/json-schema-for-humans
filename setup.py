from setuptools import setup

setup(
    setup_requires=["pbr"],
    pbr=True,
    package_data={"json_schema_for_humans": ["templates/*/*"]},
)
