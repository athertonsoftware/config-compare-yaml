# Copyright 2023 Tony Akocs
# SPDX-License-Identifier: MIT
import setuptools

with open('README.md', encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='config_compare_yaml',
    author='Tony Akocs',
    author_email='tony.akocs@gmail.com',
    description="""Compare the projects sample config keys to developers config file.""",  # noqa: E501
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/akocs/config_compare_yaml',
    project_urls={
        'Bug Tracker': 'https://github.com/akocs/config_compare_yaml/issues',  # noqa: E501
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    install_requires=[
          'PyYAML',
    ],
    python_requires='>=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*',
    entry_points={
        'console_scripts': [
            'config_compare_yaml = config_compare_yaml.main:main',
        ],
    },
    license='MIT',
    test_suite='unittest',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
