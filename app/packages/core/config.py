# -*- coding: utf-8 -*-
import os
import re
import json


class Config:
    def __init__(self):
        return

    @classmethod
    def basedir(cls):
        pattern = re.compile('^(.*)/app/packages/core/config')
        matched = pattern.match(os.path.abspath(__file__).replace("\\", "/"))
        return matched.group(1)

    @classmethod
    def view_dir(cls):
        return cls.basedir() + '/app/views'

    @classmethod
    def get(cls, key, name='application'):
        try:
            basedir = cls.basedir()

            with open(basedir + "/config/" + name + ".json", mode="r", encoding="utf-8") as fp:
                config = json.load(fp)
            if key in config:
                return config[key]
            else:
                return None
        except IOError as e:
            print(e.strerror)
            return None
