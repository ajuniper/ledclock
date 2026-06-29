# LED Clock for running on Raspberry Pi Zero

## Packages
* LED driver: luma.led_matrix
* Broadlink: mjg59 / python-broadlink 
* irsling: see gpclk branch of ir-slinger

## Symlinks
```
temperature -> /sys/class/thermal/thermal_zone0/temp
/etc/localtime -> /usr/share/zoneinfo/Europe/London
```

## Edits
* /etc/exim4/exim4.conf:MAIN_LOCAL_DOMAINS=@:localhost:pi0.aj
* /etc/timezone: Europe/London
* /etc/mailname: xxx.yyy
* /etc/aliases: root: aaa@xxx.yyy
* /etc/hosts: 127.0.1.1   shortname shortname.fqdn
* /etc/hostname: shortname
* mkdir -m 777 /run/clockmsg

## Services
* ledclock
* ledclockweb
* serial-getty@ttyS0.service
* setserial.service
* rsyslog.service
* incron.service
* exim4.service
* atd.service
* audioamp.service

## Packages (from Stretch)
```
ii  adduser                                        3.115                        all                          add and remove users and groups
ii  adwaita-icon-theme                             3.22.0-1+deb9u1              all                          default icon theme of GNOME
ii  alsa-utils                                     1.1.3-1                      armhf                        Utilities for configuring and using ALSA
ii  apt                                            1.4.11                       armhf                        commandline package manager
ii  apt-listchanges                                3.10                         all                          package change history notification tool
ii  apt-transport-https                            1.4.11                       armhf                        https download transport for APT
ii  apt-utils                                      1.4.11                       armhf                        package management related utility programs
ii  aptitude                                       0.8.7-1                      armhf                        terminal-based package manager
ii  aptitude-common                                0.8.7-1                      all                          architecture independent files for the aptitude package manager
ii  at                                             3.1.20-3                     armhf                        Delayed job execution and batch processing
ii  at-spi2-core                                   2.22.0-6+deb9u1              armhf                        Assistive Technology Service Provider Interface (dbus core)
ii  avahi-daemon                                   0.6.32-2                     armhf                        Avahi mDNS/DNS-SD daemon
ii  base-files                                     9.9+rpi1+deb9u13             armhf                        Debian base system miscellaneous files
ii  base-passwd                                    3.5.43                       armhf                        Debian base system master password and group files
ii  bash                                           4.4-5                        armhf                        GNU Bourne Again SHell
ii  bash-completion                                1:2.1-4.3                    all                          programmable completion for the bash shell
ii  bind9-host                                     1:9.10.3.dfsg.P4-12.3+deb9u7 armhf                        Version of 'host' bundled with BIND 9.X
ii  binutils                                       2.28-5                       armhf                        GNU assembler, linker and binary utilities
ii  blends-tasks                                   0.6.96                       all                          Debian Pure Blends tasks for new installations
ii  bluealsa                                       0.9                          armhf                        Bluetooth ALSA Audio backend
ii  bluez                                          5.43-2+rpt2+deb9u2           armhf                        Bluetooth tools and daemons
ii  bluez-firmware                                 1.2-3+rpt7                   all                          Firmware for Bluetooth devices
ii  bsdmainutils                                   9.0.12+nmu1                  armhf                        collection of more utilities from FreeBSD
ii  bsdutils                                       1:2.29.2-1+deb9u1            armhf                        basic utilities from 4.4BSD-Lite
ii  build-essential                                12.3                         armhf                        Informational list of build-essential packages
ii  bzip2                                          1.0.6-8.1                    armhf                        high-quality block-sorting file compressor - utilities
ii  ca-certificates                                20200601~deb9u1              all                          Common CA certificates
ii  cifs-utils                                     2:6.7-1                      armhf                        Common Internet File System utilities
ii  console-setup                                  1.164                        all                          console font and keymap setup program
ii  console-setup-linux                            1.164                        all                          Linux specific part of console-setup
ii  coreutils                                      8.26-3                       armhf                        GNU core utilities
ii  cpio                                           2.11+dfsg-6                  armhf                        GNU cpio -- a program to manage archives of files
ii  cpp                                            4:6.3.0-4                    armhf                        GNU C preprocessor (cpp)
ii  cpp-6                                          6.3.0-18+rpi1+deb9u1         armhf                        GNU C preprocessor
ii  crda                                           3.18-1                       armhf                        wireless Central Regulatory Domain Agent
ii  cron                                           3.0pl1-128+deb9u1            armhf                        process scheduling daemon
ii  curl                                           7.52.1-5+deb9u13             armhf                        command line tool for transferring data with URL syntax
ii  dash                                           0.5.8-2.4                    armhf                        POSIX-compliant shell
ii  dbus                                           1.10.32-0+deb9u1             armhf                        simple interprocess messaging system (daemon and utilities)
ii  dc                                             1.06.95-9                    armhf                        GNU dc arbitrary precision reverse-polish calculator
ii  dconf-gsettings-backend:armhf                  0.26.0-2                     armhf                        simple configuration storage system - GSettings back-end
ii  dconf-service                                  0.26.0-2                     armhf                        simple configuration storage system - D-Bus service
ii  debconf                                        1.5.61                       all                          Debian configuration management system
ii  debconf-i18n                                   1.5.61                       all                          full internationalization support for debconf
ii  debconf-utils                                  1.5.61                       all                          debconf utilities
ii  debianutils                                    4.8.1.1                      armhf                        Miscellaneous utilities specific to Debian
ii  device-tree-compiler                           1.4.4-1                      armhf                        Device Tree Compiler for Flat Device Trees
ii  dh-python                                      2.20170125                   all                          Debian helper tools for packaging Python libraries and applications
ii  dhcpcd5                                        1:6.11.5-1+rpt7              armhf                        DHCPv4, IPv6RA and DHCPv6 client with IPv4LL support
ii  diffutils                                      1:3.5-3                      armhf                        File comparison utilities
ii  distro-info-data                               0.36                         all                          information about the distributions' releases (data files)
ii  dmidecode                                      3.0-4                        armhf                        SMBIOS/DMI table decoder
ii  dmsetup                                        2:1.02.137-2                 armhf                        Linux Kernel Device Mapper userspace library
ii  dosfstools                                     4.1-1                        armhf                        utilities for making and checking MS-DOS FAT filesystems
ii  dphys-swapfile                                 20100506-3                   all                          Autogenerate and use a swap file
ii  dpkg                                           1.18.25                      armhf                        Debian package management system
ii  dpkg-dev                                       1.18.25                      all                          Debian package development tools
ii  e2fslibs:armhf                                 1.43.4-2+deb9u2              armhf                        ext2/ext3/ext4 file system libraries
ii  e2fsprogs                                      1.43.4-2+deb9u2              armhf                        ext2/ext3/ext4 file system utilities
ii  ed                                             1.10-2.1                     armhf                        classic UNIX line editor
ii  exim4-base                                     4.89-2+deb9u7                armhf                        support files for all Exim MTA (v4) packages
ii  exim4-config                                   4.89-2+deb9u7                all                          configuration for the Exim MTA (v4)
ii  exim4-daemon-light                             4.89-2+deb9u7                armhf                        lightweight Exim MTA (v4) daemon
ii  fake-hwclock                                   0.11+rpt1                    all                          Save/restore system clock on machines without working RTC hardware
ii  fakeroot                                       1.21-3.1                     armhf                        tool for simulating superuser privileges
ii  fbset                                          2.1-29                       armhf                        framebuffer device maintenance program
ii  file                                           1:5.30-1+deb9u3              armhf                        Recognize the type of data in a file using "magic" numbers
ii  findutils                                      4.6.0+git+20161106-2         armhf                        utilities for finding files--find, xargs
ii  firmware-atheros                               1:20161130-3+rpt4            all                          Binary firmware for Atheros wireless cards
ii  firmware-brcm80211                             1:20161130-3+rpt4            all                          Binary firmware for Broadcom 802.11 wireless cards
ii  firmware-libertas                              1:20161130-3+rpt4            all                          Binary firmware for Marvell wireless cards
ii  firmware-misc-nonfree                          1:20161130-3+rpt4            all                          Binary firmware for various drivers in the Linux kernel
ii  firmware-realtek                               1:20161130-3+rpt4            all                          Binary firmware for Realtek wired/wifi/BT adapters
ii  fontconfig                                     2.11.0-6.7                   armhf                        generic font configuration library - support binaries
ii  fontconfig-config                              2.11.0-6.7                   all                          generic font configuration library - configuration
ii  fonts-dejavu-core                              2.37-1                       all                          Vera font family derivate with additional characters
ii  fonts-freefont-ttf                             20120503-6                   all                          Freefont Serif, Sans and Mono Truetype fonts
ii  g++                                            4:6.3.0-4                    armhf                        GNU C++ compiler
ii  g++-6                                          6.3.0-18+rpi1+deb9u1         armhf                        GNU C++ compiler
ii  gcc                                            4:6.3.0-4                    armhf                        GNU C compiler
ii  gcc-4.6-base:armhf                             4.6.4-5+rpi1                 armhf                        GCC, the GNU Compiler Collection (base package)
ii  gcc-4.7-base:armhf                             4.7.3-11+rpi1                armhf                        GCC, the GNU Compiler Collection (base package)
ii  gcc-4.8-base:armhf                             4.8.5-4                      armhf                        GCC, the GNU Compiler Collection (base package)
ii  gcc-4.9-base:armhf                             4.9.3-14                     armhf                        GCC, the GNU Compiler Collection (base package)
ii  gcc-5-base:armhf                               5.4.1-4                      armhf                        GCC, the GNU Compiler Collection (base package)
ii  gcc-6                                          6.3.0-18+rpi1+deb9u1         armhf                        GNU C compiler
ii  gcc-6-base:armhf                               6.3.0-18+rpi1+deb9u1         armhf                        GCC, the GNU Compiler Collection (base package)
ii  gdb                                            7.12-6                       armhf                        GNU Debugger
ii  geoip-database                                 20170512-1                   all                          IP lookup command line tools that use the GeoIP library (country database)
ii  gettext-base                                   0.19.8.1-2+deb9u1            armhf                        GNU Internationalization utilities for the base system
ii  gir1.2-glib-2.0:armhf                          1.50.0-1                     armhf                        Introspection data for GLib, GObject, Gio and GModule
ii  gir1.2-gst-plugins-base-1.0                    1.10.4-1+deb9u1              armhf                        GObject introspection data for the GStreamer Plugins Base library
ii  gir1.2-gstreamer-1.0                           1.10.4-1                     armhf                        GObject introspection data for the GStreamer library
ii  glib-networking:armhf                          2.50.0-1+deb9u1              armhf                        network-related giomodules for GLib
ii  glib-networking-common                         2.50.0-1+deb9u1              all                          network-related giomodules for GLib - data files
ii  glib-networking-services                       2.50.0-1+deb9u1              armhf                        network-related giomodules for GLib - D-Bus services
ii  gnupg                                          2.1.18-8~deb9u4              armhf                        GNU privacy guard - a free PGP replacement
ii  gnupg-agent                                    2.1.18-8~deb9u4              armhf                        GNU privacy guard - cryptographic agent
ii  gpgv                                           2.1.18-8~deb9u4              armhf                        GNU privacy guard - signature verification tool
ii  grep                                           2.27-2                       armhf                        GNU grep, egrep and fgrep
ii  groff-base                                     1.22.3-9                     armhf                        GNU troff text-formatting system (base system components)
ii  gsettings-desktop-schemas                      3.22.0-1                     all                          GSettings desktop-wide schemas
ii  gstreamer1.0-plugins-base:armhf                1.10.4-1+deb9u1              armhf                        GStreamer plugins from the "base" set
ii  gtk-update-icon-cache                          3.22.11-1+rpi3               armhf                        icon theme caching utility
ii  guile-2.0-libs:armhf                           2.0.13+1-4                   armhf                        Core Guile libraries
ii  gyp                                            0.1+20150913git1f374df9-1    all                          Cross-platform build script generator
ii  gzip                                           1.6-5                        armhf                        GNU compression utilities
ii  hardlink                                       0.3.0                        armhf                        Hardlinks multiple copies of the same file
ii  hicolor-icon-theme                             0.15-1                       all                          default fallback theme for FreeDesktop.org icon themes
ii  hostname                                       3.18                         armhf                        utility to set/show the host name or domain name
ii  htop                                           2.0.2-1                      armhf                        interactive processes viewer
ii  i2c-tools                                      3.1.2-3                      armhf                        heterogeneous set of I2C tools for Linux
ii  ifupdown                                       0.8.19                       armhf                        high level tools to configure network interfaces
ii  incron                                         0.5.10-3                     armhf                        cron-like daemon which handles filesystem events
ii  info                                           6.3.0.dfsg.1-1+b1            armhf                        Standalone GNU Info documentation browser
ii  init                                           1.48                         armhf                        metapackage ensuring an init system is installed
ii  init-system-helpers                            1.48                         all                          helper tools for all init systems
ii  initramfs-tools                                0.130                        all                          generic modular initramfs generator (automation)
ii  initramfs-tools-core                           0.130                        all                          generic modular initramfs generator (core tools)
ii  inotify-tools                                  3.14-2                       armhf                        command-line programs providing a simple interface to inotify
ii  install-info                                   6.3.0.dfsg.1-1+b1            armhf                        Manage installed documentation in info format
ii  iproute2                                       4.9.0-1+deb9u1               armhf                        networking and traffic control tools
ii  iptables                                       1.6.0+snapshot20161117-6     armhf                        administration tools for packet filtering and NAT
ii  iputils-ping                                   3:20161105-1                 armhf                        Tools to test the reachability of network hosts
ii  isc-dhcp-client                                4.3.5-3+deb9u1               armhf                        DHCP client for automatically obtaining an IP address
ii  isc-dhcp-common                                4.3.5-3+deb9u1               armhf                        common manpages relevant to all of the isc-dhcp packages
ii  iso-codes                                      3.75-1                       all                          ISO language, territory, currency, script codes and their translations
ii  iw                                             4.9-0.1                      armhf                        tool for configuring Linux wireless devices
ii  javascript-common                              11                           all                          Base support for JavaScript library packages
ii  kbd                                            2.0.3-2                      armhf                        Linux console font and keytable utilities
ii  keyboard-configuration                         1.164                        all                          system-wide keyboard preferences
ii  keyutils                                       1.5.9-9                      armhf                        Linux Key Management Utilities
ii  klibc-utils                                    2.0.4-9+rpi1                 armhf                        small utilities built with klibc for early boot
ii  kmod                                           23-2                         armhf                        tools for managing Linux kernel modules
ii  less                                           481-2.1                      armhf                        pager program similar to more
ii  liba52-0.7.4:armhf                             0.7.4-19                     armhf                        library for decoding ATSC A/52 streams
ii  libaa1:armhf                                   1.4p5-44                     armhf                        ASCII art library
ii  libaacs0:armhf                                 0.8.1-2                      armhf                        free-and-libre implementation of AACS
ii  libacl1:armhf                                  2.2.52-3                     armhf                        Access control list shared library
ii  libalgorithm-diff-perl                         1.19.03-1                    all                          module to find differences between files
ii  libalgorithm-diff-xs-perl                      0.04-4+b2                    armhf                        module to find differences between files (XS accelerated)
ii  libalgorithm-merge-perl                        0.08-3                       all                          Perl module for three-way merge of textual data
ii  libao-common                                   1.2.2-1                      armhf                        Cross Platform Audio Output Library (Common files)
ii  libao4                                         1.2.2-1                      armhf                        Cross Platform Audio Output Library
ii  libapparmor1:armhf                             2.11.0-3+deb9u2              armhf                        changehat AppArmor library
ii  libapt-inst2.0:armhf                           1.4.11                       armhf                        deb package format runtime library
ii  libapt-pkg5.0:armhf                            1.4.11                       armhf                        package management runtime library
ii  libarchive13:armhf                             3.2.2-2+deb9u3               armhf                        Multi-format archive and compression library (shared library)
ii  libasan3:armhf                                 6.3.0-18+rpi1+deb9u1         armhf                        AddressSanitizer -- a fast memory error detector
ii  libasound2:armhf                               1.1.3-5+rpt4                 armhf                        shared library for ALSA applications
ii  libasound2-data                                1.1.3-5+rpt4                 all                          Configuration files and profiles for ALSA drivers
ii  libass5:armhf                                  1:0.13.4-2                   armhf                        library for SSA/ASS subtitles rendering
ii  libassuan0:armhf                               2.4.3-2                      armhf                        IPC library for the GnuPG components
ii  libasyncns0:armhf                              0.8-6                        armhf                        Asynchronous name service query library
ii  libatk-bridge2.0-0:armhf                       2.22.0-2                     armhf                        AT-SPI 2 toolkit bridge - shared library
ii  libatk1.0-0:armhf                              2.22.0-1                     armhf                        ATK accessibility toolkit
ii  libatk1.0-data                                 2.22.0-1                     all                          Common files for the ATK accessibility toolkit
ii  libatomic1:armhf                               6.3.0-18+rpi1+deb9u1         armhf                        support library providing __atomic built-in functions
ii  libatspi2.0-0:armhf                            2.22.0-6+deb9u1              armhf                        Assistive Technology Service Provider Interface - shared library
ii  libattr1:armhf                                 1:2.4.47-2                   armhf                        Extended attribute shared library
ii  libaudio2:armhf                                1.9.4-5                      armhf                        Network Audio System - shared libraries
ii  libaudit-common                                1:2.6.7-2                    all                          Dynamic library for security auditing - common files
ii  libaudit1:armhf                                1:2.6.7-2                    armhf                        Dynamic library for security auditing
ii  libauthen-sasl-perl                            2.1600-1                     all                          Authen::SASL - SASL Authentication framework
ii  libavahi-client3:armhf                         0.6.32-2                     armhf                        Avahi client library
ii  libavahi-common-data:armhf                     0.6.32-2                     armhf                        Avahi common data files
ii  libavahi-common3:armhf                         0.6.32-2                     armhf                        Avahi common library
ii  libavahi-core7:armhf                           0.6.32-2                     armhf                        Avahi's embeddable mDNS/DNS-SD library
ii  libavc1394-0:armhf                             0.5.4-4                      armhf                        control IEEE 1394 audio/video devices
ii  libavcodec57:armhf                             7:3.2.18-0+deb9u1            armhf                        FFmpeg library with de/encoders for audio/video codecs - runtime files
ii  libavformat57:armhf                            7:3.2.18-0+deb9u1            armhf                        FFmpeg library with (de)muxers for multimedia containers - runtime files
ii  libavutil55:armhf                              7:3.2.18-0+deb9u1            armhf                        FFmpeg library with functions for simplifying programming - runtime files
ii  libbabeltrace-ctf1:armhf                       1.5.1-1                      armhf                        Common Trace Format (CTF) library
ii  libbabeltrace1:armhf                           1.5.1-1                      armhf                        Babeltrace conversion libraries
ii  libbasicusageenvironment1:armhf                2016.11.28-1+deb9u2          armhf                        multimedia RTSP streaming library (BasicUsageEnvironment class)
ii  libbdplus0:armhf                               0.1.2-2                      armhf                        implementation of BD+ for reading Blu-ray Discs
ii  libbind9-140:armhf                             1:9.10.3.dfsg.P4-12.3+deb9u7 armhf                        BIND9 Shared Library used by BIND
ii  libblkid1:armhf                                2.29.2-1+deb9u1              armhf                        block device ID library
ii  libbluetooth3:armhf                            5.43-2+rpt2+deb9u2           armhf                        Library to use the BlueZ Linux Bluetooth stack
ii  libbluray1:armhf                               1:0.9.3-4                    armhf                        Blu-ray disc playback support library (shared library)
ii  libbluray2:armhf                               1:1.0.2-1                    armhf                        Blu-ray disc playback support library (shared library)
ii  libboost-filesystem1.62.0:armhf                1.62.0+dfsg-4                armhf                        filesystem operations (portable paths, iteration over directories, etc) in C++
ii  libboost-iostreams1.58.0:armhf                 1.58.0+dfsg-5.1+rpi1+b1      armhf                        Boost.Iostreams Library
ii  libboost-iostreams1.60.0:armhf                 1.60.0+dfsg-6+b2             armhf                        Boost.Iostreams Library
ii  libboost-iostreams1.62.0:armhf                 1.62.0+dfsg-4                armhf                        Boost.Iostreams Library
ii  libboost-system1.62.0:armhf                    1.62.0+dfsg-4                armhf                        Operating system (e.g. diagnostics support) library
ii  libbs2b0:armhf                                 3.1.0+dfsg-2.2               armhf                        Bauer stereophonic-to-binaural DSP library
ii  libbsd0:armhf                                  0.8.3-1                      armhf                        utility functions from BSD systems - shared library
ii  libbz2-1.0:armhf                               1.0.6-8.1                    armhf                        high-quality block-sorting file compressor library - runtime
ii  libc-ares2:armhf                               1.14.0-1~bpo9+1              armhf                        asynchronous name resolver
ii  libc-bin                                       2.24-11+deb9u4               armhf                        GNU C Library: Binaries
ii  libc-dev-bin                                   2.24-11+deb9u4               armhf                        GNU C Library: Development binaries
ii  libc-l10n                                      2.24-11+deb9u4               all                          GNU C Library: localization files
ii  libc6:armhf                                    2.24-11+deb9u4               armhf                        GNU C Library: Shared libraries
ii  libc6-dbg:armhf                                2.24-11+deb9u4               armhf                        GNU C Library: detached debugging symbols
ii  libc6-dev:armhf                                2.24-11+deb9u4               armhf                        GNU C Library: Development Libraries and Header Files
ii  libcaca0:armhf                                 0.99.beta19-2.1~deb9u1       armhf                        colour ASCII art library
ii  libcairo-gobject2:armhf                        1.14.8-1+rpi1                armhf                        Cairo 2D vector graphics library (GObject library)
ii  libcairo2:armhf                                1.14.8-1+rpi1                armhf                        Cairo 2D vector graphics library
ii  libcap-ng0:armhf                               0.7.7-3                      armhf                        An alternate POSIX capabilities library
ii  libcap2:armhf                                  1:2.25-1                     armhf                        POSIX 1003.1e capabilities (library)
ii  libcap2-bin                                    1:2.25-1                     armhf                        POSIX 1003.1e capabilities (utilities)
ii  libcc1-0:armhf                                 6.3.0-18+rpi1+deb9u1         armhf                        GCC cc1 plugin for GDB
ii  libcddb2                                       1.3.2-5                      armhf                        library to access CDDB data - runtime files
ii  libcdio-cdda1:armhf                            0.83-4.3                     armhf                        library to read and control digital audio CDs
ii  libcdio-paranoia1:armhf                        0.83-4.3                     armhf                        library to read digital audio CDs with error correction
ii  libcdio13:armhf                                0.83-4.3                     armhf                        library to read and control CD-ROM
ii  libcdparanoia0:armhf                           3.10.2+debian-11             armhf                        audio extraction tool for sampling CDs (library)
ii  libchromaprint1:armhf                          1.4.2-1                      armhf                        audio fingerprint library
ii  libcolord2:armhf                               1.3.3-2                      armhf                        system service to manage device colour profiles -- runtime
ii  libcomerr2:armhf                               1.43.4-2+deb9u2              armhf                        common error description library
ii  libcroco3:armhf                                0.6.11-3                     armhf                        Cascading Style Sheet (CSS) parsing and manipulation toolkit
ii  libcryptsetup4:armhf                           2:1.7.3-4                    armhf                        disk encryption support - shared library
ii  libcups2:armhf                                 2.2.1-8+deb9u6               armhf                        Common UNIX Printing System(tm) - Core library
ii  libcurl3:armhf                                 7.52.1-5+deb9u13             armhf                        easy-to-use client-side URL transfer library (OpenSSL flavour)
ii  libcurl3-gnutls:armhf                          7.52.1-5+deb9u13             armhf                        easy-to-use client-side URL transfer library (GnuTLS flavour)
ii  libcwidget3v5:armhf                            0.5.17-4                     armhf                        high-level terminal interface library for C++ (runtime files)
ii  libdaemon0:armhf                               0.14-6                       armhf                        lightweight C library for daemons - runtime library
ii  libdatrie1:armhf                               0.2.10-4                     armhf                        Double-array trie library
ii  libdb5.3:armhf                                 5.3.28-12+deb9u1             armhf                        Berkeley v5.3 Database Libraries [runtime]
ii  libdbus-1-3:armhf                              1.10.32-0+deb9u1             armhf                        simple interprocess messaging system (library)
ii  libdbus-glib-1-2:armhf                         0.108-2                      armhf                        simple interprocess messaging system (GLib-based shared library)
ii  libdc1394-22:armhf                             2.2.5-1                      armhf                        high level programming interface for IEEE 1394 digital cameras
ii  libdca0:armhf                                  0.0.5-10                     armhf                        decoding library for DTS Coherent Acoustics streams
ii  libdconf1:armhf                                0.26.0-2                     armhf                        simple configuration storage system - runtime library
ii  libdebconfclient0:armhf                        0.227                        armhf                        Debian Configuration Management System (C-implementation library)
ii  libdevmapper1.02.1:armhf                       2:1.02.137-2                 armhf                        Linux Kernel Device Mapper userspace library
ii  libdirectfb-1.2-9:armhf                        1.2.10.0-8+deb9u1            armhf                        direct frame buffer graphics (shared libraries)
ii  libdns-export162                               1:9.10.3.dfsg.P4-12.3+deb9u7 armhf                        Exported DNS Shared Library
ii  libdns162:armhf                                1:9.10.3.dfsg.P4-12.3+deb9u7 armhf                        DNS Shared Library used by BIND
ii  libdouble-conversion1:armhf                    2.0.1-4                      armhf                        routines to convert IEEE floats to and from strings
ii  libdpkg-perl                                   1.18.25                      all                          Dpkg perl modules
ii  libdrm-amdgpu1:armhf                           2.4.74-1                     armhf                        Userspace interface to amdgpu-specific kernel DRM services -- runtime
ii  libdrm-freedreno1:armhf                        2.4.74-1                     armhf                        Userspace interface to msm/kgsl kernel DRM services -- runtime
ii  libdrm-nouveau2:armhf                          2.4.74-1                     armhf                        Userspace interface to nouveau-specific kernel DRM services -- runtime
ii  libdrm-radeon1:armhf                           2.4.74-1                     armhf                        Userspace interface to radeon-specific kernel DRM services -- runtime
ii  libdrm2:armhf                                  2.4.74-1                     armhf                        Userspace interface to kernel DRM services -- runtime
ii  libdv4:armhf                                   1.0.0-11                     armhf                        software library for DV format digital video (runtime lib)
ii  libdvbpsi10:armhf                              1.3.0-5                      armhf                        library for MPEG TS and DVB PSI tables decoding and generating
ii  libdvdnav4:armhf                               5.0.3-3                      armhf                        DVD navigation library
ii  libdvdread4:armhf                              5.0.3-2                      armhf                        library for reading DVDs
ii  libdw1:armhf                                   0.168-1                      armhf                        library that provides access to the DWARF debug information
ii  libebml4v5:armhf                               1.3.4-1+deb9u2               armhf                        access library for the EBML format (shared library)
ii  libedit2:armhf                                 3.1-20160903-3               armhf                        BSD editline and history libraries
ii  libegl1-mesa:armhf                             13.0.6-1+rpi2                armhf                        free implementation of the EGL API -- runtime
ii  libelf1:armhf                                  0.168-1                      armhf                        library to read and write ELF files
ii  libenca0:armhf                                 1.19-1                       armhf                        Extremely Naive Charset Analyser - shared library files
ii  libencode-locale-perl                          1.05-1                       all                          utility to determine the locale encoding
ii  libepoxy0:armhf                                1.3.1-2                      armhf                        OpenGL function pointer management library
ii  libestr0                                       0.1.10-2                     armhf                        Helper functions for handling strings (lib)
ii  libevdev2:armhf                                1.5.6+dfsg-1                 armhf                        wrapper library for evdev devices
ii  libevent-2.0-5:armhf                           2.0.21-stable-3              armhf                        Asynchronous event notification library
ii  libexpat1:armhf                                2.2.0-2+deb9u3               armhf                        XML parsing C library - runtime library
ii  libexpat1-dev:armhf                            2.2.0-2+deb9u3               armhf                        XML parsing C library - development kit
ii  libfaad2:armhf                                 2.8.0~cvs20161113-1+deb9u2   armhf                        freeware Advanced Audio Decoder - runtime files
ii  libfakeroot:armhf                              1.21-3.1                     armhf                        tool for simulating superuser privileges - shared libraries
ii  libfastjson4:armhf                             0.99.4-1                     armhf                        fast json library for C
ii  libfdisk1:armhf                                2.29.2-1+deb9u1              armhf                        fdisk partitioning library
ii  libffi-dev:armhf                               3.2.1-6                      armhf                        Foreign Function Interface library (development files)
ii  libffi6:armhf                                  3.2.1-6                      armhf                        Foreign Function Interface library runtime
ii  libfftw3-single3:armhf                         3.3.5-3                      armhf                        Library for computing Fast Fourier Transforms - Single precision
ii  libfile-basedir-perl                           0.07-1                       all                          Perl module to use the freedesktop basedir specification
ii  libfile-desktopentry-perl                      0.22-1                       all                          Perl module to handle freedesktop .desktop files
ii  libfile-fcntllock-perl                         0.22-3+b2                    armhf                        Perl module for file locking with fcntl(2)
ii  libfile-listing-perl                           6.04-1                       all                          module to parse directory listings
ii  libfile-mimeinfo-perl                          0.27-1                       all                          Perl module to determine file types
ii  libflac8:armhf                                 1.3.2-1                      armhf                        Free Lossless Audio Codec - runtime C library
ii  libfont-afm-perl                               1.20-2                       all                          Font::AFM - Interface to Adobe Font Metrics files
ii  libfontconfig1:armhf                           2.11.0-6.7                   armhf                        generic font configuration library - runtime
ii  libfontenc1:armhf                              1:1.1.3-1                    armhf                        X11 font encoding library
ii  libfreetype6:armhf                             2.6.3-3.2+deb9u2             armhf                        FreeType 2 font engine, shared library files
ii  libfreetype6-dev                               2.6.3-3.2+deb9u2             armhf                        FreeType 2 font engine, development files
ii  libfribidi0:armhf                              0.19.7-1+deb9u1              armhf                        Free Implementation of the Unicode BiDi algorithm
ii  libftdi1-2:armhf                               1.3-2                        armhf                        Library to control and program the FTDI USB controllers
ii  libgbm1:armhf                                  13.0.6-1+rpi2                armhf                        generic buffer management API -- runtime
ii  libgc1c2:armhf                                 1:7.4.2-8                    armhf                        conservative garbage collector for C and C++
ii  libgcc-6-dev:armhf                             6.3.0-18+rpi1+deb9u1         armhf                        GCC support library (development files)
ii  libgcc1:armhf                                  1:6.3.0-18+rpi1+deb9u1       armhf                        GCC support library
ii  libgcrypt20:armhf                              1.7.6-2+deb9u3               armhf                        LGPL Crypto library - runtime library
ii  libgdbm3:armhf                                 1.8.3-14                     armhf                        GNU dbm database routines (runtime version)
ii  libgdk-pixbuf2.0-0:armhf                       2.36.5-2+deb9u2              armhf                        GDK Pixbuf library
ii  libgdk-pixbuf2.0-common                        2.36.5-2+deb9u2              all                          GDK Pixbuf library - data files
ii  libgeoip1:armhf                                1.6.9-4                      armhf                        non-DNS IP-to-country resolver library
ii  libgif7:armhf                                  5.1.4-0.4                    armhf                        library for GIF images (library)
ii  libgirepository-1.0-1:armhf                    1.50.0-1                     armhf                        Library for handling GObject introspection data (runtime library)
ii  libgl1-mesa-dri:armhf                          13.0.6-1+rpi2                armhf                        free implementation of the OpenGL API -- DRI modules
ii  libgl1-mesa-glx:armhf                          13.0.6-1+rpi2                armhf                        free implementation of the OpenGL API -- GLX runtime
ii  libglapi-mesa:armhf                            13.0.6-1+rpi2                armhf                        free implementation of the GL API -- shared library
ii  libgles2-mesa:armhf                            13.0.6-1+rpi2                armhf                        free implementation of the OpenGL|ES 2.x API -- runtime
ii  libglew2.0:armhf                               2.0.0-3                      armhf                        OpenGL Extension Wrangler - runtime environment
ii  libglib2.0-0:armhf                             2.50.3-2+deb9u2              armhf                        GLib library of C routines
ii  libglib2.0-data                                2.50.3-2+deb9u2              all                          Common files for GLib library
ii  libglu1-mesa:armhf                             9.0.0-2.1                    armhf                        Mesa OpenGL utility library (GLU)
ii  libgme0:armhf                                  0.6.0-4                      armhf                        Playback library for video game music files - shared library
ii  libgmp10:armhf                                 2:6.1.2+dfsg-1               armhf                        Multiprecision arithmetic library
ii  libgnutls30:armhf                              3.5.8-5+deb9u5               armhf                        GNU TLS library - main runtime library
ii  libgomp1:armhf                                 6.3.0-18+rpi1+deb9u1         armhf                        GCC OpenMP (GOMP) support library
ii  libgpg-error0:armhf                            1.26-2                       armhf                        library for common error values and messages in GnuPG components
ii  libgpm2:armhf                                  1.20.4-6.2                   armhf                        General Purpose Mouse - shared library
ii  libgraphite2-3:armhf                           1.3.10-1                     armhf                        Font rendering engine for Complex Scripts -- library
ii  libgroupsock8:armhf                            2016.11.28-1+deb9u2          armhf                        multimedia RTSP streaming library (network interfaces and sockets)
ii  libgsasl7                                      1.8.0-8+b1                   armhf                        GNU SASL library
ii  libgsm1:armhf                                  1.0.13-4                     armhf                        Shared libraries for GSM speech compressor
ii  libgssapi-krb5-2:armhf                         1.15-1+deb9u2                armhf                        MIT Kerberos runtime libraries - krb5 GSS-API Mechanism
ii  libgstreamer-plugins-base1.0-0:armhf           1.10.4-1+deb9u1              armhf                        GStreamer libraries from the "base" set
ii  libgstreamer1.0-0:armhf                        1.10.4-1                     armhf                        Core GStreamer libraries and elements
ii  libgtk-3-0:armhf                               3.22.11-1+rpi3               armhf                        GTK+ graphical user interface library
ii  libgtk-3-bin                                   3.22.11-1+rpi3               armhf                        programs for the GTK+ graphical user interface library
ii  libgtk-3-common                                3.22.11-1+rpi3               all                          common files for the GTK+ graphical user interface library
ii  libgudev-1.0-0:armhf                           230-3                        armhf                        GObject-based wrapper library for libudev
ii  libharfbuzz0b:armhf                            1.4.2-1                      armhf                        OpenType text shaping engine (shared library)
ii  libhogweed4:armhf                              3.3-1                        armhf                        low level cryptographic library (public-key cryptos)
ii  libhtml-form-perl                              6.03-1                       all                          module that represents an HTML form element
ii  libhtml-format-perl                            2.12-1                       all                          module for transforming HTML into various formats
ii  libhtml-parser-perl                            3.72-3                       armhf                        collection of modules that parse HTML text documents
ii  libhtml-tagset-perl                            3.20-3                       all                          Data tables pertaining to HTML
ii  libhtml-tree-perl                              5.03-2                       all                          Perl module to represent and create HTML syntax trees
ii  libhttp-cookies-perl                           6.01-1                       all                          HTTP cookie jars
ii  libhttp-daemon-perl                            6.01-1                       all                          simple http server class
ii  libhttp-date-perl                              6.02-1                       all                          module of date conversion routines
ii  libhttp-message-perl                           6.11-1                       all                          perl interface to HTTP style messages
ii  libhttp-negotiate-perl                         6.00-2                       all                          implementation of content negotiation
ii  libhttp-parser2.8:armhf                        2.8.1-1~bpo9+1               armhf                        parser for HTTP messages written in C
ii  libice6:armhf                                  2:1.0.9-2                    armhf                        X11 Inter-Client Exchange library
ii  libicu57:armhf                                 57.1-6+deb9u4                armhf                        International Components for Unicode
ii  libid3tag0:armhf                               0.15.1b-12                   armhf                        ID3 tag reading library from the MAD project
ii  libident                                       0.22-3.1                     armhf                        simple RFC1413 client library - runtime
ii  libidn11:armhf                                 1.33-1+deb9u1                armhf                        GNU Libidn library, implementation of IETF IDN specifications
ii  libidn2-0:armhf                                0.16-1+deb9u1                armhf                        Internationalized domain names (IDNA2008) library
ii  libinotifytools0                               3.14-2                       armhf                        utility wrapper around inotify
ii  libinput-bin                                   1.6.3-1                      armhf                        input device management and event handling library - udev quirks
ii  libinput10:armhf                               1.6.3-1                      armhf                        input device management and event handling library - shared library
ii  libio-html-perl                                1.001-1                      all                          open an HTML file with automatic charset detection
ii  libio-socket-ssl-perl                          2.044-1                      all                          Perl module implementing object oriented interface to SSL sockets
ii  libip4tc0:armhf                                1.6.0+snapshot20161117-6     armhf                        netfilter libip4tc library
ii  libip6tc0:armhf                                1.6.0+snapshot20161117-6     armhf                        netfilter libip6tc library
ii  libipc-system-simple-perl                      1.25-3                       all                          Perl module to run commands simply, with detailed diagnostics
ii  libiptc0:armhf                                 1.6.0+snapshot20161117-6     armhf                        netfilter libiptc library
ii  libisc-export160                               1:9.10.3.dfsg.P4-12.3+deb9u7 armhf                        Exported ISC Shared Library
ii  libisc160:armhf                                1:9.10.3.dfsg.P4-12.3+deb9u7 armhf                        ISC Shared Library used by BIND
ii  libisccc140:armhf                              1:9.10.3.dfsg.P4-12.3+deb9u7 armhf                        Command Channel Library used by BIND
ii  libisccfg140:armhf                             1:9.10.3.dfsg.P4-12.3+deb9u7 armhf                        Config File Handling Library used by BIND
ii  libisl15:armhf                                 0.18-1                       armhf                        manipulating sets and relations of integer points bounded by linear constraints
ii  libiw30:armhf                                  30~pre9-12                   armhf                        Wireless tools - library
ii  libjack-jackd2-0:armhf                         1.9.10+20150825git1ed50c92~d armhf                        JACK Audio Connection Kit (libraries)
ii  libjbig0:armhf                                 2.1-3.1                      armhf                        JBIGkit libraries
ii  libjim0.76:armhf                               0.76-2                       armhf                        small-footprint implementation of Tcl - shared library
ii  libjpeg-dev                                    1:1.5.1-2+deb9u1             all                          Development files for the JPEG library [dummy package]
ii  libjpeg62-turbo:armhf                          1:1.5.1-2+deb9u1             armhf                        libjpeg-turbo JPEG runtime library
ii  libjpeg62-turbo-dev:armhf                      1:1.5.1-2+deb9u1             armhf                        Development files for the libjpeg-turbo JPEG library
ii  libjs-inherits                                 2.0.3-1                      all                          Exposes inherits function from Node.js environment
ii  libjs-jquery                                   3.1.1-2+deb9u1               all                          JavaScript library for dynamic web applications
ii  libjs-node-uuid                                1.4.0-1                      all                          simple, fast generation of RFC4122 UUIDs - JavaScript library
ii  libjs-sphinxdoc                                1.4.9-2                      all                          JavaScript support for Sphinx documentation
ii  libjs-underscore                               1.8.3~dfsg-1                 all                          JavaScript's functional programming helper library
ii  libjson-glib-1.0-0:armhf                       1.2.6-1                      armhf                        GLib JSON manipulation library
ii  libjson-glib-1.0-common                        1.2.6-1                      all                          GLib JSON manipulation library (common files)
ii  libk5crypto3:armhf                             1.15-1+deb9u2                armhf                        MIT Kerberos runtime libraries - Crypto Library
ii  libkate1:armhf                                 0.4.1-7+b1                   armhf                        Codec for karaoke and text encapsulation
ii  libkeyutils1:armhf                             1.5.9-9                      armhf                        Linux Key Management Utilities (library)
ii  libklibc                                       2.0.4-9+rpi1                 armhf                        minimal libc subset for use with initramfs
ii  libkmod2:armhf                                 23-2                         armhf                        libkmod shared library
ii  libkrb5-3:armhf                                1.15-1+deb9u2                armhf                        MIT Kerberos runtime libraries
ii  libkrb5support0:armhf                          1.15-1+deb9u2                armhf                        MIT Kerberos runtime libraries - Support library
ii  libksba8:armhf                                 1.3.5-2                      armhf                        X.509 and CMS support library
ii  libkyotocabinet16v5:armhf                      1.2.76-4.2+rpi1              armhf                        Straightforward implementation of DBM - shared library
ii  liblcms2-2:armhf                               2.8-4+deb9u1                 armhf                        Little CMS 2 color management library
ii  libldap-2.4-2:armhf                            2.4.44+dfsg-5+deb9u4         armhf                        OpenLDAP libraries
ii  libldap-common                                 2.4.44+dfsg-5+deb9u4         all                          OpenLDAP common files for libraries
ii  libldb1:armhf                                  2:1.1.27-1+deb9u1            armhf                        LDAP-like embedded database - shared library
ii  liblirc-client0:armhf                          0.9.4c-9                     armhf                        infra-red remote control support - client library
ii  liblirc0:armhf                                 0.9.4c-9                     armhf                        Infra-red remote control support - Run-time libraries
ii  liblivemedia57:armhf                           2016.11.28-1+deb9u2          armhf                        multimedia RTSP streaming library
ii  libllvm3.9:armhf                               1:3.9.1-9+rpi1               armhf                        Modular compiler and toolchain technologies, runtime library
ii  liblocale-gettext-perl                         1.07-3+b1                    armhf                        module using libc functions for internationalization in Perl
ii  liblogging-stdlog0:armhf                       1.0.5-2                      armhf                        easy to use and lightweight logging library
ii  liblognorm5:armhf                              2.0.1-1.1                    armhf                        log normalizing library
ii  libltdl7:armhf                                 2.4.6-2                      armhf                        System independent dlopen wrapper for GNU libtool
ii  liblua5.2-0:armhf                              5.2.4-1.1                    armhf                        Shared library for the Lua interpreter version 5.2
ii  libluajit-5.1-common                           2.0.4+dfsg-1+deb9u1          all                          Just in time compiler for Lua - common files
ii  liblwp-mediatypes-perl                         6.02-1                       all                          module to guess media type for a file or a URL
ii  liblwp-protocol-https-perl                     6.06-2                       all                          HTTPS driver for LWP::UserAgent
ii  liblwres141:armhf                              1:9.10.3.dfsg.P4-12.3+deb9u7 armhf                        Lightweight Resolver Library used by BIND
ii  liblz4-1:armhf                                 0.0~r131-2                   armhf                        Fast LZ compression algorithm library - runtime
ii  liblzma5:armhf                                 5.2.2-1.2                    armhf                        XZ-format compression library
ii  liblzo2-2:armhf                                2.08-1.2                     armhf                        data compression library
ii  libmad0:armhf                                  0.15.1b-8+deb9u1             armhf                        MPEG audio decoder library
ii  libmagic-mgc                                   1:5.30-1+deb9u3              armhf                        File type determination library using "magic" numbers (compiled magic file)
ii  libmagic1:armhf                                1:5.30-1+deb9u3              armhf                        Recognize the type of data in a file using "magic" numbers - library
ii  libmailtools-perl                              2.18-1                       all                          Manipulate email in perl programs
ii  libmailutils5:armhf                            1:3.1.1-1                    armhf                        GNU Mail abstraction library
ii  libmariadbclient18:armhf                       10.1.47-0+deb9u1             armhf                        MariaDB database client library
ii  libmatroska6v5:armhf                           1.4.5-2                      armhf                        extensible open standard audio/video container format (shared library)
ii  libmaxminddb0:armhf                            1.2.0-1+deb9u1               armhf                        IP geolocation database library
ii  libmnl-dev                                     1.0.4-2                      armhf                        minimalistic Netlink communication library (devel)
ii  libmnl0:armhf                                  1.0.4-2                      armhf                        minimalistic Netlink communication library
ii  libmount1:armhf                                2.29.2-1+deb9u1              armhf                        device mounting library
ii  libmp3lame0:armhf                              3.99.5+repack1-9             armhf                        MP3 encoding library
ii  libmpc3:armhf                                  1.0.3-1                      armhf                        multiple precision complex floating-point library
ii  libmpcdec6:armhf                               2:0.1~r495-1                 armhf                        MusePack decoder - library
ii  libmpdec2:armhf                                2.4.2-1                      armhf                        library for decimal floating point arithmetic (runtime library)
ii  libmpeg2-4:armhf                               0.5.1-7                      armhf                        MPEG1 and MPEG2 video decoder library
ii  libmpfr4:armhf                                 3.1.5-1                      armhf                        multiple precision floating-point computation
ii  libmpg123-0:armhf                              1.23.8-1                     armhf                        MPEG layer 1/2/3 audio decoder (shared library)
ii  libmtdev1:armhf                                1.1.5-1                      armhf                        Multitouch Protocol Translation Library - shared library
ii  libmtp-common                                  1.1.13-1                     all                          Media Transfer Protocol (MTP) common files
ii  libmtp-runtime                                 1.1.13-1                     armhf                        Media Transfer Protocol (MTP) runtime tools
ii  libmtp9:armhf                                  1.1.13-1                     armhf                        Media Transfer Protocol (MTP) library
ii  libncurses5:armhf                              6.0+20161126-1+deb9u2        armhf                        shared libraries for terminal handling
ii  libncursesw5:armhf                             6.0+20161126-1+deb9u2        armhf                        shared libraries for terminal handling (wide character support)
ii  libnet-dbus-perl                               1.1.0-4+b1                   armhf                        Perl extension for the DBus bindings
ii  libnet-http-perl                               6.12-1                       all                          module providing low-level HTTP connection client
ii  libnet-smtp-ssl-perl                           1.04-1                       all                          Perl module providing SSL support to Net::SMTP
ii  libnet-ssleay-perl                             1.80-1                       armhf                        Perl module for Secure Sockets Layer (SSL)
ii  libnet1:armhf                                  1.1.6+dfsg-3                 armhf                        library for the construction and handling of network packets
ii  libnetfilter-conntrack3:armhf                  1.0.6-2                      armhf                        Netfilter netlink-conntrack library
ii  libnettle6:armhf                               3.3-1                        armhf                        low level cryptographic library (symmetric and one-way cryptos)
ii  libnewt0.52:armhf                              0.52.19-1                    armhf                        Not Erik's Windowing Toolkit - text mode windowing with slang
ii  libnfnetlink0:armhf                            1.0.1-3                      armhf                        Netfilter netlink library
ii  libnfs8:armhf                                  1.11.0-2                     armhf                        NFS client library (shared library)
ii  libnfsidmap2:armhf                             0.25-5.1                     armhf                        NFS idmapping library
ii  libnghttp2-14:armhf                            1.18.1-1+deb9u1              armhf                        library implementing HTTP/2 protocol (shared library)
ii  libnih-dbus1                                   1.0.3-8                      armhf                        NIH D-Bus Bindings Library
ii  libnih1                                        1.0.3-8                      armhf                        NIH Utility Library
ii  libnl-3-200:armhf                              3.2.27-2                     armhf                        library for dealing with netlink sockets
ii  libnl-genl-3-200:armhf                         3.2.27-2                     armhf                        library for dealing with netlink sockets - generic netlink
ii  libnotify4:armhf                               0.7.7-2                      armhf                        sends desktop notifications to a notification daemon
ii  libnpth0:armhf                                 1.3-1                        armhf                        replacement for GNU Pth using system threads
ii  libnss-mdns:armhf                              0.10-8                       armhf                        NSS module for Multicast DNS name resolution
ii  libntlm0:armhf                                 1.4-8                        armhf                        NTLM authentication library
ii  libogg0:armhf                                  1.3.2-1                      armhf                        Ogg bitstream library
ii  libopenal-data                                 1:1.17.2-4                   all                          Software implementation of the OpenAL audio API (data files)
ii  libopenal1:armhf                               1:1.17.2-4                   armhf                        Software implementation of the OpenAL audio API (shared library)
ii  libopencore-amrnb0:armhf                       0.1.3-2.1                    armhf                        Adaptive Multi Rate speech codec - shared library
ii  libopencore-amrwb0:armhf                       0.1.3-2.1                    armhf                        Adaptive Multi-Rate - Wideband speech codec - shared library
ii  libopenjp2-7:armhf                             2.1.2-1.1+deb9u5             armhf                        JPEG 2000 image compression/decompression library
ii  libopenmpt-modplug1:armhf                      0.2.7386~beta20.3-3+deb9u4   armhf                        module music library based on OpenMPT -- modplug compat library
ii  libopenmpt0:armhf                              0.2.7386~beta20.3-3+deb9u4   armhf                        module music library based on OpenMPT -- shared library
ii  libopus0:armhf                                 1.2~alpha2-1                 armhf                        Opus codec runtime library
ii  liborc-0.4-0:armhf                             1:0.4.26-2                   armhf                        Library of Optimized Inner Loops Runtime Compiler
ii  libout123-0:armhf                              1.23.8-1                     armhf                        MPEG layer 1/2/3 audio decoder (libout123 shared library)
ii  libp11-kit0:armhf                              0.23.3-2                     armhf                        library for loading and coordinating access to PKCS#11 modules - runtime
ii  libpam-chksshpwd:armhf                         1.1.8-3.6+rpi1               armhf                        PAM module to enable SSH password checking support
ii  libpam-modules:armhf                           1.1.8-3.6+rpi1               armhf                        Pluggable Authentication Modules for PAM
ii  libpam-modules-bin                             1.1.8-3.6+rpi1               armhf                        Pluggable Authentication Modules for PAM - helper binaries
ii  libpam-runtime                                 1.1.8-3.6+rpi1               all                          Runtime support for the PAM library
ii  libpam-systemd:armhf                           232-25+deb9u12               armhf                        system and service manager - PAM module
ii  libpam0g:armhf                                 1.1.8-3.6+rpi1               armhf                        Pluggable Authentication Modules library
ii  libpango-1.0-0:armhf                           1.40.5-1                     armhf                        Layout and rendering of internationalized text
ii  libpangocairo-1.0-0:armhf                      1.40.5-1                     armhf                        Layout and rendering of internationalized text
ii  libpangoft2-1.0-0:armhf                        1.40.5-1                     armhf                        Layout and rendering of internationalized text
ii  libparted2:armhf                               3.2-17                       armhf                        disk partition manipulator - shared library
ii  libpcap0.8:armhf                               1.8.1-3                      armhf                        system interface for user-level packet capture
ii  libpcre16-3:armhf                              2:8.39-3                     armhf                        Old Perl 5 Compatible Regular Expression Library - 16 bit runtime files
ii  libpcre3:armhf                                 2:8.39-3                     armhf                        Old Perl 5 Compatible Regular Expression Library - runtime files
ii  libpcsclite1:armhf                             1.8.20-1                     armhf                        Middleware to access a smart card using PC/SC (library)
ii  libperl5.24:armhf                              5.24.1-3+deb9u7              armhf                        shared Perl library
ii  libpipeline1:armhf                             1.4.1-2                      armhf                        pipeline manipulation library
ii  libpixman-1-0:armhf                            0.34.0-1+rpi1                armhf                        pixel-manipulation library for X and cairo
ii  libplymouth4:armhf                             0.9.2-4+rpi1                 armhf                        graphical boot animation and logger - shared libraries
ii  libpng-dev:armhf                               1.6.28-1+deb9u1              armhf                        PNG library - development (version 1.6)
ii  libpng-tools                                   1.6.28-1+deb9u1              armhf                        PNG library - tools (version 1.6)
ii  libpng16-16:armhf                              1.6.28-1+deb9u1              armhf                        PNG library - runtime (version 1.6)
ii  libpolkit-agent-1-0:armhf                      0.105-18+deb9u1              armhf                        PolicyKit Authentication Agent API
ii  libpolkit-backend-1-0:armhf                    0.105-18+deb9u1              armhf                        PolicyKit backend API
ii  libpolkit-gobject-1-0:armhf                    0.105-18+deb9u1              armhf                        PolicyKit Authorization API
ii  libpopt0:armhf                                 1.16-10                      armhf                        lib for parsing cmdline parameters
ii  libportaudio2:armhf                            19.6.0-1                     armhf                        Portable audio I/O - shared library
ii  libpostproc54:armhf                            7:3.2.18-0+deb9u1            armhf                        FFmpeg library for post processing - runtime files
ii  libprocps6:armhf                               2:3.3.12-3+deb9u1            armhf                        library for accessing process information from /proc
ii  libprotobuf-lite10:armhf                       3.0.0-9                      armhf                        protocol buffers C++ library (lite version)
ii  libproxy-tools                                 0.4.14-2+deb9u2              armhf                        automatic proxy configuration management library (tools)
ii  libproxy1v5:armhf                              0.4.14-2+deb9u2              armhf                        automatic proxy configuration management library (shared)
ii  libpsl5:armhf                                  0.17.0-3                     armhf                        Library for Public Suffix List (shared libraries)
ii  libpulse0:armhf                                10.0-1+deb9u1                armhf                        PulseAudio client libraries
ii  libpython-all-dev:armhf                        2.7.13-2                     armhf                        package depending on all supported Python development packages
ii  libpython-dev:armhf                            2.7.13-2                     armhf                        header files and a static library for Python (default)
ii  libpython-stdlib:armhf                         2.7.13-2                     armhf                        interactive high-level object-oriented language (default python version)
ii  libpython2.7:armhf                             2.7.13-2+deb9u4              armhf                        Shared Python runtime library (version 2.7)
ii  libpython2.7-dev:armhf                         2.7.13-2+deb9u4              armhf                        Header files and a static library for Python (v2.7)
ii  libpython2.7-minimal:armhf                     2.7.13-2+deb9u4              armhf                        Minimal subset of the Python language (version 2.7)
ii  libpython2.7-stdlib:armhf                      2.7.13-2+deb9u4              armhf                        Interactive high-level object-oriented language (standard library, version 2.7)
ii  libpython3-dev:armhf                           3.5.3-1                      armhf                        header files and a static library for Python (default)
ii  libpython3-stdlib:armhf                        3.5.3-1                      armhf                        interactive high-level object-oriented language (default python3 version)
ii  libpython3.5:armhf                             3.5.3-1+deb9u5               armhf                        Shared Python runtime library (version 3.5)
ii  libpython3.5-dev:armhf                         3.5.3-1+deb9u5               armhf                        Header files and a static library for Python (v3.5)
ii  libpython3.5-minimal:armhf                     3.5.3-1+deb9u5               armhf                        Minimal subset of the Python language (version 3.5)
ii  libpython3.5-stdlib:armhf                      3.5.3-1+deb9u5               armhf                        Interactive high-level object-oriented language (standard library, version 3.5)
ii  libqt5core5a:armhf                             5.7.1+dfsg-3+rpi1+deb9u3     armhf                        Qt 5 core module
ii  libqt5dbus5:armhf                              5.7.1+dfsg-3+rpi1+deb9u3     armhf                        Qt 5 D-Bus module
ii  libqt5gui5:armhf                               5.7.1+dfsg-3+rpi1+deb9u3     armhf                        Qt 5 GUI module
ii  libqt5network5:armhf                           5.7.1+dfsg-3+rpi1+deb9u3     armhf                        Qt 5 network module
ii  libqt5svg5:armhf                               5.7.1~20161021-2.1+deb9u1    armhf                        Qt 5 SVG module
ii  libqt5widgets5:armhf                           5.7.1+dfsg-3+rpi1+deb9u3     armhf                        Qt 5 widgets module
ii  libqt5x11extras5:armhf                         5.7.1~20161021-2             armhf                        Qt 5 X11 extras
ii  libraspberrypi-bin                             1.20190819~stretch-1         armhf                        Miscellaneous Raspberry Pi utilities
ii  libraspberrypi-dev                             1.20190819~stretch-1         armhf                        EGL/GLES/OpenVG/etc. libraries for the Raspberry Pi's VideoCore IV (headers)
ii  libraspberrypi-doc                             1.20190819~stretch-1         armhf                        EGL/GLES/OpenVG/etc. libraries for the Raspberry Pi's VideoCore IV (headers)
ii  libraspberrypi0                                1.20190819~stretch-1         armhf                        EGL/GLES/OpenVG/etc. libraries for the Raspberry Pi's VideoCore IV
ii  libraw1394-11:armhf                            2.1.2-1                      armhf                        library for direct access to IEEE 1394 bus (aka FireWire)
ii  libreadline6:armhf                             6.3-9                        armhf                        GNU readline and history libraries, run-time libraries
ii  libreadline7:armhf                             7.0-3                        armhf                        GNU readline and history libraries, run-time libraries
ii  libresid-builder0c2a                           2.1.1-15                     armhf                        SID chip emulation class based on resid
ii  librest-0.7-0:armhf                            0.8.0-2                      armhf                        REST service access library
ii  librsvg2-2:armhf                               2.40.21-0+deb9u1             armhf                        SAX-based renderer library for SVG files (runtime)
ii  librsvg2-common:armhf                          2.40.21-0+deb9u1             armhf                        SAX-based renderer library for SVG files (extra runtime)
ii  librtmp1:armhf                                 2.4+20151223.gitfa8646d.1-1  armhf                        toolkit for RTMP streams (shared library)
ii  libsamplerate0:armhf                           0.1.8-8                      armhf                        Audio sample rate conversion library
ii  libsasl2-2:armhf                               2.1.27~101-g0780600+dfsg-3+d armhf                        Cyrus SASL - authentication abstraction library
ii  libsasl2-modules:armhf                         2.1.27~101-g0780600+dfsg-3+d armhf                        Cyrus SASL - pluggable authentication modules
ii  libsasl2-modules-db:armhf                      2.1.27~101-g0780600+dfsg-3+d armhf                        Cyrus SASL - pluggable authentication modules (DB)
ii  libsbc1:armhf                                  1.3-2                        armhf                        Sub Band CODEC library - runtime
ii  libsdl-image1.2:armhf                          1.2.12-5+deb9u2              armhf                        Image loading library for Simple DirectMedia Layer 1.2, libraries
ii  libsdl1.2debian:armhf                          1.2.15+dfsg1-4+rpt2          armhf                        Simple DirectMedia Layer
ii  libseccomp2:armhf                              2.3.1-2.1+deb9u1             armhf                        high level interface to Linux seccomp filter
ii  libsecret-1-0:armhf                            0.18.5-3.1                   armhf                        Secret store
ii  libsecret-common                               0.18.5-3.1                   all                          Secret store (common files)
ii  libselinux1:armhf                              2.6-3                        armhf                        SELinux runtime shared libraries
ii  libsemanage-common                             2.6-2                        all                          Common files for SELinux policy management libraries
ii  libsemanage1:armhf                             2.6-2                        armhf                        SELinux policy management library
ii  libsensors4:armhf                              1:3.4.0-4                    armhf                        library to read temperature/voltage/fan sensors
ii  libsepol1:armhf                                2.6-2                        armhf                        SELinux library for manipulating binary security policies
ii  libshine3:armhf                                3.1.0-5                      armhf                        Fixed-point MP3 encoding library - runtime files
ii  libshout3:armhf                                2.3.1-3                      armhf                        MP3/Ogg Vorbis broadcast streaming library
ii  libsidplay2                                    2.1.1-15                     armhf                        SID (MOS 6581) emulation library
ii  libsigc++-1.2-5c2                              1.2.7-2+b1                   armhf                        type-safe Signal Framework for C++ - runtime
ii  libsigc++-2.0-0v5:armhf                        2.10.0-1                     armhf                        type-safe Signal Framework for C++ - runtime
ii  libslang2:armhf                                2.3.1-5                      armhf                        S-Lang programming library - runtime version
ii  libsm6:armhf                                   2:1.2.2-1+b1                 armhf                        X11 Session Management library
ii  libsmartcols1:armhf                            2.29.2-1+deb9u1              armhf                        smart column output alignment library
ii  libsmbclient:armhf                             2:4.5.16+dfsg-1+deb9u3       armhf                        shared library for communication with SMB/CIFS servers
ii  libsmi2ldbl:armhf                              0.4.8+dfsg2-15               armhf                        library to access SMI MIB information
ii  libsnappy1v5:armhf                             1.1.3-3                      armhf                        fast compression/decompression library
ii  libsndfile1:armhf                              1.0.27-3+deb9u1              armhf                        Library for reading/writing audio files
ii  libsndio6.1:armhf                              1.1.0-3                      armhf                        Small audio and MIDI framework from OpenBSD, runtime libraries
ii  libsoup-gnome2.4-1:armhf                       2.56.0-2+deb9u2              armhf                        HTTP library implementation in C -- GNOME support library
ii  libsoup2.4-1:armhf                             2.56.0-2+deb9u2              armhf                        HTTP library implementation in C -- Shared library
ii  libsox-fmt-all:armhf                           14.4.1-5+deb9u2              armhf                        All SoX format libraries
ii  libsox-fmt-alsa:armhf                          14.4.1-5+deb9u2              armhf                        SoX alsa format I/O library
ii  libsox-fmt-ao:armhf                            14.4.1-5+deb9u2              armhf                        SoX Libao format I/O library
ii  libsox-fmt-base:armhf                          14.4.1-5+deb9u2              armhf                        Minimal set of SoX format libraries
ii  libsox-fmt-mp3:armhf                           14.4.1-5+deb9u2              armhf                        SoX MP2 and MP3 format library
ii  libsox-fmt-oss:armhf                           14.4.1-5+deb9u2              armhf                        SoX OSS format I/O library
ii  libsox-fmt-pulse:armhf                         14.4.1-5+deb9u2              armhf                        SoX PulseAudio format I/O library
ii  libsox2:armhf                                  14.4.1-5+deb9u2              armhf                        SoX library of audio effects and processing
ii  libsoxr0:armhf                                 0.1.2-2                      armhf                        High quality 1D sample-rate conversion library
ii  libspandsp2:armhf                              0.0.6+dfsg-0.1               armhf                        Telephony signal processing library
ii  libspeex1:armhf                                1.2~rc1.2-1                  armhf                        The Speex codec runtime library
ii  libspeexdsp1:armhf                             1.2~rc1.2-1                  armhf                        The Speex extended runtime library
ii  libsqlite3-0:armhf                             3.16.2-5+deb9u3              armhf                        SQLite 3 shared library
ii  libss2:armhf                                   1.43.4-2+deb9u2              armhf                        command-line interface parsing library
ii  libssh-gcrypt-4:armhf                          0.7.3-2+deb9u3               armhf                        tiny C SSH library (gcrypt flavor)
ii  libssh2-1:armhf                                1.7.0-1+deb9u1               armhf                        SSH2 client-side library
ii  libssl-dev:armhf                               1.1.0l-1~deb9u2              armhf                        Secure Sockets Layer toolkit - development files
ii  libssl-doc                                     1.1.0l-1~deb9u2              all                          Secure Sockets Layer toolkit - development documentation
ii  libssl1.0.2:armhf                              1.0.2u-1~deb9u3              armhf                        Secure Sockets Layer toolkit - shared libraries
ii  libssl1.1:armhf                                1.1.0l-1~deb9u2              armhf                        Secure Sockets Layer toolkit - shared libraries
ii  libstdc++-6-dev:armhf                          6.3.0-18+rpi1+deb9u1         armhf                        GNU Standard C++ Library v3 (development files)
ii  libstdc++6:armhf                               6.3.0-18+rpi1+deb9u1         armhf                        GNU Standard C++ Library v3
ii  libswresample2:armhf                           7:3.2.18-0+deb9u1            armhf                        FFmpeg library for audio resampling, rematrixing etc. - runtime files
ii  libswscale4:armhf                              7:3.2.18-0+deb9u1            armhf                        FFmpeg library for image scaling and various conversions - runtime files
ii  libsysfs2:armhf                                2.1.0+repack-4               armhf                        interface library to sysfs
ii  libsystemd0:armhf                              232-25+deb9u12               armhf                        systemd utility library
ii  libtag1v5:armhf                                1.11.1+dfsg.1-0.3+deb9u1     armhf                        audio meta-data library
ii  libtag1v5-vanilla:armhf                        1.11.1+dfsg.1-0.3+deb9u1     armhf                        audio meta-data library - vanilla flavour
ii  libtalloc2:armhf                               2.1.8-1                      armhf                        hierarchical pool based memory allocator
ii  libtasn1-6:armhf                               4.10-1.1+deb9u1              armhf                        Manage ASN.1 structures (runtime)
ii  libtdb1:armhf                                  1.3.11-2                     armhf                        Trivial Database - shared library
ii  libtevent0:armhf                               0.9.31-1                     armhf                        talloc-based event loop library - shared library
ii  libtext-charwidth-perl                         0.04-7+b7                    armhf                        get display widths of characters on the terminal
ii  libtext-iconv-perl                             1.7-5+b8                     armhf                        converts between character sets in Perl
ii  libtext-wrapi18n-perl                          0.06-7.1                     all                          internationalized substitute of Text::Wrap
ii  libthai-data                                   0.1.26-1                     all                          Data files for Thai language support library
ii  libthai0:armhf                                 0.1.26-1                     armhf                        Thai language support library
ii  libtheora0:armhf                               1.1.1+dfsg.1-14              armhf                        Theora Video Compression Codec
ii  libtie-ixhash-perl                             1.23-2                       all                          Perl module to order associative arrays
ii  libtiff5:armhf                                 4.0.8-2+deb9u5               armhf                        Tag Image File Format (TIFF) library
ii  libtimedate-perl                               2.3000-2+deb9u1              all                          collection of modules to manipulate date/time information
ii  libtinfo5:armhf                                6.0+20161126-1+deb9u2        armhf                        shared low-level terminfo library for terminal handling
ii  libtirpc1:armhf                                0.2.5-1.2+deb9u1             armhf                        transport-independent RPC library
ii  libtwolame0:armhf                              0.3.13-2                     armhf                        MPEG Audio Layer 2 encoding library
ii  libtxc-dxtn-s2tc:armhf                         1.0+git20151227-2            armhf                        Texture compression library for Mesa
ii  libubsan0:armhf                                6.3.0-18+rpi1+deb9u1         armhf                        UBSan -- undefined behaviour sanitizer (runtime)
ii  libudev0:armhf                                 175-7.2                      armhf                        libudev shared library
ii  libudev1:armhf                                 232-25+deb9u12               armhf                        libudev shared library
ii  libunistring0:armhf                            0.9.6+really0.9.3-0.1        armhf                        Unicode string library for C
ii  libupnp6                                       1:1.6.19+git20160116-1.2+deb armhf                        Portable SDK for UPnP Devices, version 1.6 (shared libraries)
ii  liburi-perl                                    1.71-1                       all                          module to manipulate and access URI strings
ii  libusageenvironment3:armhf                     2016.11.28-1+deb9u2          armhf                        multimedia RTSP streaming library (UsageEnvironment classes)
ii  libusb-0.1-4:armhf                             2:0.1.12-30                  armhf                        userspace USB programming library
ii  libusb-1.0-0:armhf                             2:1.0.21-1                   armhf                        userspace USB programming library
ii  libustr-1.0-1:armhf                            1.0.4-6                      armhf                        Micro string library: shared library
ii  libuuid1:armhf                                 2.29.2-1+deb9u1              armhf                        Universally Unique ID library
ii  libuv1:armhf                                   1.18.0-3~bpo9+1              armhf                        asynchronous event notification library - runtime library
ii  libuv1-dev:armhf                               1.18.0-3~bpo9+1              armhf                        asynchronous event notification library - development files
ii  libv4l-0:armhf                                 1.12.3-1                     armhf                        Collection of video4linux support libraries
ii  libv4l2rds0:armhf                              1.12.3-1                     armhf                        Video4Linux Radio Data System (RDS) decoding library
ii  libv4lconvert0:armhf                           1.12.3-1                     armhf                        Video4linux frame format conversion library
ii  libva-drm1:armhf                               1.7.3-2                      armhf                        Video Acceleration (VA) API for Linux -- DRM runtime
ii  libva-wayland1:armhf                           1.7.3-2                      armhf                        Video Acceleration (VA) API for Linux -- Wayland runtime
ii  libva-x11-1:armhf                              1.7.3-2                      armhf                        Video Acceleration (VA) API for Linux -- X11 runtime
ii  libva1:armhf                                   1.7.3-2                      armhf                        Video Acceleration (VA) API for Linux -- runtime
ii  libvdpau-va-gl1:armhf                          0.4.2-1                      armhf                        VDPAU driver with OpenGL/VAAPI backend
ii  libvdpau1:armhf                                1.1.1-6                      armhf                        Video Decode and Presentation API for Unix (libraries)
ii  libvisual-0.4-0:armhf                          0.4.0-10                     armhf                        audio visualization framework
ii  libvlc-bin:armhf                               3.0.12-0+deb9u1              armhf                        tools for VLC's base library
ii  libvlc5:armhf                                  3.0.12-0+deb9u1              armhf                        multimedia player and streamer library
ii  libvlccore9:armhf                              3.0.12-0+deb9u1              armhf                        base library for VLC and its modules
ii  libvorbis0a:armhf                              1.3.5-4+deb9u2               armhf                        decoder library for Vorbis General Audio Compression Codec
ii  libvorbisenc2:armhf                            1.3.5-4+deb9u2               armhf                        encoder library for Vorbis General Audio Compression Codec
ii  libvorbisfile3:armhf                           1.3.5-4+deb9u2               armhf                        high-level API for Vorbis General Audio Compression Codec
ii  libvorbisidec1                                 1.0.2+svn18153-1+deb9u1      armhf                        Integer-only Ogg Vorbis decoder, AKA "tremor"
ii  libvpx4:armhf                                  1.6.1-3+deb9u2               armhf                        VP8 and VP9 video codec (shared library)
ii  libwacom-bin                                   0.22-1                       armhf                        Wacom model feature query library -- binaries
ii  libwacom-common                                0.22-1                       all                          Wacom model feature query library (common files)
ii  libwacom2:armhf                                0.22-1                       armhf                        Wacom model feature query library
ii  libwavpack1:armhf                              5.0.0-2+deb9u2               armhf                        audio codec (lossy and lossless) - library
ii  libwayland-client0:armhf                       1.12.0-1+deb9u1              armhf                        wayland compositor infrastructure - client library
ii  libwayland-egl1-mesa:armhf                     13.0.6-1+rpi2                armhf                        implementation of the Wayland EGL platform -- runtime
ii  libwayland-server0:armhf                       1.12.0-1+deb9u1              armhf                        wayland compositor infrastructure - server library
ii  libwbclient0:armhf                             2:4.5.16+dfsg-1+deb9u3       armhf                        Samba winbind client library
ii  libwebp6:armhf                                 0.5.2-1                      armhf                        Lossy compression of digital photographic images.
ii  libwebpmux2:armhf                              0.5.2-1                      armhf                        Lossy compression of digital photographic images.
ii  libwireshark-data                              2.6.8-1.1~deb9u1             all                          network packet dissection library -- data files
ii  libwireshark11:armhf                           2.6.8-1.1~deb9u1             armhf                        network packet dissection library -- shared library
ii  libwiretap8:armhf                              2.6.8-1.1~deb9u1             armhf                        network packet capture library -- shared library
ii  libwrap0:armhf                                 7.6.q-26                     armhf                        Wietse Venema's TCP wrappers library
ii  libwscodecs2:armhf                             2.6.8-1.1~deb9u1             armhf                        network packet dissection codecs library -- shared library
ii  libwsutil9:armhf                               2.6.8-1.1~deb9u1             armhf                        network packet dissection utilities library -- shared library
ii  libwww-perl                                    6.15-1                       all                          simple and consistent interface to the world-wide web
ii  libwww-robotrules-perl                         6.01-1                       all                          database of robots.txt-derived permissions
ii  libx11-6:armhf                                 2:1.6.4-3+deb9u3             armhf                        X11 client-side library
ii  libx11-data                                    2:1.6.4-3+deb9u3             all                          X11 client-side library
ii  libx11-protocol-perl                           0.56-7                       all                          Perl module for the X Window System Protocol, version 11
ii  libx11-xcb1:armhf                              2:1.6.4-3+deb9u3             armhf                        Xlib/XCB interface library
ii  libx264-148:armhf                              2:0.148.2748+git97eaef2-1+rp armhf                        x264 video coding library
ii  libx265-95:armhf                               2.1-2                        armhf                        H.265/HEVC video stream encoder (shared library)
ii  libxapian30:armhf                              1.4.3-2+deb9u3               armhf                        Search engine library
ii  libxau6:armhf                                  1:1.0.8-1                    armhf                        X11 authorisation library
ii  libxaw7:armhf                                  2:1.0.13-1                   armhf                        X11 Athena Widget library
ii  libxcb-dri2-0:armhf                            1.12-1                       armhf                        X C Binding, dri2 extension
ii  libxcb-dri3-0:armhf                            1.12-1                       armhf                        X C Binding, dri3 extension
ii  libxcb-glx0:armhf                              1.12-1                       armhf                        X C Binding, glx extension
ii  libxcb-icccm4:armhf                            0.4.1-1                      armhf                        utility libraries for X C Binding -- icccm
ii  libxcb-image0:armhf                            0.4.0-1                      armhf                        utility libraries for X C Binding -- image
ii  libxcb-keysyms1:armhf                          0.4.0-1                      armhf                        utility libraries for X C Binding -- keysyms
ii  libxcb-present0:armhf                          1.12-1                       armhf                        X C Binding, present extension
ii  libxcb-randr0:armhf                            1.12-1                       armhf                        X C Binding, randr extension
ii  libxcb-render-util0:armhf                      0.3.9-1                      armhf                        utility libraries for X C Binding -- render-util
ii  libxcb-render0:armhf                           1.12-1                       armhf                        X C Binding, render extension
ii  libxcb-shape0:armhf                            1.12-1                       armhf                        X C Binding, shape extension
ii  libxcb-shm0:armhf                              1.12-1                       armhf                        X C Binding, shm extension
ii  libxcb-sync1:armhf                             1.12-1                       armhf                        X C Binding, sync extension
ii  libxcb-util0:armhf                             0.3.8-3                      armhf                        utility libraries for X C Binding -- atom, aux and event
ii  libxcb-xfixes0:armhf                           1.12-1                       armhf                        X C Binding, xfixes extension
ii  libxcb-xinerama0:armhf                         1.12-1                       armhf                        X C Binding, xinerama extension
ii  libxcb-xkb1:armhf                              1.12-1                       armhf                        X C Binding, XKEYBOARD extension
ii  libxcb-xv0:armhf                               1.12-1                       armhf                        X C Binding, xv extension
ii  libxcb1:armhf                                  1.12-1                       armhf                        X C Binding
ii  libxcomposite1:armhf                           1:0.4.4-2                    armhf                        X11 Composite extension library
ii  libxcursor1:armhf                              1:1.1.14-1+deb9u2            armhf                        X cursor management library
ii  libxdamage1:armhf                              1:1.1.4-2+b1                 armhf                        X11 damaged region extension library
ii  libxdmcp6:armhf                                1:1.1.2-3                    armhf                        X11 Display Manager Control Protocol library
ii  libxext6:armhf                                 2:1.3.3-1                    armhf                        X11 miscellaneous extension library
ii  libxfixes3:armhf                               1:5.0.3-1                    armhf                        X11 miscellaneous 'fixes' extension library
ii  libxft2:armhf                                  2.3.2-1                      armhf                        FreeType-based font drawing library for X
ii  libxi6:armhf                                   2:1.7.9-1                    armhf                        X11 Input extension library
ii  libxinerama1:armhf                             2:1.1.3-1+b1                 armhf                        X11 Xinerama extension library
ii  libxkbcommon-x11-0:armhf                       0.7.1-2~deb9u1               armhf                        library to create keymaps with the XKB X11 protocol
ii  libxkbcommon0:armhf                            0.7.1-2~deb9u1               armhf                        library interface to the XKB compiler - shared library
ii  libxml-parser-perl                             2.44-2+b1                    armhf                        Perl module for parsing XML files
ii  libxml-twig-perl                               1:3.50-1                     all                          Perl module for processing huge XML documents in tree mode
ii  libxml-xpathengine-perl                        0.13-1                       all                          re-usable XPath engine for DOM-like trees
ii  libxml2:armhf                                  2.9.4+dfsg1-2.2+deb9u3       armhf                        GNOME XML library
ii  libxmu6:armhf                                  2:1.1.2-2                    armhf                        X11 miscellaneous utility library
ii  libxmuu1:armhf                                 2:1.1.2-2                    armhf                        X11 miscellaneous micro-utility library
ii  libxpm4:armhf                                  1:3.5.12-1                   armhf                        X11 pixmap library
ii  libxrandr2:armhf                               2:1.5.1-1                    armhf                        X11 RandR extension library
ii  libxrender1:armhf                              1:0.9.10-1                   armhf                        X Rendering Extension client library
ii  libxshmfence1:armhf                            1.2-1                        armhf                        X shared memory fences - shared library
ii  libxss1:armhf                                  1:1.2.2-1                    armhf                        X11 Screen Saver extension library
ii  libxt6:armhf                                   1:1.1.5-1                    armhf                        X11 toolkit intrinsics library
ii  libxtables12:armhf                             1.6.0+snapshot20161117-6     armhf                        netfilter xtables library
ii  libxtst6:armhf                                 2:1.2.3-1                    armhf                        X11 Testing -- Record extension library
ii  libxv1:armhf                                   2:1.0.11-1                   armhf                        X11 Video extension library
ii  libxvidcore4:armhf                             2:1.3.4-1                    armhf                        Open source MPEG-4 video codec (library)
ii  libxvmc1:armhf                                 2:1.0.10-1                   armhf                        X11 Video extension library
ii  libxxf86dga1:armhf                             2:1.1.4-1                    armhf                        X11 Direct Graphics Access extension library
ii  libxxf86vm1:armhf                              1:1.1.4-1                    armhf                        X11 XFree86 video mode extension library
ii  libyaml-0-2:armhf                              0.1.7-2                      armhf                        Fast YAML 1.1 parser and emitter library
ii  libzvbi-common                                 0.2.35-13                    all                          Vertical Blanking Interval decoder (VBI) - common files
ii  libzvbi0:armhf                                 0.2.35-13                    armhf                        Vertical Blanking Interval decoder (VBI) - runtime files
ii  linux-base                                     4.5                          all                          Linux image base package
ii  linux-libc-dev:armhf                           4.9.82-1+deb9u3+rpi1         armhf                        Linux support headers for userspace development
ii  lirc                                           0.9.4c-9                     armhf                        Infra-red remote control support - daemons and utils
ii  locales                                        2.24-11+deb9u4               all                          GNU C Library: National Language (locale) data [support]
ii  login                                          1:4.4-4.1                    armhf                        system login tools
ii  logrotate                                      3.11.0-0.1                   armhf                        Log rotation utility
ii  lsb-base                                       9.20161125+rpi1              all                          Linux Standard Base init script functionality
ii  lsb-release                                    9.20161125+rpi1              all                          Linux Standard Base version reporting utility
ii  lua5.1                                         5.1.5-8.1                    armhf                        Simple, extensible, embeddable programming language
ii  luajit                                         2.0.4+dfsg-1+deb9u1          armhf                        Just in time compiler for Lua programming language version 5.1
ii  mailutils                                      1:3.1.1-1                    armhf                        GNU mailutils utilities for handling mail
ii  mailutils-common                               1:3.1.1-1                    all                          Common files for GNU mailutils
ii  make                                           4.1-9.1                      armhf                        utility for directing compilation
ii  makedev                                        2.3.1-93                     all                          creates device files in /dev
ii  man-db                                         2.7.6.1-2                    armhf                        on-line manual pager
ii  manpages                                       4.10-2                       all                          Manual pages about using a GNU/Linux system
ii  manpages-dev                                   4.10-2                       all                          Manual pages about using GNU/Linux for development
ii  mawk                                           1.3.3-17                     armhf                        a pattern scanning and text processing language
ii  mesa-utils                                     8.3.0-3                      armhf                        Miscellaneous Mesa GL utilities
ii  mesa-va-drivers:armhf                          13.0.6-1+rpi2                armhf                        Mesa VA-API video acceleration drivers
ii  mesa-vdpau-drivers:armhf                       13.0.6-1+rpi2                armhf                        Mesa VDPAU video acceleration drivers
ii  mime-support                                   3.60                         all                          MIME files 'mime.types' & 'mailcap', and support programs
ii  mount                                          2.29.2-1+deb9u1              armhf                        tools for mounting and manipulating filesystems
ii  mountall                                       2.54                         armhf                        filesystem mounting tool
ii  mpg123                                         1.23.8-1                     armhf                        MPEG layer 1/2/3 audio player
ii  mplayer                                        2:1.3.0-6                    armhf                        movie player for Unix-like systems
ii  multiarch-support                              2.24-11+deb9u4               armhf                        Transitional package to ensure multiarch compatibility
ii  mysql-common                                   5.8+1.0.2                    all                          MySQL database common files, e.g. /etc/mysql/my.cnf
ii  nano                                           2.7.4-1                      armhf                        small, friendly text editor inspired by Pico
ii  ncdu                                           1.12-1                       armhf                        ncurses disk usage viewer
ii  ncurses-base                                   6.0+20161126-1+deb9u2        all                          basic terminal type definitions
ii  ncurses-bin                                    6.0+20161126-1+deb9u2        armhf                        terminal-related programs and man pages
ii  ncurses-term                                   6.0+20161126-1+deb9u2        all                          additional terminal type definitions
ii  net-tools                                      1.60+git20161116.90da8a0-1   armhf                        NET-3 networking toolkit
ii  netbase                                        5.4                          all                          Basic TCP/IP networking system
ii  netcat-openbsd                                 1.130-3                      armhf                        TCP/IP swiss army knife
ii  netcat-traditional                             1.10-41                      armhf                        TCP/IP swiss army knife
ii  nfs-common                                     1:1.3.4-2.1+deb9u1           armhf                        NFS support files common to client and server
ii  node-abbrev                                    1.0.9-1                      all                          Get unique abbreviations for a set of strings - Node.js module
ii  node-ansi                                      0.3.0-2                      all                          Advanced ANSI formatting tool for Node.js
ii  node-ansi-color-table                          1.0.0-1                      all                          Color and format tables for ansi output - Node.js module
ii  node-archy                                     1.0.0-1                      all                          Pretty-print nested hierarchies module for Node.js
ii  node-async                                     0.8.0-1                      all                          higher-order functions and common patterns for asynchronous Javascript
ii  node-balanced-match                            0.4.2-1                      all                          Match balanced character pairs in Node.js
ii  node-block-stream                              0.0.9-1                      all                          Stream of fixed-size blocks, with zero-padding when necessary
ii  node-brace-expansion                           1.1.6-1+deb9u1               all                          Brace expansion as known from sh/bash for Node.js
ii  node-builtin-modules                           1.1.1-1                      all                          List of the Node.js builtin modules
ii  node-combined-stream                           0.0.5-1                      all                          Append streams one after another - module for Node.js
ii  node-concat-map                                0.0.1-1                      all                          concatenative mapdashery for Node.js
ii  node-cookie-jar                                0.3.1-1                      all                          Cookie handling for HTTP clients - module for Node.js
ii  node-delayed-stream                            0.0.5-1                      all                          Buffer stream events for later handling - module for Node.js
ii  node-forever-agent                             0.5.1-1                      all                          HTTP agent supporting keep-alive requests - module for Node.js
ii  node-form-data                                 0.1.0-1                      all                          Create multipart/form-data streams module for Node.js
ii  node-fs.realpath                               1.0.0-1                      all                          Use node's fs.realpath
ii  node-fstream                                   1.0.10-1+deb9u1              all                          Advanced filesystem streaming tools for Node.js
ii  node-fstream-ignore                            0.0.6-2                      all                          Directory reader configurable by .ignore module for Node.js
ii  node-github-url-from-git                       1.4.0-1                      all                          Convert github git or gist url to an http url - Node.js module
ii  node-glob                                      7.1.1-1                      all                          glob functionality for Node.js
ii  node-graceful-fs                               4.1.11-1                     all                          drop-in replacement improving the Node.js fs module
ii  node-gyp                                       3.4.0-1                      all                          Native addon build tool for Node.js
ii  node-hosted-git-info                           2.1.5-1                      all                          Provides metadata from Github, Bitbucket and Gitlab
ii  node-inflight                                  1.0.6-1                      all                          add callbacks to requests in flight to avoid async duplication
ii  node-inherits                                  2.0.3-1                      all                          Exposes inherits function from Node.js environment
ii  node-ini                                       1.1.0-1+deb9u1               all                          ini format parser and serializer for Node.js
ii  node-is-builtin-module                         1.0.0-1                      all                          Check if string matches name of a Node.js builtin module
ii  node-isexe                                     1.1.2-1                      all                          minimal module to check if a file is executable
ii  node-json-stringify-safe                       5.0.0-1                      all                          JSON.stringify with circular references module for Node.js
ii  node-lockfile                                  0.4.1-1                      all                          Asynchronous file lock module for Node.js
ii  node-lru-cache                                 4.0.2-1                      all                          least-recently-used cache object for Node.js
ii  node-mime                                      1.3.4-1                      all                          library for mime-type mapping for Node.js
ii  node-minimatch                                 3.0.3-1                      all                          Convert glob expressions into RegExp objects for Node.js
ii  node-mkdirp                                    0.5.0-1                      all                          Recursively create directories - Node.js module
ii  node-mute-stream                               0.0.7-1                      all                          Pass-through stream that can be muted module for Node.js
ii  node-node-uuid                                 1.4.0-1                      all                          simple, fast generation of RFC4122 UUIDs - Node module
ii  node-nopt                                      3.0.6-3                      all                          Command-line option parser for Node.js
ii  node-normalize-package-data                    2.3.5-2                      all                          Normalizes package metadata - Node.js module
ii  node-npmlog                                    0.0.4-1                      all                          Logger with custom levels and colored output for Node.js
ii  node-once                                      1.4.0-2                      all                          Run a function only once with this module for Node.js
ii  node-osenv                                     0.1.0-1                      all                          Environment settings lookup module for Node.js
ii  node-path-is-absolute                          1.0.0-1                      all                          Node.js 0.12 path.isAbsolute() ponyfill
ii  node-pseudomap                                 1.0.2-1                      all                          like ES6 `Map`, but without iterators
ii  node-qs                                        2.2.4-1                      all                          Parse, stringify query strings for Node.js
ii  node-read                                      1.0.7-1                      all                          Read user input from stdin module for Node.js
ii  node-read-package-json                         1.2.4-1                      all                          Read package.json for npm module for Node.js
ii  node-request                                   2.26.1-1                     all                          simplified HTTP request client module for Node.js
ii  node-retry                                     0.6.0-1                      all                          Retry strategies for failed operations module for Node.js
ii  node-rimraf                                    2.5.4-2                      all                          Deep deletion (like rm -rf) module for Node.js
ii  node-semver                                    5.3.0-1                      all                          Semantic Versioning for Node.js
ii  node-sha                                       1.2.3-1                      all                          Check and get file or stream hashes - module for Node.js
ii  node-slide                                     1.1.4-1                      all                          Simple chain and asyncMap flow control module for Node.js
ii  node-spdx-correct                              1.0.2-1                      all                          correct invalid SPDX identifiers
ii  node-spdx-expression-parse                     1.0.4-1                      all                          parse SPDX license expressions
ii  node-spdx-license-ids                          1.2.2-1                      all                          List of SPDX license identifiers
ii  node-tar                                       2.2.1-1                      all                          read and write portable tar archives module for Node.js
ii  node-tunnel-agent                              0.3.1-1                      all                          HTTP proxy tunneling agent module for Node.js
ii  node-underscore                                1.8.3~dfsg-1+deb9u1          all                          JavaScript's functional programming helper library - NodeJS
ii  node-validate-npm-package-license              3.0.1-1                      all                          Tells if a string is a valid npm package license string
ii  node-which                                     1.2.11-1                     all                          Cross-platform 'which' module for Node.js
ii  node-wrappy                                    1.0.2-1                      all                          Callback wrapping utility
ii  node-yallist                                   2.0.0-1                      all                          Yet Another Linked List
ii  nodejs                                         8.11.1~dfsg-2~bpo9+1         armhf                        evented I/O for V8 javascript
ii  nodejs-dev                                     8.11.1~dfsg-2~bpo9+1         armhf                        evented I/O for V8 javascript (development files)
ii  nodejs-doc                                     8.11.1~dfsg-2~bpo9+1         all                          API documentation for Node.js, the javascript platform
ii  notification-daemon                            3.20.0-1                     armhf                        daemon for displaying passive pop-up notifications
ii  npm                                            1.4.21+ds-2                  all                          package manager for Node.js
ii  openresolv                                     3.8.0-1                      armhf                        management framework for resolv.conf
ii  openssh-client                                 1:7.4p1-10+deb9u7            armhf                        secure shell (SSH) client, for secure access to remote machines
ii  openssh-server                                 1:7.4p1-10+deb9u7            armhf                        secure shell (SSH) server, for secure access from remote machines
ii  openssh-sftp-server                            1:7.4p1-10+deb9u7            armhf                        secure shell (SSH) sftp server module, for SFTP access from remote machines
ii  openssl                                        1.1.0l-1~deb9u2              armhf                        Secure Sockets Layer toolkit - cryptographic utility
ii  parted                                         3.2-17                       armhf                        disk partition manipulator
ii  passwd                                         1:4.4-4.1                    armhf                        change and administer password and group data
ii  patch                                          2.7.5-1+deb9u2               armhf                        Apply a diff file to an original
ii  paxctld                                        1.2.1-1                      armhf                        Daemon to automatically set appropriate PaX flags
ii  perl                                           5.24.1-3+deb9u7              armhf                        Larry Wall's Practical Extraction and Report Language
ii  perl-base                                      5.24.1-3+deb9u7              armhf                        minimal Perl system
ii  perl-modules-5.24                              5.24.1-3+deb9u7              all                          Core Perl modules
ii  perl-openssl-defaults:armhf                    3                            armhf                        version compatibility baseline for Perl OpenSSL packages
ii  pi-bluetooth                                   0.1.10                       all                          Raspberry Pi 3 bluetooth
ii  pigpio                                         1.64-1                       armhf                        Library for Raspberry Pi GPIO control
ii  pinentry-curses                                1.0.0-2                      armhf                        curses-based PIN or pass-phrase entry dialog for GnuPG
ii  pkg-config                                     0.29-4                       armhf                        manage compile and link flags for libraries
ii  plymouth                                       0.9.2-4+rpi1                 armhf                        boot animation, logger and I/O multiplexer
ii  policykit-1                                    0.105-18+deb9u1              armhf                        framework for managing administrative policies and privileges
ii  procps                                         2:3.3.12-3+deb9u1            armhf                        /proc file system utilities
ii  psmisc                                         22.21-2.1                    armhf                        utilities that use the proc file system
ii  python                                         2.7.13-2                     armhf                        interactive high-level object-oriented language (default version)
ii  python-all                                     2.7.13-2                     armhf                        package depending on all supported Python runtime versions
ii  python-all-dev                                 2.7.13-2                     armhf                        package depending on all supported Python development packages
ii  python-apt-common                              1.4.3                        all                          Python interface to libapt-pkg (locales)
ii  python-blinker                                 1.3.dfsg2-1                  all                          Fast, simple object-to-object and broadcast signaling library
ii  python-cffi-backend                            1.9.1-2                      armhf                        Foreign Function Interface for Python calling C code - backend
ii  python-click                                   6.6-1                        all                          Simple wrapper around optparse for powerful command line utilities - Python 2.7
ii  python-colorama                                0.3.7-1                      all                          Cross-platform colored terminal text in Python - Python 2.x
ii  python-crypto                                  2.6.1-7                      armhf                        cryptographic algorithms and protocols for Python
ii  python-cryptography                            1.7.1-3+deb9u2               armhf                        Python library exposing cryptographic recipes and primitives (Python 2)
ii  python-dbus                                    1.2.4-1                      armhf                        simple interprocess messaging system (Python interface)
ii  python-dev                                     2.7.13-2                     armhf                        header files and a static library for Python (default)
ii  python-enum34                                  1.1.6-1                      all                          backport of Python 3.4's enum package
ii  python-flask                                   0.12.1-1                     all                          micro web framework based on Werkzeug and Jinja2 - Python 2.7
ii  python-flask-doc                               0.12.1-1                     all                          documentation for Flask micro web framework
ii  python-flaskext.wtf                            0.12-2                       all                          Simple integration of Flask and WTForms (Python 2)
ii  python-gi                                      3.22.0-2                     armhf                        Python 2.x bindings for gobject-introspection libraries
ii  python-gst-1.0                                 1.10.4-1                     armhf                        GStreamer GObject Introspection overrides for Python
ii  python-idna                                    2.2-1                        all                          Python IDNA2008 (RFC 5891) handling (Python 2)
ii  python-ipaddress                               1.0.17-1                     all                          Backport of Python 3 ipaddress module (Python 2)
ii  python-itsdangerous                            0.24+dfsg1-2                 all                          Various helpers to pass trusted data to untrusted environment - Python 2.x
ii  python-jinja2                                  2.8-1                        all                          small but fast and easy to use stand-alone template engine
ii  python-keyring                                 10.1-1                       all                          store and access your passwords safely
ii  python-keyrings.alt                            1.3-1                        all                          alternate backend implementations for python-keyring
ii  python-lirc                                    1.2.1-2                      armhf                        LIRC client API (Python 2)
ii  python-markupsafe                              0.23-3                       armhf                        HTML/XHTML/XML string library for Python
ii  python-minimal                                 2.7.13-2                     armhf                        minimal subset of the Python language (default version)
ii  python-openssl                                 16.2.0-1                     all                          Python 2 wrapper around the OpenSSL library
ii  python-pip                                     9.0.1-2+rpt2                 all                          Python package installer
ii  python-pip-whl                                 9.0.1-2+rpt2                 all                          Python package installer
ii  python-pkg-resources                           33.1.1-1                     all                          Package Discovery and Resource Access using pkg_resources
ii  python-pyasn1                                  0.1.9-2                      all                          ASN.1 library for Python (Python 2 module)
ii  python-pyaudio                                 0.2.11-1                     armhf                        Python bindings for PortAudio v19
ii  python-pyinotify                               0.9.6-1                      all                          simple Linux inotify Python bindings
ii  python-rpi.gpio                                0.6.5~stretch-1              armhf                        Python GPIO module for Raspberry Pi
ii  python-secretstorage                           2.3.1-2                      all                          Python module for storing secrets - Python 2.x version
ii  python-setuptools                              33.1.1-1                     all                          Python Distutils Enhancements
ii  python-simplejson                              3.10.0-1                     armhf                        simple, fast, extensible JSON encoder/decoder for Python 2.x
ii  python-six                                     1.12.0-0+rpt1                all                          Python 2 and 3 compatibility utilities (Python 2)
ii  python-smbus:armhf                             3.1.2-3                      armhf                        Python bindings for Linux SMBus access through i2c-dev
ii  python-talloc                                  2.1.8-1                      armhf                        hierarchical pool based memory allocator - Python bindings
ii  python-werkzeug                                0.11.15+dfsg1-1+deb9u1       all                          collection of utilities for WSGI applications (Python 2.x)
ii  python-wheel                                   0.29.0-2                     all                          built-package format for Python
ii  python-wtforms                                 2.1-1                        all                          flexible forms validation and rendering library for Python 2
ii  python-xdg                                     0.25-4                       all                          Python 2 library to access freedesktop.org standards
ii  python2.7                                      2.7.13-2+deb9u4              armhf                        Interactive high-level object-oriented language (version 2.7)
ii  python2.7-dev                                  2.7.13-2+deb9u4              armhf                        Header files and a static library for Python (v2.7)
ii  python2.7-minimal                              2.7.13-2+deb9u4              armhf                        Minimal subset of the Python language (version 2.7)
ii  python3                                        3.5.3-1                      armhf                        interactive high-level object-oriented language (default python3 version)
ii  python3-apt                                    1.4.3                        armhf                        Python 3 interface to libapt-pkg
ii  python3-cffi-backend                           1.9.1-2                      armhf                        Foreign Function Interface for Python 3 calling C code - runtime
ii  python3-chardet                                2.3.0-2                      all                          universal character encoding detector for Python3
ii  python3-crypto                                 2.6.1-7                      armhf                        cryptographic algorithms and protocols for Python 3
ii  python3-cryptography                           1.7.1-3+deb9u2               armhf                        Python library exposing cryptographic recipes and primitives (Python 3)
ii  python3-dbus                                   1.2.4-1                      armhf                        simple interprocess messaging system (Python 3 interface)
ii  python3-dev                                    3.5.3-1                      armhf                        header files and a static library for Python (default)
ii  python3-gi                                     3.22.0-2                     armhf                        Python 3 bindings for gobject-introspection libraries
ii  python3-idna                                   2.2-1                        all                          Python IDNA2008 (RFC 5891) handling (Python 3)
ii  python3-keyring                                10.1-1                       all                          store and access your passwords safely - Python 3 version of the package
ii  python3-keyrings.alt                           1.3-1                        all                          alternate backend implementations for python3-keyring
ii  python3-lirc                                   1.2.1-2                      armhf                        LIRC client API (Python 3)
ii  python3-minimal                                3.5.3-1                      armhf                        minimal subset of the Python language (default python3 version)
ii  python3-pip                                    9.0.1-2+rpt2                 all                          Python package installer
ii  python3-pkg-resources                          33.1.1-1                     all                          Package Discovery and Resource Access using pkg_resources
ii  python3-pyasn1                                 0.1.9-2                      all                          ASN.1 library for Python (Python 3 module)
ii  python3-requests                               2.12.4-1                     all                          elegant and simple HTTP library for Python3, built for human beings
ii  python3-secretstorage                          2.3.1-2                      all                          Python module for storing secrets - Python 3.x version
ii  python3-setuptools                             33.1.1-1                     all                          Python3 Distutils Enhancements
ii  python3-six                                    1.12.0-0+rpt1                all                          Python 2 and 3 compatibility utilities (Python 3)
ii  python3-smbus:armhf                            3.1.2-3                      armhf                        Python 3 bindings for Linux SMBus access through i2c-dev
ii  python3-urllib3                                1.19.1-1                     all                          HTTP library with thread-safe connection pooling for Python3
ii  python3-wheel                                  0.29.0-2                     all                          built-package format for Python
ii  python3-xdg                                    0.25-4+deb9u1                all                          Python 3 library to access freedesktop.org standards
ii  python3-yaml                                   3.12-1                       armhf                        YAML parser and emitter for Python3
ii  python3.5                                      3.5.3-1+deb9u5               armhf                        Interactive high-level object-oriented language (version 3.5)
ii  python3.5-dev                                  3.5.3-1+deb9u5               armhf                        Header files and a static library for Python (v3.5)
ii  python3.5-minimal                              3.5.3-1+deb9u5               armhf                        Minimal subset of the Python language (version 3.5)
ii  qt5-gtk-platformtheme:armhf                    5.7.1+dfsg-3+rpi1+deb9u3     armhf                        Qt 5 GTK+ 3 platform theme
ii  qttranslations5-l10n                           5.7.1~20161021-1             all                          translations for Qt 5
ii  raspberrypi-bootloader                         1.20190819~stretch-1         armhf                        Raspberry Pi bootloader
ii  raspberrypi-kernel                             1.20190819~stretch-1         armhf                        Raspberry Pi bootloader
ii  raspberrypi-net-mods                           1.2.7                        all                          Network configuration for the Raspberry Pi UI
ii  raspberrypi-sys-mods                           20181127                     armhf                        System tweaks for the Raspberry Pi
ii  raspbian-archive-keyring                       20120528.2                   all                          GnuPG archive keys of the raspbian archive
ii  raspi-config                                   20190423                     all                          Raspberry Pi configuration tool
ii  raspi-copies-and-fills                         0.11                         armhf                        ARM-accelerated versions of selected functions from string.h
ii  read-edid                                      3.0.2-1                      armhf                        hardware information-gathering tool for VESA PnP monitors
ii  readline-common                                7.0-3                        all                          GNU readline and history libraries, common files
ii  rename                                         0.20-4                       all                          Perl extension for renaming multiple files
ii  rfkill                                         0.5-1                        armhf                        tool for enabling and disabling wireless devices
ii  rng-tools5                                     5-1                          armhf                        Daemon to use a Hardware TRNG
ii  rpcbind                                        0.2.3-0.6                    armhf                        converts RPC program numbers into universal addresses
ii  rpi-update                                     20140705                     all                          Raspberry Pi firmware updating tool
ii  rsync                                          3.1.2-1+deb9u2               armhf                        fast, versatile, remote (and local) file-copying tool
ii  rsyslog                                        8.24.0-1                     armhf                        reliable system and kernel logging daemon
ii  samba-common                                   2:4.5.16+dfsg-1+deb9u3       all                          common files used by both the Samba server and client
ii  samba-libs:armhf                               2:4.5.16+dfsg-1+deb9u3       armhf                        Samba core libraries
ii  sed                                            4.4-1                        armhf                        GNU stream editor for filtering/transforming text
ii  sensible-utils                                 0.0.9+deb9u1                 all                          Utilities for sensible alternative selection
ii  setserial                                      2.17-50                      armhf                        controls configuration of serial ports
ii  sgml-base                                      1.29                         all                          SGML infrastructure and SGML catalog file support
ii  shared-mime-info                               1.8-1+deb9u1                 armhf                        FreeDesktop.org shared MIME database and spec
ii  sox                                            14.4.1-5+deb9u2              armhf                        Swiss army knife of sound processing
ii  ssh                                            1:7.4p1-10+deb9u7            all                          secure shell client and server (metapackage)
ii  ssh-import-id                                  5.6-1                        all                          securely retrieve an SSH public key and install it locally
ii  strace                                         4.15-2                       armhf                        System call tracer
ii  sudo                                           1.8.19p1-2.1+deb9u2          armhf                        Provide limited super user privileges to specific users
ii  systemd                                        232-25+deb9u12               armhf                        system and service manager
ii  systemd-sysv                                   232-25+deb9u12               armhf                        system and service manager - SysV links
ii  sysvinit-utils                                 2.88dsf-59.9                 armhf                        System-V-like utilities
ii  tar                                            1.29b-1.1                    armhf                        GNU version of the tar archiving utility
ii  tasksel                                        3.39                         all                          tool for selecting tasks for installation on Debian systems
ii  tasksel-data                                   3.39                         all                          official tasks used for installation of Debian systems
ii  tcpd                                           7.6.q-26                     armhf                        Wietse Venema's TCP wrapper utilities
ii  tcptraceroute                                  1.5beta7+debian-4            armhf                        traceroute implementation using TCP packets
ii  traceroute                                     1:2.1.0-2                    armhf                        Traces the route taken by packets over an IPv4/IPv6 network
ii  triggerhappy                                   0.5.0-1                      armhf                        global hotkey daemon for Linux
ii  tshark                                         2.6.8-1.1~deb9u1             armhf                        network traffic analyzer - console version
ii  tzdata                                         2020e-0+deb9u1               all                          time zone and daylight-saving time data
ii  ucf                                            3.0036                       all                          Update Configuration File(s): preserve user changes to config files
ii  udev                                           232-25+deb9u12               armhf                        /dev/ and hotplug management daemon
ii  unzip                                          6.0-21+deb9u2                armhf                        De-archiver for .zip files
ii  usb-modeswitch                                 2.5.0+repack0-1              armhf                        mode switching tool for controlling "flip flop" USB devices
ii  usb-modeswitch-data                            20170120-1                   all                          mode switching data for usb-modeswitch
ii  usbutils                                       1:007-4+deb9u1               armhf                        Linux USB utilities
ii  util-linux                                     2.29.2-1+deb9u1              armhf                        miscellaneous system utilities
ii  v4l-utils                                      1.12.3-1                     armhf                        Collection of command line video4linux utilities
ii  va-driver-all:armhf                            1.7.3-2                      armhf                        Video Acceleration (VA) API -- driver metapackage
ii  vdpau-driver-all:armhf                         1.1.1-6                      armhf                        Video Decode and Presentation API for Unix (driver metapackage)
ii  vim                                            2:8.0.0197-4+deb9u3          armhf                        Vi IMproved - enhanced vi editor
ii  vim-common                                     2:8.0.0197-4+deb9u3          all                          Vi IMproved - Common files
ii  vim-runtime                                    2:8.0.0197-4+deb9u3          all                          Vi IMproved - Runtime files
ii  vim-tiny                                       2:8.0.0197-4+deb9u3          armhf                        Vi IMproved - enhanced vi editor - compact version
ii  vlc                                            3.0.12-0+deb9u1              armhf                        multimedia player and streamer
ii  vlc-bin                                        3.0.12-0+deb9u1              armhf                        binaries from VLC
ii  vlc-data                                       3.0.12-0+deb9u1              all                          Common data for VLC
ii  vlc-l10n                                       3.0.12-0+deb9u1              all                          Translations for VLC
ii  vlc-plugin-base:armhf                          3.0.12-0+deb9u1              armhf                        multimedia player and streamer (base plugins)
ii  vlc-plugin-notify:armhf                        3.0.12-0+deb9u1              armhf                        LibNotify plugin for VLC
ii  vlc-plugin-qt:armhf                            3.0.12-0+deb9u1              armhf                        multimedia player and streamer (Qt plugin)
ii  vlc-plugin-samba:armhf                         3.0.12-0+deb9u1              armhf                        Samba plugin for VLC
ii  vlc-plugin-skins2:armhf                        3.0.12-0+deb9u1              armhf                        multimedia player and streamer (Skins2 plugin)
ii  vlc-plugin-video-output:armhf                  3.0.12-0+deb9u1              armhf                        multimedia player and streamer (video output plugins)
ii  vlc-plugin-video-splitter:armhf                3.0.12-0+deb9u1              armhf                        multimedia player and streamer (video splitter plugins)
ii  vlc-plugin-visualization:armhf                 3.0.12-0+deb9u1              armhf                        multimedia player and streamer (visualization plugins)
ii  wget                                           1.18-5+deb9u3                armhf                        retrieves files from the web
ii  whiptail                                       0.52.19-1                    armhf                        Displays user-friendly dialog boxes from shell scripts
ii  wireless-regdb                                 2018.05.09-0~rpt1            all                          wireless regulatory database
ii  wireless-tools                                 30~pre9-12                   armhf                        Tools for manipulating Linux Wireless Extensions
ii  wireshark-common                               2.6.8-1.1~deb9u1             armhf                        network traffic analyzer - common files
ii  wpasupplicant                                  2:2.6-21~bpo9~rpt1           armhf                        client support for WPA and WPA2 (IEEE 802.11i)
ii  x11-common                                     1:7.7+19                     all                          X Window System (X.Org) infrastructure
ii  x11-utils                                      7.7+3                        armhf                        X11 utilities
ii  x11-xserver-utils                              7.7+7                        armhf                        X server utilities
ii  xauth                                          1:1.0.9-1                    armhf                        X authentication utility
ii  xdg-user-dirs                                  0.15-2                       armhf                        tool to manage well known user directories
ii  xdg-utils                                      1.1.1-1+deb9u2               all                          desktop integration utilities from freedesktop.org
ii  xkb-data                                       2.19-1+deb9u1                all                          X Keyboard Extension (XKB) configuration data
ii  xml-core                                       0.17                         all                          XML infrastructure and XML catalog file support
ii  xxd                                            2:8.0.0197-4+deb9u3          armhf                        tool to make (or reverse) a hex dump
ii  xz-utils                                       5.2.2-1.2                    armhf                        XZ-format compression utilities
ii  zlib1g:armhf                                   1:1.2.8.dfsg-5               armhf                        compression library - runtime
ii  zlib1g-dev:armhf                               1:1.2.8.dfsg-5               armhf                        compression library - development
```

## PIP3 Packages (user installed)
```
flux-led (0.24.11)
webcolors (1.11.1)
```

# PIP3 Packages (root installed)
```
chardet (2.3.0)
cryptography (1.7.1)
idna (2.2)
keyring (10.1)
keyrings.alt (1.3)
pip (9.0.1)
pyasn1 (0.1.9)
pycrypto (2.6.1)
pygobject (3.22.0)
python-apt (1.4.3)
python-lirc (1.2.1)
pyxdg (0.25)
PyYAML (3.12)
requests (2.12.4)
SecretStorage (2.3.1)
setuptools (33.1.1)
six (1.12.0)
ssh-import-id (5.6)
urllib3 (1.19.1)
wheel (0.29.0)
```

## `/boot/config.txt`
```
dtparam=i2c_arm=on
dtparam=spi=on
gpu_mem=8
start_x=0
enable_uart=1
dtoverlay=hifiberry-dac
dtoverlay=i2s-mmap
```
