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
from jinja2 import Environment, FileSystemLoader

from utils.words import WordsList


def main(out_file):
    data_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    template_dir = os.path.join(data_dir, 'templates')
    template_file = os.path.join(template_dir, 'nameit.h')
    if not os.path.isfile(template_file):
        raise Exception('Template not found {}'.format(template_file))

    word_list = WordsList(os.path.join(data_dir, 'word_list'), os.path.join(data_dir, 'cache'))
    template_environment = Environment(loader=FileSystemLoader(template_dir),
                                       autoescape=False,
                                       trim_blocks=False)

    with open(out_file, 'w') as generated_file:
        template = template_environment.get_template(os.path.basename(template_file))
        data = template.render({'words': word_list.words})
        generated_file.write(data)


if __name__ == '__main__':
    main('nameit.h')
