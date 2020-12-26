import pandas as pd


class Indexer:
    def __init__(self, filepath):
        self.index_filepath = filepath
        self.file_index = pd.read_csv(filepath)

    def resync_index(self):
        pass

    def add_media(self, media_type, meta):
        self.file_index.append({'type': media_type, 'meta': meta})
        self.resync_index()
