#!/usr/bin/env python

import optparse
import os
import sys
import tempfile


def do_pip_download(repo_url, options):
    cmd = 'pip install'  \
        + ' --no-install' \
        + ' --no-dependencies' \
        + ' --source-dir=%s' % options.source_dir \
        + ' -e ' + repo_url \
        + '#egg=pkg'

    if options.verbose:
        print("Command: %r" % cmd)

    exit_code = os.system(cmd)
    if not exit_code == 0:
        raise RuntimeError('pip download failed for repo: %s' % repo_url)


def main():
    (options, args) = get_option_parser().parse_args()

    if options.source_dir is None:
        options.source_dir = tempfile.mkdtemp()

    do_pip_download(args[0], options)
    os.chdir(os.path.join(options.source_dir, 'pkg'))
    os.system('tox')


def get_option_parser():
    option_parser = optparse.OptionParser()

    option_parser.add_option(
        '-v', '--verbose',
        dest='verbose',
        action='store_true',
        help='Give more output')
    option_parser.add_option(
        '-s', '--source-dir', '--src-dir',
        dest='source_dir',
        default=None,
        help='Directory to download source code into')

    return option_parser


if __name__ == '__main__':
    main()


