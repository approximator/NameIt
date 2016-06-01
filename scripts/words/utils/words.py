#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright © 2016 Oleksii Aliakin. All rights reserverd.
# Author: Oleksii Aliakin (alex@nls.la)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
import time
import json
import requests


class Word(object):

    def __init__(self, word, part_of_speech, definition, example):
        self.__word = word.strip()
        self.__part_of_speech = part_of_speech.strip()
        self.__definition = definition.strip()
        self.__example = example.strip()

    @property
    def word(self):
        return self.__word

    @property
    def part_of_speech(self):
        return self.__part_of_speech

    @property
    def definition(self):
        return self.__definition

    @property
    def example(self):
        return self.__example


class WordsList(object):

    def __init__(self, word_list_file, cache_dir):
        self.__word_list_file = word_list_file
        self.__cache_dir = cache_dir
        self.__is_cache_valid = False
        self.__api_url = 'http://api.pearson.com/v2/dictionaries/entries'

    @property
    def words(self):
        if not self.__is_cache_valid:
            self.update_cache()
            self.__is_cache_valid = True
        return map(lambda wrd: self.make_word(wrd), self.load_word_list())

    def load_word_list(self):
        return [word.strip().lower()
                for word in open(self.__word_list_file, 'r').readlines() if word.strip()]

    def make_word(self, word_name):
        part_of_speech = ''
        definition = ''
        example = ''
        info_file_name = os.path.join(self.__cache_dir, word_name)
        if os.path.isfile(info_file_name):
            with open(info_file_name) as info_file:
                json_data = json.loads(info_file.read())
                results = json_data.get('results', None)
                if results:
                    results = results[0]
                    part_of_speech = results.get('part_of_speech', '')
                    senses = results.get('senses', None)
                    if senses:
                        senses = senses[0]
                        definition = senses.get('definition', '')
                        if isinstance(definition, list):
                            definition = definition[0]
                        example = senses.get('examples', [{}])[0].get('text', '')
        return Word(word_name, part_of_speech, definition, example)

    def update_cache(self):
        words = self.load_word_list()
        for word in words:
            info_file = os.path.join(self.__cache_dir, word)
            try:
                if os.path.isfile(info_file):
                    continue
                r = requests.get(self.__api_url, params={'headword': word})
                print(r.url)
                with open(info_file, 'w') as data_file:
                    data_file.write(r.text.encode('utf-8'))
                time.sleep(2)
            except Exception as ex:
                print(word)
                print(str(ex))
