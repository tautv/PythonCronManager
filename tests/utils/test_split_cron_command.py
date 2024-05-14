import unittest
from src.utils.parse_commands import split_cron_command


class TestSplitCronCommand(unittest.TestCase):
    def test_none_cases(self):
        command = ""
        expected_output = None
        self.assertEqual(split_cron_command(command), expected_output)

    def test_basic_command(self):
        command = "mv /var/log/application.log /var/log/application.log.$(date +\%Y\%m\%d) && touch /var/log/application.log"  # noqa
        expected_output = (
        "mv /var/log/application.log /var/log/application.log.$(date +\%Y\%m\%d) && touch /var/log/application.log",
        # noqa
        "", "", "", "")
        self.assertEqual(split_cron_command(command), expected_output)

        command = "rsync -avz --delete /var/www/html/ user@example.com:/var/www/backup/"
        expected_output = ("rsync -avz --delete /var/www/html/ user@example.com:/var/www/backup/",
                           "", "", "", "")
        self.assertEqual(split_cron_command(command), expected_output)

        command = "find /tmp -type f -name \"tempfile*\" -mtime +7 -exec rm {} \;"  # noqa
        expected_output = ("find /tmp -type f -name \"tempfile*\" -mtime +7 -exec rm {} \;",  # noqa
                           "", "", "", "")
        self.assertEqual(split_cron_command(command), expected_output)

        command = "/bin/bash -c \"/path/to/command\""
        expected_output = ("/bin/bash -c \"/path/to/command\"", "", "", "", "")
        self.assertEqual(split_cron_command(command), expected_output)

        command = '/bin/bash -c "source /path/to/env_vars.sh && /path/to/first_script.sh && /path/to/second_script.sh"'
        expected_output = ('/bin/bash -c "source /path/to/env_vars.sh && /path/to/first_script.sh && /path/to/second_script.sh"',  # noqa
                           "", "", "", "")
        self.assertEqual(split_cron_command(command), expected_output)

    def test_output_redirect(self):
        command = "pg_dump -U username dbname | gzip > /backup/location/$(date +\%Y\%m\%d\%H\%M\%S)_backup.sql.gz"  # noqa
        expected_output = ("pg_dump -U username dbname | gzip",
                           ">",
                           "/backup/location/$(date +\%Y\%m\%d\%H\%M\%S)_backup.sql.gz",  # noqa
                           "", "")
        self.assertEqual(split_cron_command(command), expected_output)

        command = "/usr/bin/top -n 1 -b | /usr/bin/head -n 10 >> /var/log/resource_usage.log"
        expected_output = ("/usr/bin/top -n 1 -b | /usr/bin/head -n 10",
                           ">>",
                           "/var/log/resource_usage.log",
                           "", "")
        self.assertEqual(split_cron_command(command), expected_output)

        command = "/path/to/data_generator.sh | awk '/pattern/{print $2}' | grep -v 'exclude_pattern' >> /path/to/output.txt"  # noqa
        expected_output = ("/path/to/data_generator.sh | awk '/pattern/{print $2}' | grep -v 'exclude_pattern'",
                           ">>",
                           "/path/to/output.txt",
                           "", "")
        self.assertEqual(split_cron_command(command), expected_output)

    def test_error_redirect(self):
        command = "/bin/bash -c \"/path/to/command\" 2>&1"
        expected_output = ("/bin/bash -c \"/path/to/command\"",
                           "",
                           "",
                           "2>",
                           "&1")
        self.assertEqual(split_cron_command(command), expected_output)

    def test_output_and_error_redirect(self):
        command = "pg_dump -U username dbname > /backup/location/backup_$(date +\%Y\%m\%d\%H\%M\%S).sql 2>/backup/location/backup_error_$(date +\%Y\%m\%d\%H\%M\%S).log"  # noqa
        expected_output = ("pg_dump -U username dbname",
                           ">",
                           "/backup/location/backup_$(date +\%Y\%m\%d\%H\%M\%S).sql",  # noqa
                           "2>",
                           "/backup/location/backup_error_$(date +\%Y\%m\%d\%H\%M\%S).log")  # noqa
        self.assertEqual(split_cron_command(command), expected_output)

        command = "mv /var/log/application.log /var/log/application.log.$(date +\%Y\%m\%d) > /var/log/log_rotation_$(date +\%Y\%m\%d).log 2>/var/log/log_rotation_error_$(date +\%Y\%m\%d).log && touch /var/log/application.log"  # noqa
        expected_output = ("mv /var/log/application.log /var/log/application.log.$(date +\%Y\%m\%d)",  # noqa
                           ">",
                           "/var/log/log_rotation_$(date +\%Y\%m\%d).log",
                           "2>",
                           "/var/log/log_rotation_error_$(date +\%Y\%m\%d).log && touch /var/log/application.log")
        self.assertEqual(split_cron_command(command), expected_output)

        command = "/usr/bin/top -n 1 -b > /var/log/resource_usage_$(date +\%Y\%m\%d\%H\%M\%S).log 2>/var/log/resource_usage_error_$(date +\%Y\%m\%d\%H\%M\%S).log"  # noqa
        expected_output = ("/usr/bin/top -n 1 -b",
                           ">",
                           "/var/log/resource_usage_$(date +\%Y\%m\%d\%H\%M\%S).log",  # noqa
                           "2>",
                           "/var/log/resource_usage_error_$(date +\%Y\%m\%d\%H\%M\%S).log")  # noqa
        self.assertEqual(split_cron_command(command), expected_output)

        command = "/bin/bash -c \"/path/to/command\" > \"/path/to/output_and_error.log\" 2>&1"
        expected_output = ("/bin/bash -c \"/path/to/command\"",
                           ">",
                           "\"/path/to/output_and_error.log\"",
                           "2>",
                           "&1")
        self.assertEqual(split_cron_command(command), expected_output)

        command = "/usr/bin/python3 /path/to/script.py > /path/to/logfile.log 2>&1"
        expected_output = ("/usr/bin/python3 /path/to/script.py",
                           ">",
                           "/path/to/logfile.log",
                           "2>",
                           "&1")
        self.assertEqual(split_cron_command(command), expected_output)


if __name__ == '__main__':
    unittest.main()
