import unittest

from src.utils.cron_command_parse import join_cron_command


class TestJoinCronCommand(unittest.TestCase):
    def test_basic_command(self):
        command = "ls"
        output_redirect = ""
        output_file = ""
        error_redirect = ""
        error_file = ""
        expected_output = "ls"
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)

        command = "mv /var/log/application.log /var/log/application.log.$(date +\%Y\%m\%d) && touch /var/log/application.log"  # noqa
        output_redirect = ""
        output_file = ""
        error_redirect = ""
        error_file = ""
        expected_output = "mv /var/log/application.log /var/log/application.log.$(date +\%Y\%m\%d) && touch /var/log/application.log"  # noqa
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)

    def test_output_redirect(self):
        command = "ls"
        output_redirect = ">"
        output_file = "out.txt"
        error_redirect = ""
        error_file = ""
        expected_output = "ls > out.txt"
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)

        command = "pg_dump -U username dbname | gzip"
        output_redirect = ">"
        output_file = "/backup/location/$(date +\%Y\%m\%d\%H\%M\%S)_backup.sql.gz"  # noqa
        error_redirect = ""
        error_file = ""
        expected_output = "pg_dump -U username dbname | gzip > /backup/location/$(date +\%Y\%m\%d\%H\%M\%S)_backup.sql.gz"  # noqa
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)

    def test_error_redirect(self):
        command = "ls"
        output_redirect = ""
        output_file = ""
        error_redirect = "2>"
        error_file = "error.txt"
        expected_output = "ls 2> error.txt"
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)

    def test_output_and_error_redirect(self):
        command = "ls"
        output_redirect = ">"
        output_file = "out.txt"
        error_redirect = "2>"
        error_file = "error.txt"
        expected_output = "ls > out.txt 2> error.txt"
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)

    def test_append_output_redirect(self):
        command = "ls"
        output_redirect = ">>"
        output_file = "out.txt"
        error_redirect = ""
        error_file = ""
        expected_output = "ls >> out.txt"
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)

    def test_append_error_redirect(self):
        command = "ls"
        output_redirect = ""
        output_file = ""
        error_redirect = "2>>"
        error_file = "error.txt"
        expected_output = "ls 2>> error.txt"
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)

    def test_append_output_and_error_redirect(self):
        command = "ls"
        output_redirect = ">>"
        output_file = "out.txt"
        error_redirect = "2>>"
        error_file = "error.txt"
        expected_output = "ls >> out.txt 2>> error.txt"
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)

        command = "pip --version"
        output_redirect = ">"
        output_file = "out.txt"
        error_redirect = "2>"
        error_file = '"$1"'
        expected_output = "pip --version > out.txt 2> \"$1\""
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)

    def test_error_redirect_to_output(self):
        command = '/bin/bash -c "echo Test!"'
        output_redirect = ''
        output_file = ''
        error_redirect = '2>>'
        error_file = '&1'
        expected_output = '/bin/bash -c "echo Test!" 2>>&1'
        self.assertEqual(join_cron_command(command, output_redirect, output_file, error_redirect, error_file),
                         expected_output)


if __name__ == '__main__':
    unittest.main()
