from setuptools import setup
gh_repo = 'https://github.com/weaming/sets'

setup(
    name='sets-operation-over-files',  # Required
    version='0.1.2',  # Required
    description='Set operate over files which contains set of lines',  # Required
    url=gh_repo,  # Optional
    author='weaming',  # Optional
    author_email='garden.yuen@gmail.com',  # Optional
    py_modules=['sets'],
    keywords='set,cli',  # Optional
    entry_points={  # Optional
        'console_scripts': [
            'sets=sets:main',
        ],
    },

    project_urls={  # Optional
        'Bug Reports': gh_repo,
        'Source': gh_repo,
    },
)
