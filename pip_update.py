#!/usr/bin/env python3
"""Pip3 Updater

This module creates a class which calls the sysetem's pip3 and gets a list of
packages that can be updated and upgrades them.

Example:
    Create an object using UpdateUpgradePip: example = UpdateUpgradePip()
    Update the object's packages with outdated modules: example.update()
    Upgrade the system's packages based on the update list: example.upgrade()

"""

from subprocess import check_output, call
import re


class UpdateUpgradePip(object):
    """Allows one to call pip3 locally and update and upgrade pacakges"""

    def __init__(self):
        self.compile_regex = re.compile(r"^\S*")
        self.update_list = []

    def update(self):
        """Updates local pip3 packages"""

        pip_update_list = check_output("pip3 list -o", shell=True).decode('UTF-8')

        for package in pip_update_list.strip().split('\n'):
            package_to_update = self.compile_regex.search(package).group()
            self.update_list.append(package_to_update)

    def upgrade(self):
        """Calls pip3 with upgrade flag for particular package"""

        self.number_of_packages = len(self.update_list)
        self.counter = 1

        for package in self.update_list:
            print('Upgrading "{}" ({}/{})'.format(package, self.counter, self.number_of_packages))
            self.counter += 1

            call('pip3 install {} --upgrade'.format(package), shell=True)

            print("------------", end="\n\n")

if __name__ == '__main__':
    """Standard usage for updating pip3 modules"""
    pip_update = UpdateUpgradePip()
    pip_update.update()
    pip_update.upgrade()
