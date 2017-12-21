import os
import g_drive
import compliance_assist
from migration.file_data import file_data

class Migration(object):

    def __init__(self):
        self.f = open("migration.log","wb")
        self.f.write("Exception log for Compliance Assist migration task.")
        self.compliance_assist = compliance_assist.Site()
        self.g_drive = g_drive.Site()
        self.file_data = file_data

    def migrate(self):
        for folder in self.file_data:
            self.download_directory(folder)
            self.upload_directory(folder)
            self._clean()
    
    def upload_directory(self,folder):
        # TODO: Implement this method.
        pass

    def _clean(self):
        # TODO: Implement this method.
        pass     

    def download_directory(self,folder):
        self.file_buffer = set()
        for file_ in file_data[folder]:
            file_name = file_["file_name"]
            file_name = self._unduplicate(file_name,folder)
            self.file_buffer.add(file_name,folder)                
            file_url = file_["link"]
            self.compliance_assist.download(file_url)

    def _unduplicate(self,file_name,folder):
        k = 1
        while(file_name in self.file_buffer):
            if(k==1):
                file_name_split = file_name.split(".")
                file_name_split[-2] += " (1)"
                file_name = '.'.join(file_name_split)
            else:
                file_name.replace(str(k-1),str(k))
            k += 1
            self.f.write("Duplicate in {}: {} created.\n\n".format(folder,file_name))
        return file_name

    def __exit__(self,exc_type,exc_value,traceback):
        self.compliance_assist.close()
        self.g_drive.close()
        self.f.close()