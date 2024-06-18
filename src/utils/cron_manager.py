from typing import List
from crontab import CronTab
from src.utils.cron_command_parse import split_cron_command, join_cron_command

DEFAULT_OUTPUT_CHOICES = ['Cron Default',  # Cron default behavior
                          'None',  # /dev/null
                          'Write To File',  # > write
                          'Append To File']  # >> append
DEFAULT_ERROR_CHOICES = ['Cron Default',  # Cron default behavior
                         'None',  # /dev/null
                         'Write To File',  # > write
                         'Append To File',  # >> append
                         'To Output File']  # &1


class CronJob:
    def __init__(self, enabled=True, cron_command="", output_type="", output_file_path="",
                 error_type="", error_file_path=""):
        # UI essentials
        self.enabled = enabled
        self.cron_command_unparsed = ''
        self.cron_command = cron_command
        self.output_type = output_type
        self.output_type_parsed = ''
        self.output_file_path = output_file_path
        self.error_type = error_type
        self.error_type_parsed = ''
        self.error_file_path = error_file_path
        # CronTab structure:
        self.default_minutes = '*'
        self.default_hours = '*'
        self.default_days = '*'
        self.default_months = '*'
        self.default_dow = '*'  # 0 = Sunday, 1 = Monday...
        self.default_comment = "This is a default comment!"
        # Other

    def parse_command(self):
        if self.cron_command_unparsed:
            (self.cron_command,
             _output_type,
             self.output_file_path,
             _error_type,
             self.error_file_path) = split_cron_command(self.cron_command_unparsed)
            # Output Type Parse:
            if _output_type == '':
                self.output_type_parsed = DEFAULT_OUTPUT_CHOICES[0]  # Cron Default
                self.output_type = _output_type
            if _output_type == '>':
                self.output_type_parsed = DEFAULT_OUTPUT_CHOICES[2]  # Write To File
                self.output_type = _output_type
            if _output_type == '>>':
                self.output_type_parsed = DEFAULT_OUTPUT_CHOICES[3]  # Append To File
                self.output_type = _output_type
            if self.output_file_path == '/dev/null':
                self.output_type_parsed = DEFAULT_OUTPUT_CHOICES[1]  # None
            # Error Type Parse:
            if _error_type == '':
                self.error_type_parsed = DEFAULT_ERROR_CHOICES[0]  # Cron Default
                self.error_type = _error_type
            if _error_type == '2>':
                self.error_type_parsed = DEFAULT_ERROR_CHOICES[2]  # Write To File
                self.error_type = _error_type
            if _error_type == '2>>':
                self.error_type_parsed = DEFAULT_ERROR_CHOICES[3]  # Append To File
                self.error_type = _error_type
            if self.error_file_path == '/dev/null':
                self.error_type_parsed = DEFAULT_ERROR_CHOICES[1]  # None
            if self.error_file_path == '&1':
                self.error_type_parsed = DEFAULT_ERROR_CHOICES[4]  # To Output File


class CronManager:
    def __init__(self, user=True):
        self.user = user
        self.cron = None
        self.cron_jobs = []
        self.read_cron_jobs()

    def add_cron_job(self, cron_job):
        if self.cron is not None:
            _command = join_cron_command(cron_job.cron_command,
                                         cron_job.output_type,
                                         cron_job.output_file_path,
                                         cron_job.error_type,
                                         cron_job.error_file_path)
            cron_job.cron_command_unparsed = _command
            new_job = self.cron.new(
                command=_command,
                comment=cron_job.default_comment,
                user=self.user
            )

            # TODO: Crontab needs timing parsed:
            #   Should be parsed from _command,
            #   then translated to the below:

            # Set timing attributes
            new_job.setall(
                cron_job.default_minutes,
                cron_job.default_hours,
                cron_job.default_days,
                cron_job.default_months,
                cron_job.default_dow
            )

            # Save the cron job
            self.cron.write()

            # Append the cron job object to the list
            self.cron_jobs.append(cron_job)

    def update_cron_job(self, cron_job):
        pass

    def delete_cron_job(self, cron_job):
        pass

    def get_all_cron_jobs(self) -> List[CronJob]:
        if self.cron:
            return self.cron_jobs
        return []

    def read_cron_jobs(self):
        self.cron = CronTab(user=self.user)
        self.cron_jobs = []
        if self.cron is not None:
            for job in self.cron.crons:
                cb = CronJob()
                cb.enabled = job.enabled
                cb.cron_command_unparsed = job.command
                cb.parse_command()
                cb.default_minutes = job.minutes
                cb.default_hours = job.hours
                cb.default_days = job.day
                cb.default_months = job.months
                cb.default_dow = job.dow
                cb.default_comment = job.comment
                self.cron_jobs.append(cb)


if __name__ == '__main__':
    cm = CronManager()
    # ncj = CronJob(cron_command="/bin/bash -c \"echo Test\"")
    # ncj.enabled = False
    # ncj.output_type = '>>'
    # ncj.output_file_path = '~/Desktop/output.txt'
    # ncj.error_type = '2>>'
    # ncj.error_file_path = '&1'
    # cm.add_cron_job(ncj)

    for _job in cm.cron_jobs:
        _job.parse_command()
        for key, value in _job.__dict__.items():
            print(f"[{key}]\t\t\t\t\t{value}")
        print(join_cron_command(_job.cron_command, _job.output_type, _job.output_file_path, _job.error_type,
                                _job.error_file_path))
    cj = CronJob()
    cj.cron_command_unparsed = '* * * * * /bin/bash -c "echo Test" > ~/Desktop/test.txt'
    cj.parse_command()
    cm.add_cron_job(cj)
