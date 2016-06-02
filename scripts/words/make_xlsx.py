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
from utils.words import WordsList
from utils.xlsx import XlsxFile

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def main():
    word_list = WordsList(os.path.join(DATA_DIR, 'word_list'), os.path.join(DATA_DIR, 'cache'))
    XlsxFile('words.xlsx').write(word_list.words)


if __name__ == '__main__':
    main()
