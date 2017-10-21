# -*- coding: utf-8 -*-

__author__ = 'sobolevn'


class EmailSender(object):
    last_email = None

    def _send_email_by_smtp(self, to, subject, text):
        pass  # imagine, that email is sent

    def _log(self, *args):
        print('Sent email with params: {}'.format(args))

    def send_email(self, to, subject, text):
        self._send_email_by_smtp(to, subject, text)

        self.__class__.last_email = (to, subject, text, )
        self._log(to, subject, text)








class Logger(object):
    def log(self, pattern, *args):
        raise NotImplemented()


class ConsoleLogger(Logger):
    def log(self, pattern, *args):
        print(pattern.format(args))


class Storage(object):
    _obj = None

    def __new__(cls, *args, **kwargs):
        if cls._obj is None:
            cls._obj = object.__new__(cls)
            cls._repository = {}
        return cls._obj

    @classmethod
    def store(cls, key, value):
        cls._repository[key] = value

    @classmethod
    def get(cls, key):
        return cls._repository[key]


class RefactoredEmailSender(object):
    def __init__(self, logger, storage):
        self.logger = logger
        self.storage = storage

    def _send_email_by_smtp(self, to, subject, text):
        pass

    def send_email(self, to, subject, text):
        self._send_email_by_smtp(to, subject, text)

        self.storage.store('last_email', (to, subject, text, ))
        self.logger.log('Sent with params: {}', to, subject, text)


if __name__ == '__main__':
    EmailSender().send_email(
        'mail@sobolevn.me',
        'This is a bad design',
        'You know it? Make some changes!',
    )

    # Right one:
    RefactoredEmailSender(
        ConsoleLogger(), Storage()
    ).send_email(
        'mail@sobolevn.me',
        'This is better',
        'Some changes made!',
    )
