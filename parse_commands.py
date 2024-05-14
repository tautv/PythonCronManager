# To test this can go to: https://regexr.com/
import re

example_1 = "0 2 * * * pg_dump -U username dbname | gzip > /backup/location/$(date +\%Y\%m\%d\%H\%M\%S)_backup.sql.gz"
example_2 = "0 0 * * 0 mv /var/log/application.log /var/log/application.log.$(date +\%Y\%m\%d) && touch /var/log/application.log"
example_3 = "30 3 * * * find /tmp -type f -name \"tempfile*\" -mtime +7 -exec rm {} \;"
example_4 = "0 4 * * * rsync -avz --delete /var/www/html/ user@example.com:/var/www/backup/"
example_5 = "*/5 * * * * /usr/bin/top -n 1 -b | /usr/bin/head -n 10 >> /var/log/resource_usage.log"
example_6 = "0 2 * * * pg_dump -U username dbname > /backup/location/backup_$(date +\%Y\%m\%d\%H\%M\%S).sql 2>/backup/location/backup_error_$(date +\%Y\%m\%d\%H\%M\%S).log"
example_7 = "0 0 * * 0 mv /var/log/application.log /var/log/application.log.$(date +\%Y\%m\%d) > /var/log/log_rotation_$(date +\%Y\%m\%d).log 2>/var/log/log_rotation_error_$(date +\%Y\%m\%d).log && touch /var/log/application.log"
example_8 = "/usr/bin/top -n 1 -b > /var/log/resource_usage_$(date +\%Y\%m\%d\%H\%M\%S).log 2>/var/log/resource_usage_error_$(date +\%Y\%m\%d\%H\%M\%S).log"
example_9 = '/bin/bash -c "/path/to/command" > "/path/to/output_and_error.log" 2>&1'
example_10 = '/bin/bash -c "/path/to/command"'
example_11 = '/bin/bash -c "/path/to/command" 2>&1'

all_examples = [example_1, example_2, example_3, example_4, example_5, example_6, example_7, example_8, example_9,
                example_10, example_11]


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

        return cmd, output_redirect, output_file, error_redirect, error_file
    else:
        return None


# Example usage
for command in all_examples:
    parsed = split_cron_command(command)
    print('==============')
    print("Command", command)
    print("Command P:", parsed[0])
    print("Output symbol:", parsed[1])
    print("Output Redirect:", parsed[2])
    print("Error symbol:", parsed[3])
    print("Error Redirect:", parsed[4])
