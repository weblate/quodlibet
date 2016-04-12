# -*- coding: utf-8 -*-
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation

from tests import TestCase

from quodlibet.qltk.msg import *


class TWarningMessage(TestCase):

    def test_ctr(self):
        WarningMessage(None, "title", "description").destroy()


class TErrorMessage(TestCase):

    def test_ctr(self):
        ErrorMessage(None, "title", "description").destroy()


class TCancelRevertSave(TestCase):
    def setUp(self):
        self.win = CancelRevertSave(None)

    def test_ctr(self):
        pass

    def tearDown(self):
        self.win.destroy()


class TFileReplace(TestCase):

    def setUp(self):
        self.win = ConfirmFileReplace(None, "")

    def test_ctr(self):
        pass

    def tearDown(self):
        self.win.destroy()
