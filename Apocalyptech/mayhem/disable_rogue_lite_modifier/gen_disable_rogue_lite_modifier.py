#!/usr/bin/env python3
# vim: set expandtab tabstop=4 shiftwidth=4:

# Copyright 2019-2020 Christopher J. Kucera
# <cj@apocalyptech.com>
# <http://apocalyptech.com/contact.php>
#
# This Borderlands 3 Hotfix Mod is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation, either version 3 of
# the License, or (at your option) any later version.
#
# This Borderlands 3 Hotfix Mod is distributed in the hope that it will
# be useful, but WITHOUT ANY WARRANTY; without even the implied
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this Borderlands 3 Hotfix Mod.  If not, see
# <https://www.gnu.org/licenses/>.

import sys
sys.path.append('../../../python_mod_helpers')
from bl3hotfixmod.bl3hotfixmod import Mod

mod = Mod('disable_rogue_lite_modifier.bl3hotfix',
        'Disable "Rogue Lite" Modifier',
        'Apocalyptech',
        [
            "As the title says, makes it so 'Rogue Lite' will never show up",
            "as a Very Hard Mayhem 2.0 modifier.  I'd always reroll if I get",
            "that one, so this just saves me some keypresses.",
        ],
        lic=Mod.CC_BY_SA_40,
        v='1.0.0',
        cats='mayhem',
        )

mod.reg_hotfix(Mod.PATCH, '',
        '/Game/PatchDLC/Mayhem2/ModifierSets/ModSet_Mayhem2_VeryHard',
        'ModifierSets.ModifierSets[1].Weight',
        0)

mod.close()
