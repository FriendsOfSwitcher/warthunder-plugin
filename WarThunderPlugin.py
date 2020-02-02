#  Switcher, a tool for managing graphics and keymap profiles in games.
#  Copyright (C) 2020 Sam McCormack
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program. If not, see <https://www.gnu.org/licenses/>.
import os
from os import path

from src.api.Plugin import Plugin


class WarThunderPlugin(Plugin):

    def initialise(self) -> None:
        pass

    def identify(self, folder_path: str) -> bool:
        _path, name = path.split(folder_path)
        if name != "War Thunder":
            return False

        launcher = "launcher.exe" and "win64" in os.listdir(folder_path)
        start = "aces.exe" in os.listdir(path.join(folder_path, "win64"))
        return launcher and start

    def save_profile(self, *types) -> None:
        pass

    def get_executable(self) -> str:
        pass
