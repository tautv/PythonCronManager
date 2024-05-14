# To test this can go to: https://regexr.com/
import re


def split_cron_command(command):
    # Regular expression pattern to match command + output redirect and error redirect
    # Don't mess this up. it works really well right now:
    # pattern = r'(.+?)\s*(?:(>[>]?|2>[>]?)(.+?))?\s*(?:(2>[>]?)(.+?))?$'

    # Slightly updated, to not lump error red into output red, if output red is not given!:
    pattern = r'(.+?)\s*(?:(>[>]?)(.+?))?\s*(?:(2>[>]?)(.+?))?$'
    # pattern = r'(.+?)\s*(?:(>[>]?)(.+?))?\s*(?:(2>[>]?)(.+?))?$'

    match = re.match(pattern, command)
    if match:
        groups = match.groups()
        cmd = groups[0].strip()
        output_redirect = groups[1]
        output_file = groups[2]
        error_redirect = groups[3]
        error_file = groups[4]

        # If no output redirect is specified, set defaults
        if output_redirect is None:
            output_redirect = ''
            output_file = ''

        # If no error redirect is specified, set defaults
        if error_redirect is None:
            error_redirect = ''
            error_file = ''

        return cmd, output_redirect.strip(), output_file.strip(), error_redirect.strip(), error_file.strip()
        # Changed from non stripped version:
        # return cmd, output_redirect.strip(), output_file, error_redirect, error_file
    else:
        return None
