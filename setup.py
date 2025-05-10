from setuptools import setup, find_packages

setup(
    name='django-auth-plugin',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Django>=3.0,<4.0',
        'django-allauth',
    ],
    description='A plugin for user authentication, signup, login, email confirmation, and password reset.',
    author='Jackson Njihia',
    author_email='njihiajack7son@gmail.com',
    url='https://github.com/JaxnStack/allauth_account.git',
)
