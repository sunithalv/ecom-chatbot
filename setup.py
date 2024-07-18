from setuptools import find_packages, setup

setup(
    name="Ecommercebot",
    version="0.0.1",
    author="sunithalv",
    author_email="sunithalv05@gmail.com",
    packages=find_packages(),
    install_requires=['langchain-astradb','langchain ','langchain-groq','datasets','pypdf','python-dotenv','flask']
)