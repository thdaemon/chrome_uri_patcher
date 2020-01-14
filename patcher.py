#!/usr/bin/env python3

import sys
import json
import shutil

extension_string = """
      {
        "active_permissions": {
          "api": [
          ],
          "manifest_permissions": []
        },
        "commands": {},
        "content_settings": [],
        "creation_flags": 9,
        "events": [
        ],
        "extension_can_script_all_urls": false,
        "from_bookmark": false,
        "from_webstore": false,
        "granted_permissions": {
          "api": [
          ],
          "explicit_host": [
          ],
          "manifest_permissions": []
        },
        "incognito": true,
        "incognito_content_settings": [],
        "incognito_preferences": {},
        "install_time": "13213341138196510",
        "last_activated_ime_engine": false,
        "lastpingday": "13220524801107624",
        "location": 1,
        "manifest": {
          "description": "Dummy extension for showing scheme:// and www in URI",
          "icons": {
            "128": "images/orangeflag128.png",
            "16": "images/orangeflag16.png",
            "48": "images/orangeflag48.png"
          },
          "key": "MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAowA8wOUQ8ShyITJ15B9rcJrnoolyo+OLj07g8QWBlEBikgszYwlbc88OIRL+dJOASok3yG6RQ60fvIjBrtNEk1yQZJfNwF/CN0jFrkE3HN3xVMoX0XIQPB93kDZARcfR5nwU3RUgwwWGTqt69KSSU8QzRRQJSEgM8GENa3OBhw1UBn/I/RbhaFcTykJSomo9j55goJwNzUhXTJk458DQ5diY+gWMadDXlDBa8cciCVlaGOjBV5ezmxnD6p1GXhrvyEKZP8IlreDJC2Nw9hxrT3GIo1FzbmeDPANKJ9pkY1H3LOVsGJDtytBpD/FRErlvfkJVqp3N5ifF2EQ8lOAHrQIDAQAB",
          "manifest_version": 2,
          "name": "URI Guard",
          "permissions": [
          ],
          "update_url": "x-scheme-chrome-extension-uriguard://disable_auto_upgrade",
          "version": "0.1"
        },
        "needs_sync": true,
        "never_activated_since_loaded": true,
        "path": "jknemblkbdhdcpllfgbfekkdciegfboi/",
        "preferences": {},
        "regular_only_preferences": {},
        "runtime_granted_permissions": {
          "api": [],
          "manifest_permissions": []
        },
        "state": 1,
        "was_installed_by_default": false,
        "was_installed_by_oem": true
      }
"""

shutil.copyfile(sys.argv[1], "/tmp/chrome_pfile_backup")
print("Preferences has been backup to /tmp/chrome_pfile_backup")

extension = json.loads(extension_string)

print("Loading preferences...")
with open(sys.argv[1]) as pfile:
	pdata = json.load(pfile)

print("Patching preferences...")
pdata["extensions"]["settings"]["jknemblkbdhdcpllfgbfekkdciegfboi"] = extension
with open(sys.argv[1], 'w') as pfile:
	json.dump(pdata, pfile)

