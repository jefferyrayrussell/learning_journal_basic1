import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.txt')) as f:
    README = f.read()
with open(os.path.join(here, 'CHANGES.txt')) as f:
    CHANGES = f.read()

requires = [
    'pyramid',
    'pyramid_ipython',
    'pyramid_jinja2',
    'pyramid_debugtoolbar',
    'pyramid_tm',
    'waitress',
    'SQLAlchemy',
    'transaction',
    'zope.sqlalchemy',
]

tests_require = [
    'WebTest >= 1.3.1',  # py3 compat
    'pytest',  # includes virtualenv
    'pytest-cov',
    'tox',
]

setup(name='learning_journal_basic1',
      version='0.0',
      description='learning_journal_basic1',
      long_description=README + '\n\n' + CHANGES,
      classifiers=[
          "Programming Language :: Python",
          "Framework :: Pyramid",
          "Topic :: Internet :: WWW/HTTP",
          "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
      ],
      author='Jeffery Ray Russell',
      author_email='jefferyrayrussell@gmail.com',
      url='https://github.com/jefferyrayrussell/learning_journal_basic1',
      keywords='web wsgi bfg pyramid pylons',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      extras_require={
          'testing': tests_require,
      },
      install_requires=requires,
      entry_points="""\
      [paste.app_factory]
      main = learning_journal_basic1:main
      [console_scripts]
      initialize_db = learning_journal_basic1.scripts.initializedb: main""",
      )
