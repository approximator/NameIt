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

#include <random>
#include <string>
#include <vector>

namespace nameit
{

class RandomName
{
public:
    operator std::string() const
    {
        return randomElement(adjectives) + "_" + randomElement(nouns);
    }

private:
    const std::string& randomElement(const std::vector<std::string>& elements) const
    {
        std::random_device random_device;
        std::mt19937 engine{ random_device() };
        std::uniform_int_distribution<int> dist(0, elements.size() - 1);
        return elements[dist(engine)];
    }

    static const std::vector<std::string> nouns;
    static const std::vector<std::string> adjectives;
};

const std::vector<std::string> RandomName::nouns{ "abuse", "agony", "alliteration", "anonymous", "apocalypse",
    "armageddon", "backbone", "backstabbing", "belief", "blood", "bonanza", "bravery", "buffoon", "bully", "cabotage",
    "cadaver", "caution", "cheer", "crush", "cynical", "defiance", "disposition", "dollar", "eye-opening", "feast",
    "fortitude", "freebie", "gambling", "gift", "guise", "hurricane", "hyperbole", "irony", "jail", "jurisdiction",
    "karma", "lawsuit", "lifetime", "looming", "loser", "lunatic", "meltdown", "miracle", "mired", "misanthrope",
    "oxymoron", "paradigm", "payback", "piranha", "pitfall", "pluck", "poison", "prison", "privacy", "profit",
    "research", "rich", "salopettes", "slaughter", "snob", "spectacular", "spine", "strange", "surge", "tank", "tawdry",
    "terror", "trap", "treasure", "triumph", "valor", "victim", "victory", "warning"
};

const std::vector<std::string> RandomName::adjectives{
    "ambiguous", "authentic", "banned", "benevolent", "best", "blacklisted", "bloodcurdling", "brazen", "capricious",
    "cheap", "collapsible", "confidential", "controversial", "dangerous", "disgusting", "double", "dumb", "embarrassed",
    "endorsed", "evil", "fearless", "feeble", "frantic", "frenzy", "grateful", "greatest", "guaranteed", "hazardous",
    "hidden", "illegal", "inexpensive", "insidious", "lascivious", "lethargic", "lewd", "loathsome", "lonely", "lost",
    "lucid", "luxurious", "mind-blowing", "naughty", "obnoxious", "official", "protected", "provocative", "quixotic",
    "rambunctious", "reduced", "risky", "scary", "secure", "sensational", "serene", "shameless", "silly", "sleeping",
    "snooty", "snotty", "stupid", "surprising", "sweaty", "tantalizing", "toxic", "triple", "unauthorized", "uncanny",
    "underhanded", "vague", "volatile", "vulnerable", "wonderful", "wondrous", "wonky"
};

}

#endif /* __NAME_IT_H_ */
