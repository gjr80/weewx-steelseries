"""
This program is free software; you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation; either version 2 of the License, or (at your option) any later
version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

                  Installer for SteelSeries Weather Gauges

Version: 2.7.4-1                                  Date: 9 May 2020

Revision History
    9 May 2020          v2.7.4-1
        - upgraded to SteelSeries Weather Gauges version 2.7.4(minor tweaks)
    17 September 2019   v2.7.4
        - upgraded to SteelSeries Weather Gauges version 2.7.4
    27 March 2019       v2.7.3
        - upgraded to SteelSeries Weather Gauges version 2.7.3
    31 August 2017      v2.6.3
        - upgraded to SteelSeries Weather Gauges version 2.6.3
    13 June 2017        v2.6.1
        - initial release as a weeWX extension
        - version number chosen to match SteelSeries Weather Gauges version
"""

import weewx

from distutils.version import StrictVersion
from setup import ExtensionInstaller

REQUIRED_VERSION = "3.4.0"
SSWG_VERSION = "2.7.4-1"


def loader():
    return SswgInstaller()


class SswgInstaller(ExtensionInstaller):
    def __init__(self):
        if StrictVersion(weewx.__version__) < StrictVersion(REQUIRED_VERSION):
            msg = "%s requires weeWX %s or greater, found %s" % (''.join('SteelSeries Weather Gauges ', SSWG_VERSION),
                                                                 REQUIRED_VERSION,
                                                                 weewx.__version__)
            raise weewx.UnsupportedFeature(msg)
        super(SswgInstaller, self).__init__(
            version=SSWG_VERSION,
            name='SteelSeries',
            description='A weeWX extension for the SteelSeries Weather Gauges.',
            author="Packaged by Gary Roderick, SteelSeries gauges by Gerrit Grunwald, "
                 "Weather Gauges scripts by Mark Crossley and weeWX skin by Matthew Wall",
            author_email="gjroderick<@>gmail.com",
            config={
                'StdReport': {
                    'SteelSeries': {
                        'skin': 'ss',
                        'HTML_ROOT': 'ss',
                        'Units': {
                            'Groups': {
                                'group_altitude': 'foot',  # foot or meter
                                'group_pressure': 'hPa',   # hPa, inHg or mbar
                                'group_rain': 'mm',        # mm or inch
                                'group_rainRate': 'mm_per_hour',   # mm_per_hour or inch_per_hour
                                'group_speed': 'km_per_hour',      # km_per_hour, mile_per_hour,
                                                                   # meter_per_second or knot
                                'group_temperature': 'degree_C'    # degree_C or degree_F
                            },
                            'StringFormats': {
                                'degree_C': '%.1f',
                                'degree_F': '%.1f',
                                'degree_compass': '%.0f',
                                'foot': '%.0f',
                                'hPa': '%.1f',
                                'inHg': '%.3f',
                                'inch': '%.2f',
                                'inch_per_hour': '%.2f',
                                'km': '%.1f',
                                'km_per_hour': '%.0f',
                                'knot': '%.0f',
                                'mbar': '%.1f',
                                'meter': '%.0f',
                                'meter_per_second': '%.1f',
                                'mile': '%.1f',
                                'mile_per_hour': '%.0f',
                                'mm': '%.1f',
                                'mmHg': '%.1f',
                                'mm_per_hour': '%.1f',
                                'percent': '%.0f',
                                'uv_index': '%.1f',
                                'watt_per_meter_squared': '%.0f'
                            }
                        }
                    }
                }
            },
            files=[('skins/ss', ['skins/ss/gauge-data.txt.tmpl',
                                 'skins/ss/index.html.tmpl',
                                 'skins/ss/skin.conf',
                                 'skins/ss/scripts/gauges.js',
                                 'skins/ss/scripts/language.min.js',
                                 'skins/ss/scripts/RGraph.common.core.min.js',
                                 'skins/ss/scripts/RGraph.rose.min.js',
                                 'skins/ss/scripts/steelseries_tween.min.js',
                                 'skins/ss/css/gauges-ss.css'
                                 ]
                    )]
        )
