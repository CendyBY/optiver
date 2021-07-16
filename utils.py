import zipfile
import os

def ensure_directory_exists(directory: str):
    if not os.path.exists(directory):
        os.makedirs(directory)

def unzip_file(destination_path,filepath="./", filename=None):
    unzip_path = os.path.join(filepath, filename)
    if os.path.exists(unzip_path):
        with zipfile.ZipFile(unzip_path) as z:
            z.extractall(destination_path)
    return True


if __name__ == '__main__':
    path_dir = '../input/optiver-realized-volatility-prediction'
    ensure_directory_exists(path_dir)
    filename = 'optiver-realized-volatility-prediction.zip'
    filepath = './'
    unzip_file(path_dir, filename=filename)


