
class Item:
    def __init__(self, data):
        self.data = data
        self.guid = self.create_item()

    def create_item(self):
        """Makes an api call and returns guid"""
        pass

    def info(self):
        return {'item_guid': self.guid, 'data': self.data}


class FileTypeItem:
    def __init__(self, filepath, url):
        self.filepath = filepath
        self.url = url

    def create_item(self):
        """Makes an api call and returns guid"""

    def upload_file(self,):
        """Upload the file to S3"""
        pass

    def filename(self):
        """Returns filename only"""
        pass

    def filesize(self):
        """Returns filesize only"""
        pass

    def file_data(self):
        """Returns the data from file"""
        pass

    def info(self):
        return {'file': {'name': self.filename(),
                         'size': self.filesize()},
                'data': self.file_data()}


class Set:
    def __init__(self, files):
        self.files = files
        self.guid = self.create_set()

    def create_set(self):
        pass

    def get_item_guids(self):
        pass

    def info(self):
        return {'item_guids': self.get_item_guids(), 'set_guid': self.guid}


class Group:
    def __init__(self, sets):
        self.sets = sets
        self.guid = self.create_guid()

    def create_guid(self):
        pass

    def get_sets_guid(self):
        pass

    def info(self):
        return {'group_guid': self.guid, 'sets_guid': self.get_sets_guid()}

