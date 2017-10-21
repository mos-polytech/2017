# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class IProduct(object):
    def get_volume(self):
        raise NotImplemented()

    def get_price(self):
        raise NotImplemented()

    def get_name(self):
        raise NotImplemented()

    def get_price_promo(self):
        raise NotImplemented()

    def input_promo(self):
        raise NotImplemented()







class IVolume(object):
    def get_volume(self):
        raise NotImplemented()


class ICleanProduct(object):
    def get_price(self):
        raise NotImplemented()

    def get_name(self):
        raise NotImplemented()


class IPromo(object):
    def get_price_promo(self):
        raise NotImplemented()

    def input_promo(self):
        raise NotImplemented()


class Product(ICleanProduct, IPromo, IVolume):
    pass


class DownloadableSong(IPromo, ICleanProduct):
    pass
