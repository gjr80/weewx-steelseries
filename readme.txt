The SteelSeries Weather Gauges extension allows automated installation and
default setup of the SteelSeries Weather Gauges as per the SteelSeries Weather
Gauges GitHub repository (https://github.com/mcrossley/SteelSeries-Weather-Gauges).
Once the SteelSeries Weather Gauges extension is installed WeeWX will generate
a gauge-data.txt file and a demonstration html page displaying the SteelSeries
Weather Gauges using WeeWX sourced data. These files are updated each report
cycle.

The SteelSeries Weather Gauges extension consists of a skin that generates
gauge-data.txt and index.html each report cycle. The skin also contains the
SteelSeries Weather Gauges JavaScript and CSS files used in rendering the
gauges. The JavaScript and CSS files are copied once to the WeeWX symbolic
$HTML_ROOT directory during the first report cycle after WeeWX has been
started.

The SteelSeries Weather Gauges extension version number is identical to the
version number of the SteelSeries Weather Gauges code included within the
extension.

Pre-Requisites

The SteelSeries Weather Gauges extension requires weeWX v3.4.0 or greater.

    Note: Symbolic names are used below to refer to some file location on the
          WeeWX system. These symbolic names allow a common name to be used to
          refer to a directory that may be different from system to system. The
          following symbolic names are used in this document:

          - $DOWNLOAD_ROOT. The path to the directory containing the downloaded
            SteelSeries Weather Gauges extension.

          - $HTML_ROOT. The path to the directory where WeeWX generated reports
            are saved. This directory is normally set in the [StdReport]
            section of weewx.conf. Refer to 'where to find things' in the WeeWX
            User's Guide http://weewx.com/docs/usersguide.htm#Where_to_find_things
            for further information.

          - $SKIN_ROOT. The path to the directory where WeeWX skin directories
            are located. This directory is normally set in the [StdReport]
            section of weewx.conf. Refer to 'where to find things' in the WeeWX
            User's Guide http://weewx.com/docs/usersguide.htm#Where_to_find_things
            for further information.


Installation Instructions

The preferred method of installation of the SteelSeries Weather Gauges
extension is through use of the wee_extension utility. However, if this is not
possible the SteelSeries Weather Gauges extension may be installed manually.

Installation using the wee_extension utility

1.  Download the latest SteelSeries Weather Gauges extension from the
weewx-steelseries releases page
(https://github.com/gjr80/weewx-steelseries_gauges/releases) into a directory
accessible from the WeeWX machine:

    $ wget -P $DOWNLOAD_ROOT https://github.com/gjr80/weewx-steelseries/weather_gauges/releases/download/v2.7.3/steelseries-2.7.3.tar.gz

	where $DOWNLOAD_ROOT is the path to the directory where the SteelSeries
    Weather Gauges extension is to be downloaded.

2.  Install the SteelSeries Weather Gauges extension downloaded at step 1 using
the wee_extension utility:

    $ wee_extension --install=$DOWNLOAD_ROOT/steelseries-2.7.3.tar.gz

    This will result in output similar to the following:

        Request to install '/var/tmp/steelseries-2.7.3.tar.gz'
        Extracting from tar archive /var/tmp/steelseries-2.7.3.tar.gz
        Saving installer file to /home/weewx/bin/user/installer/SteelSeries
        Saved configuration dictionary. Backup copy at /home/weewx/weewx.conf.20170320124410
        Finished installing extension '/var/tmp/steelseries-2.7.3.tar.gz'

3.  Restart WeeWX:

    $ sudo /etc/init.d/weewx restart

	or

    $ sudo service weewx restart

This will result in WeeWX generating the weeWX SteelSeries Weather Gauges data
file (gauge-data.txt) and a demonstration page displaying the Steel Series
Weather Gauges (index.html) each report cycle. The generated files can be found
in the $HTML_ROOT/ss directory. The demonstration page can be displayed in a
browser by pointing it at $HTML_ROOT/ss/index.html.

Further customization of the SteelSeries Gauges can be performed by following
the Customizing the SteelSeries Gauges section below.

Manual installation

1.  Download the latest SteelSeries Weather Gauges extension from the
weewx-steelseries_gauges releases page
(https://github.com/gjr80/weewx-steelseries_gauges/releases) into a directory
accessible from the WeeWX machine:

     $ wget -P $DOWNLOAD_ROOT https://github.com/gjr80/weewx-steelseries/weather_gauges/releases/download/v2.7.3/steelseries-2.7.3.tar.gz

	where $DOWNLOAD_ROOT is the path to the directory where the SteelSeries
    Weather Gauges extension is to be downloaded.

2.  Unpack the extension as follows:

    $ tar xvfz steelseries-2.7.3.tar.gz

3.  Copy files from within the resulting directory as follows:

    $ cp -R steelseries/skins/* $SKIN_ROOT

	replacing the symbolic name $SKIN_ROOT with the nominal location for your
    installation.

4.  Add the SteelSeries Weather Gauges skin to the report service settings in
weewx.conf:

    -   edit weewx.conf

        $ vi weewx.conf

    -   locate the [StdReport] section and add the following stanza:

        [[SteelSeries]]
            HTML_ROOT = public_html/ss
            skin = ss
            [[[Units]]]
                [[[[StringFormats]]]]
                    mm_per_hour = %.1f
                    mile_per_hour = %.0f
                    degree_compass = %.0f
                    degree_C = %.1f
                    inHg = %.3f
                    mmHg = %.1f
                    meter_per_second = %.1f
                    meter = %.0f
                    mile = %.1f
                    uv_index = %.1f
                    watt_per_meter_squared = %.0f
                    percent = %.0f
                    km_per_hour = %.0f
                    inch = %.2f
                    degree_F = %.1f
                    knot = %.0f
                    foot = %.0f
                    hPa = %.1f
                    mbar = %.1f
                    inch_per_hour = %.2f
                    mm = %.1f
                    km = %.1f
                [[[[Groups]]]]
                    group_temperature = degree_C
                    group_altitude = foot
                    group_pressure = hPa
                    group_rain = mm
                    group_rainRate = mm_per_hour
                    group_speed = km_per_hour

    -   save weewx.conf

5.  Restart WeeWX:

    $ sudo /etc/init.d/weewx restart

	or

    $ sudo service weewx restart

This will result in WeeWX generating the weeWX SteelSeries Weather Gauges data
file (gauge-data.txt) and a demonstration page displaying the SteelSeries
Weather Gauges (index.html) each report cycle. The generated files can be found
in the $HTML_ROOT/ss directory. The demonstration page can be displayed in a
browser by pointing it at $HTML_ROOT/ss/index.html.

Further customization of the SteelSeries Gauges can be performed by following
the Customizing the SteelSeries Gauges section below.


Customizing the SteelSeries Gauges

Setting station timeout

The SteelSeries Weather Gauges extension is configured with a station timeout
value of 10 minutes. If your station uses an archive period of 10 minutes or
more you may wish to change the station timeout value to a more suitable value.
To change the station timeout value:

    -   edit $SKIN_ROOT/ss/scripts/gauges.js:

        $ vi $SKIN_ROOT/ss/scripts/gauges.js

    -   locate the stationTimeout setting and change as required, eg:

        stationTimeout : 20,      // set to twice archive interval, in minutes

    -   save $SKIN_ROOT/ss/scripts/gauges.js

    -   restart WeeWX:

        $ sudo /etc/init.d/weewx restart

	    or

        $ sudo service weewx restart

Displaying solar radiation and UV gauges

The SteelSeries Weather Gauges extension is configured to display the solar
radiation and UV gauges. If your station does not have these sensors you may
hide these gauges by editing gauges.js. To hide the solar radiation and UV
gauges:

    -   edit $SKIN_ROOT/ss/scripts/gauges.js:

        $ vi $SKIN_ROOT/ss/scripts/gauges.js

    -   locate the showUvGauge and showSolarGauge settings and set both to
        false, eg:

        showUvGauge        : false,              // Display the UV Index gauge
        showSolarGauge     : false,              // Display the Solar gauge

    -   save $SKIN_ROOT/ss/scripts/gauges.js

    -   restart WeeWX:

        $ sudo /etc/init.d/weewx restart

	    or

        $ sudo service weewx restart


Changing the gauge-data.txt units

The gauge-data.txt file generated by the SteelSeries Weather Gauges extension
defaults to Metric units for all observations except cloudbase. Whilst the
SteelSeries Gauges page provides the ability to set the display units, the
units used in gauge-data.txt are the units used when the SteelSeries Gauges
page is first displayed. To change the units used in gauge-data.txt:

    -   edit weewx.conf:

        $ vi weewx.conf

    -   locate the [StdReport], [[SteelSeries]], [[[Units]]], [[[[Groups]]]]
        stanza and change the settings as required:

        [StdReport]
            ....
            [[SteelSeries]]
                ....
                [[[Units]]]
                    ....
                    [[[[Groups]]]]
                        group_temperature = degree_C
                        group_altitude = foot
                        group_pressure = hPa
                        group_rain = mm
                        group_rainRate = mm_per_hour
                        group_speed = km_per_hour

        Note: The units used in gauge-data.txt merely set the initial units
              displayed by the SteelSeries Gauges page. The SteelSeries Gauges
              include a number of option selectors that set the displayed
              units. Once these options are set the displayed units will remain
              as set irrespective of the units used in gauge-data.txt.

    -   save weewx.conf

    -   force a WeeWX configuration reload:

        $ sudo /etc/init.d/weewx reload

        or

        $ sudo service weewx reload