from setuptools import setup
from setuptools import find_packages

REQUIRED_PACKAGES = ['sklearn', 'pandas']

setup(name='trainer',
		version='1.0',
		install_requires=REQUIRED_PACKAGES,
		packages=find_packages(),
		description='Iris Dataset',
		author='DJS',
		autor_email='prohacking321@gmail.com',
		include_package_data=True,
		license='MIT'

	)