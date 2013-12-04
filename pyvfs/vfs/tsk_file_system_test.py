#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2013 The PyVFS Project Authors.
# Please see the AUTHORS file for details on individual authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Tests for the file system implementation using the SleuthKit (TSK)."""

import os
import unittest

from pyvfs.io import os_file_io
from pyvfs.path import os_path_spec
from pyvfs.path import tsk_path_spec
from pyvfs.vfs import tsk_file_system


class TSKFileSystemTest(unittest.TestCase):
  """The unit test for the SleuthKit (TSK) file system object."""

  def setUp(self):
    """Sets up the needed objects used throughout the test."""
    test_file = os.path.join('test_data', 'image.dd')
    self._os_path_spec = os_path_spec.OSPathSpec(test_file)
    self._os_file_object = os_file_io.OSFile()
    self._os_file_object.open(self._os_path_spec, mode='rb')

  def testIntialize(self):
    """Test the initialize functionality."""
    file_system = tsk_file_system.TSKFileSystem(self._os_file_object)

    self.assertNotEquals(file_system, None)

  def testGetRootFileEntry(self):
    """Test the get root file entry functionality."""
    # TODO: this segfaults pytsk3 figure out why.
    #file_system = tsk_file_system.TSKFileSystem(self._os_file_object)

    #file_entry = file_system.GetRootFileEntry()

    #self.assertNotEquals(file_entry, None)

  def testGetFileEntryByPathSpec(self):
    """Test the get entry by path specification functionality."""
    file_system = tsk_file_system.TSKFileSystem(self._os_file_object)
    path_spec = tsk_path_spec.TSKPathSpec(inode=15)

    file_entry = file_system.GetFileEntryByPathSpec(path_spec)

    self.assertNotEquals(file_entry, None)
    # There is no way to determine the file_entry.name without a location string
    # in the path_spec or retrieving the file_entry from its parent.

    path_spec = tsk_path_spec.TSKPathSpec(inode=15, location=u'password.txt')

    file_entry = file_system.GetFileEntryByPathSpec(path_spec)

    self.assertNotEquals(file_entry, None)
    self.assertEquals(file_entry.name, u'password.txt')

if __name__ == '__main__':
  unittest.main()
