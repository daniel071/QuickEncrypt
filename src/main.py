# main.py
#
# Copyright 2020 Daniel Pavela
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
    def onSaveButtonPressed(self, button):
        print("Hello World!")


builder = Gtk.Builder()
builder.add_from_file("/home/daniel/Documents/Programming/Python/QuickEncrypt/src/main.ui")
builder.connect_signals(Handler())

window = builder.get_object("QuickencryptWindow")
window.show_all()

Gtk.main()

