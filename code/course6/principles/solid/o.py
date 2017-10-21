# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class WindowsModule(object):
    def __init__(self, path, filename):
        #
        self.full_path = path + '\\' + filename
        #


class UnixModule(WindowsModule):
    pass  # error!












class BaseModule(object):
    path_separator = '\\'

    def __init__(self, path, filename):
        self.full_path = path + self.__class__.path_separator + filename


class NewUnixModule(BaseModule):
    path_separator = '/'


class NewWindowsModule(BaseModule):
    path_separator = '\\'
