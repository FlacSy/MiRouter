from setuptools import setup, find_packages

setup(
    name='MiRouter',
    version='1.0.0',
    description='Python library for interacting with Xiaomi routers via their web API',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/FlacSy/MiRouter',
    author='FlacSy',
    author_email='flacsy.x@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='Xiaomi router web API',
    packages=find_packages(),
    install_requires=['requests'],
)
