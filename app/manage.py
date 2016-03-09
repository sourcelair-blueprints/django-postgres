#!/usr/bin/env python
import os
import subprocess
import sys

if __name__ == "__main__":
    if os.getenv('SL_ENV'):
        try:
            # Attempt to create the database every time this script
            # gets invoked, if run on SourceLair
            out = subprocess.check_output(
                ["../bin/db-create"],
                stderr=subprocess.STDOUT,
            )
        except Exception as e:
            pass

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
