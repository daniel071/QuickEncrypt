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
import os

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class Handler:
    def onSaveButtonPressed(self, button):
        save_as_file()

    def onLoadButtonPressed(self, button):
        open_file()

    def onAboutButtonClicked(self, button):
        aboutDialog = builder.get_object("aboutDialog")
        aboutDialog.run()

        aboutDialog.destroy()



builder = Gtk.Builder()
builder.add_from_file("/home/daniel/Documents/Programming/Python/QuickEncrypt/src/main.ui")
builder.connect_signals(Handler())

window = builder.get_object("QuickencryptWindow")
window.show_all()

def save_as_file():
    # Thanks to https://github.com/sriske2/umte for some of this code
    """Prompt the user with a save dialog and write the file."""
    save_dialog = Gtk.FileChooserDialog(
        "Save As", window,
        Gtk.FileChooserAction.SAVE,
        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
        Gtk.STOCK_SAVE, Gtk.ResponseType.OK))

    # Make sure the user is warned if they're overwriting an existing file.
    save_dialog.set_do_overwrite_confirmation(True)
    # Suggest a generic filename.
    save_dialog.set_current_name("untitled.txt")

    response = save_dialog.run()
    if response == Gtk.ResponseType.OK:
        # Get the path and filename then save the file.
        epicPath = save_dialog.get_filename()
        # filename = os.path.basename(self.path)
        write_file(epicPath)

    elif response == Gtk.ResponseType.CANCEL:
        pass

    save_dialog.destroy()

def write_file(file_path):
        try:
            _file = open(file_path, 'w', encoding='utf-8')
        except IOError:
            self.error("Unable to save" + file_path, "Check that you have proper permissions")
            self.path = None
            self.filename = None
            return

        # Get the buffer
        epicBuffer = builder.get_object("textBuffer")

        # Get the text from the buffer and add a \n to it
        start, end = epicBuffer.get_bounds()
        text = epicBuffer.get_text(start, end, False) + "\n"
        # Write to the file and close it
        _file.write(text)
        _file.close()
        #
        epicBuffer.set_modified(False)

        # Add the filename to the window's title
        # Remove the modification status from the title since the file has been saved.

        # TODO: Fix this
        # self.title = self.filename + ' - ' + self.name
        # self.set_title(self.title)


def open_file():
    """Open a file from disk"""
    open_dialog = Gtk.FileChooserDialog("Open",
                        window,
                        Gtk.FileChooserAction.OPEN,
                        (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
                        Gtk.STOCK_OPEN, Gtk.ResponseType.OK))

    response = open_dialog.run()
    if response == Gtk.ResponseType.OK:
        # If the user pressed OK
        # Get the path and filename
        epicPath = open_dialog.get_filename()
        epicFilename = os.path.basename(epicPath)

        # Get the buffer
        epicBuffer = builder.get_object("textBuffer")

        # TODO: Fix this
        # Add the filename to the window's title
        # self.title = self.filename + " - " + self.name
        # self.set_title(self.title)

        # Add the contents of the file to the buffer
        try:
            _file = open(epicPath, 'r', encoding='utf-8')
        except IOError:
            self.error("Unable to open" + epicPath, "Check that you have proper permissions")
            epicPath = None
            self.filename = None
            open_dialog.destroy()
            return

        epicBuffer.set_text(_file.read())
        _file.close()

        epicBuffer.set_modified(False)
        open_dialog.destroy()

    elif response == Gtk.ResponseType.CANCEL:
        # The user clicked CANCEL
        open_dialog.destroy()

    open_dialog.destroy()

Gtk.main()

