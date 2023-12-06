[app]

# (str) Title of your application
title = Cornish Catch!

# (str) Package name
package.name = cornishcatch

# (str) Package domain (needed for android/ios packaging)
package.domain = org.cornishcatch

# (str) Source files to include (python files, generally)
source.include_exts = py,png,jpg,kv,atlas

# (list) List of inclusions using pattern matching
#source.include_patterns = assets/*,images/*.png

# (list) List of exclusions using pattern matching
#source.exclude_patterns = tests/*, bin/*

# (list) Application requirements
# comma separated e.g. requirements = sqlite3,kivy
requirements = python3,kivy

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
#requirements.source.kivy = ../../kivy

# (list) Garden requirements
#garden_requirements =

# (str) Presplash of the application
#presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
icon.filename = %(source.dir)s/images/Cornish.png

# (str) Supported orientation (one of landscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (string) Presplash background color (for new android toolchain)
#presplash.color = #FFFFFF

# (list) List of service to declare
#services = NAME:ENTRYPOINT_TO_PY,NAME2:ENTRYPOINT2_TO_PY

#
# iOS specific
#

# (str) Path to a custom kivy-ios folder
#ios.kivy_ios_dir = ../kivy-ios
# For iOS deployment, replace with path to your kivy-ios folder

# (bool) Whether to use kivy-ios toolchain for building the ios app
ios.use_kivy_ios = 1

# (str) Name of the certificate to use for signing the debug version
# get a list of available identities: buildozer ios list_identities
#ios.codesign.debug = "iPhone Developer: <lastname> <firstname> (<hexstring>)"

# (str) Name of the certificate to use for signing the release version
#ios.codesign.release = %(ios.codesign.debug)s

[buildozer]

# (int) Android API to use
android.api = 29

# (int) Minimum API required
android.minapi = 21

# (int) Android SDK version to use
android.sdk = 24

# (str) Android NDK version to use
android.ndk = 19b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path =

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path =

# (str) ANT directory (if empty, it will be automatically downloaded.)
#android.ant_path =

# (bool) If True, then skip trying to update the Android sdk
# This can be useful to avoid excess Internet downloads or save time
# when an update is due and you just want to test/build your package
#android.skip_update = False

# (bool) If True, then automatically accept SDK license agreements
# This is useful for automation, but not recommended otherwise
# The accepted Android SDK licenses may not legally represent you.
#android.accept_sdk_license = False

# (str) Android entry point, default is MainActivity
#android.entrypoint = org.renpy.android.PythonActivity

# (str) Android app theme, default is Theme.NoTitleBar
#android.apptheme = @android:style/Theme.NoTitleBar

# (list) Pattern to whitelist for the whole project
#android.whitelist =

# (str) Path to a custom whitelist file
#android.whitelist_src =

# (str) Path to a custom blacklist file
#android.blacklist_src =

# (bool) Use a blacklist instead of a whitelist to select what to include
#android.blacklist = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
android.arch = armeabi-v7a

# (bool) Whether to make the debug apk
#android.build_mode = debug