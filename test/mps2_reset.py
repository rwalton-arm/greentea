# Copyright (c) 2021, Arm Limited and affiliates.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import unittest
from unittest.mock import patch
import os
import time

from htrun.host_tests_plugins.module_reset_mps2 import HostTestPluginResetMethod_MPS2

class MPS2ResetTestCase(unittest.TestCase):

    def setUp(self):
        self.mps2_reset_plugin = HostTestPluginResetMethod_MPS2()

    def tearDown(self):
        pass

    @patch("os.name", "posix")
    @patch("time.sleep")
    @patch("htrun.host_tests_plugins.module_reset_mps2.HostTestPluginResetMethod_MPS2.run_command")
    def test_check_sync(self, run_command_function, sleep_function):
        # Check that a sync call has correctly been executed
        self.mps2_reset_plugin.execute("reboot.txt", disk=".")
        args, _ = run_command_function.call_args
        self.assertTrue("sync" in args[0])
        os.remove("reboot.txt")

if __name__ == '__main__':
    unittest.main()
