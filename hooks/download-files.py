TARGET_PATH = 'project-files/input/'


def download_files(course):
    # This is just for testing purpose.
    with open(f'{TARGET_PATH}{course}.txt', 'w') as f:
        f.write(course)


if __name__ == '__main__':
    download_files('{{ cookiecutter.course }}')