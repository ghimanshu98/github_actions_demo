from setuptools import setup, find_packages

REQUIREMENT_FILE_NAME = "requirements.txt"
REMOVE_PACKAGE = "-e ."

def get_requirement_list(requirement_file_name = REQUIREMENT_FILE_NAME) -> list:
    try:
        requirement_list = None
        with open(requirement_file_name) as requirement_file:
            requirement_list = [requirement.replace("\n", "") for requirement in requirement_file]
            requirement_list.remove(REMOVE_PACKAGE)

            return requirement_list
    except Exception as e:
        raise e


# calling the setup function

setup(
    name="DVC_Github_Action_Demo",
    license="MIT",
    version="0.0.0",
    description="Demo project for showing working of Github Action and DVC",
    author="Himanshu",
    packages=find_packages(),
    requires=get_requirement_list()
)