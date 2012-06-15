import subprocess
import unittest

import piptox


class PipToxTests(unittest.TestCase):

    def __test_port_for_success(self):
        output = self._run_piptox('git+https://github.com/kmike/port-for.git')
        self.assertTrue('py26: commands succeeded' in output)
        self.assertTrue('py27: commands succeeded' in output)

    def test_fail(self):
        output = self._run_piptox('git+https://zd42.com/km/p.git')
        self.assertTrue('pip download failed' in output)

    def test_help(self):
        output = self._run_piptox('--help')
        self.assertTrue('piptox [options]' in output)

    def _run_piptox(self, *args):
        process = subprocess.Popen(
            ('piptox',) + args,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        output, _unused_err = process.communicate()
        output = output.decode('utf-8')
        _retcode = process.poll()

        return output
