from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='tbfac.theme',
      version=version,
      description="TBFAC Theme Package",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='web zope plone theme',
      author='TsungWei Hu',
      author_email='marr.tw@gmail.com',
      url='http://github.com/l34marr/tbfac.theme',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['tbfac'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      )
