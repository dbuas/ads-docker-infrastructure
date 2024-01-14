"""
This script will run after the project has been generated.
Add any additional setup steps here.
"""

import os


def create_env_file():
    os.system('cp .env.example .env')


if __name__ == '__main__':
    create_env_file()