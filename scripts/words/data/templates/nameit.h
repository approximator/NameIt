/*!
 * @file nameit.h
 *
 * Copyright © 2016 Oleksii Aliakin. All rights reserved.
 * Author: Oleksii Aliakin (alex@nls.la)
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef __NAME_IT_H_
#define __NAME_IT_H_

{% set nouns = words|selectattr("part_of_speech", "equalto", "noun")|selectattr("definition") -%}
{% set adjectives = words|selectattr("part_of_speech", "equalto", "adjective")|selectattr("definition") -%}

#include <string>
#include <vector>
#include <random>

namespace nameit {

class RandomName
{
public:
    operator std::string() const {
        return randomElement(adjectives) + "_" + randomElement(nouns);
    }

private:
    const std::string& randomElement(const std::vector<std::string>& elements) const {
        std::random_device random_device;
        std::mt19937 engine { random_device() };
        std::uniform_int_distribution<int> dist(0, elements.size() - 1);
        return elements[dist(engine)];
    }

    static const std::vector<std::string> nouns;
    static const std::vector<std::string> adjectives;
};

const std::vector<std::string> RandomName::nouns {
{% set pipe = joiner(",") %}
{%- for noun in nouns-%}
    {{ pipe() }}"{{ noun.word }}"
{% endfor %}
};

const std::vector<std::string> RandomName::adjectives {
{% set pipe = joiner(",") %}
{%- for adjective in adjectives-%}
    {{ pipe() }}"{{ adjective.word }}"
{% endfor %}
};

}

#endif /* __NAME_IT_H_ */
