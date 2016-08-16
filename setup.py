from setuptools import setup


setup(
    name='Context logging',
    version='0.1.0',
    description='Pretty contextual key-value colored logging',
    long_description='Context logging provides contextual (with key-value scheme), level-colored (optional) logger based on _logging_ module.',
    classifiers=[
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5'],
    author='Oleg Krasnikov',
    author_email='a.insolite@gmail.com',
    url='https://github.com/insolite/context-logging',
    download_url='https://github.com/insolite/context-logging',
    packages=['context_logging'],
    include_package_data=True,
)