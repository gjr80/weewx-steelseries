# SteelSeries Weather Gauges extension #

A WeeWX extension to install the *SteelSeries Weather Gauges*.

The current *SteelSeries Weather Gauges* extension version is v2.7.6 which contains *SteelSeries Weather Gauges* v2.7.6.

## Description ##

The *SteelSeries Weather Gauges* extension provides an automated installation and default setup of the [SteelSeries Weather Gauges used with WeeWX](https://github.com/mcrossley/SteelSeries-Weather-Gauges/tree/master/weather_server/WeeWX).

## Pre-Requisites ##

The *SteelSeries Weather Gauges* extension requires *WeeWX v3.4.0* or greater.

**Note:** Symbolic names are used in this document to refer to some file locations on the WeeWX system. These symbolic names allow a common name to be used to refer to a directory that may be different from system to system. The following symbolic names are used in this document:

*$DOWNLOAD_ROOT*. The path to the directory containing the downloaded SteelSeries Weather Gauges extension.

*$HTML_ROOT*. The path to the directory where WeeWX generated reports are saved. This directory is normally set in the *[StdReport]* section of *weewx.conf*. Refer to [where to find things](http://weewx.com/docs/usersguide.htm#Where_to_find_things) in the WeeWX [User's Guide](http://weewx.com/docs/usersguide.htm) for further information.

## Installation ##

The preferred method to install the *SteelSeries Weather Gauges* extension is to use the *wee\_extension* utility as follows:

1.  Download the latest *SteelSeries Weather Gauges* extension from the [weewx-steelseries releases page](https://github.com/gjr80/weewx-steelseries/releases) into a directory accessible from the WeeWX machine:

        $ wget -P $DOWNLOAD_ROOT https://github.com/gjr80/weewx-steelseries/releases/download/v2.7.6/steelseries-2.7.6.tar.gz

    where *$DOWNLOAD_ROOT* is the path to the directory where the *SteelSeries Weather Gauges* extension is to be downloaded.

2.  Install the *SteelSeries Weather Gauges* extension downloaded at step 1 using the *wee\_extension* utility:

        $ wee_extension --install=$DOWNLOAD_ROOT/steelseries-2.7.6.tar.gz

    this will result in output similar to the following:

        Request to install '/var/tmp/steelseries-2.7.6.tar.gz'
        Extracting from tar archive /var/tmp/steelseries-2.7.6.tar.gz
        Saving installer file to /home/weewx/bin/user/installer/SteelSeries
        Saved configuration dictionary. Backup copy at /home/weewx/weewx.conf.20170320124410
        Finished installing extension '/var/tmp/steelseries-2.7.6.tar.gz'

3.  Restart WeeWX:

        $ sudo /etc/init.d/weewx restart

    or

        $ sudo service weewx restart

    or

        $ sudo systemctl restart weewx

This will result in WeeWX generating the WeeWX *SteelSeries Weather Gauges* data file (*gauge-data.txt*) and a demonstration page displaying the *SteelSeries Weather Gauges* (*index.html*) each report cycle. The generated files can be found in the *$HTML\_ROOT/ss* directory. The demonstration page can be displayed in a browser by pointing it at *$HTML\_ROOT/ss/index.html*.

Further customization of the SteelSeries Gauges can be performed by following the steps in the [SteelSeries Weather Gauges wiki](<https://github.com/gjr80/weewx-steelseries/wiki>).

The *SteelSeries Weather Gauges* JavaScript and CSS files are copied to the *$HTML\_ROOT/ss* directory during the first report cycle after WeeWX is started.

If the *SteelSeries Weather Gauges* are to be served by a remote web server then the contents of the *$HTML\_ROOT/ss* directory will need to be transferred from the WeeWX server to the remote web server using the FTP or RSYNC skins of via some other external means.

## Support ###

General support issues may be raised in the Google Groups [weewx-user forum](https://groups.google.com/group/weewx-user "Google Groups weewx-user forum"). Specific bugs in the *SteelSeries Weather Gauges* extension code (eg. *wee\_extension* installation errors) should be the subject of a new issue raised via the [Issues Page](https://github.com/gjr80/weewx-steelseries/issues "SteelSeries Weather Gauges extension Issues").
 
## Licensing ##

The *SteelSeries Weather Gauges* extension is licensed under the [GNU Public License v2](https://github.com/gjr80/weewx-steelseries/blob/master/LICENSE "SteelSeries Weather Gauges extension License"). The *SteelSeries Weather Gauges* code included in the *SteelSeries Weather Gauges* extension is licensed by Mark Crossley under the [GNU Public License v2](https://github.com/mcrossley/SteelSeries-Weather-Gauges/blob/master/LICENSE "SteelSeries Weather Gauges License"). The *SteelSeries Weather Gauges* source code included in the *SteelSeries Weather Gauges* extension is available from the GitHub [SteelSeries Weather Gauges repository](https://github.com/mcrossley/SteelSeries-Weather-Gauges).
