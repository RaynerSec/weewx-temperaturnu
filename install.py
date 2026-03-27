# installer for temperatur.nu
# Copyright 2026 Based on weewx-windy by Matthew Wall
# Distributed under the terms of the GNU Public License (GPLv3)

from weecfg.extension import ExtensionInstaller

def loader():
    return TemperaturNuInstaller()

class TemperaturNuInstaller(ExtensionInstaller):
    def __init__(self):
        super(TemperaturNuInstaller, self).__init__(
            version="0.1",
            name='temperaturnu',
            description='Upload weather data to Temperatur.nu.',
            author="RC Chuah (Based on weewx-windy by Matthew Wall)",
            author_email="44928288+rc-chuah@users.noreply.github.com",
            restful_services='user.temperaturnu.TemperaturNu',
            config={
                'StdRESTful': {
                    'TemperaturNu': {
                        'apikey': 'replace_me'}}},
            files=[('bin/user', ['bin/user/temperaturnu.py'])]
        )
