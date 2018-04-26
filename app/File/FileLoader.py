import os
import pandas as pd

class FileLoader:
    """
        Class FileLoader:
            load files and pandas csv


    """
    def __init__ (self, file):
        self.file = file;

    def exist(self, file):
        return os.path.exists(file)

    def get_path(self):
        return os.path.dirname(__file__)

    def get_file_path(self):
        return  os.path.join(self.get_path(), '..',  self.file)

    def load_data(self):
        file = self.file

        # the path to file
        file = self.get_file_path()

        if self.exist(file):
            try:
                return pd.read_csv(file)
            except Exception as e:
                print(str(e))
        else :
            # file not found
            raise FileNotFoundError('File not found: {0}'.format(file))
