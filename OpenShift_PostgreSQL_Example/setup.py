from setuptools import setup

setup(name='FlairGen',
      version='1.0',
      description='Inline flair generator for reddit /r/cfb',
      author='henrygd',
      author_email='henryoflivonia@gmail.com',
      url='https://www.gitgub.com/henrygd',
      install_requires=[
      'Flask>=0.7.2',
      'Jinja2==2.7.3',
      'MarkupSafe==0.23',
      'Werkzeug==0.9.6',
      'argparse==1.2.1',
      'itsdangerous==0.24',
      'wsgiref==0.1.',   
      'psycopg2==2.5',
      ],
     )
