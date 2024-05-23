from crontab import CronTab


class CronJob:
    def __init__(self, enabled=True, cron_command="", output_type="Cron Default", output_file_path="",
                 error_type="Cron Default", error_file_path=""):
        # Dataview dependent structure:
        self.enabled = enabled
        self.cron_command = cron_command
        self.output_type = output_type
        self.output_file_path = output_file_path
        self.error_type = error_type
        self.error_file_path = error_file_path
        # CronTab structure:
        self.default_minutes = 0
        self.default_hours = 0
        self.default_days = 1
        self.default_months = 1
        self.default_dow = 0  # 0 = Sunday, 1 = Monday...
        self.default_comment = ""
        self.default_command = ""


class CronManager:
    def __init__(self, user=True):
        self.cron = CronTab(user=user)
        self.cron_jobs = []
        self.get_all_cron_jobs()

    def add_cron_job(self, cron_job):
        pass

    def update_cron_job(self, cron_job):
        pass

    def delete_cron_job(self, cron_job):
        pass

    def get_all_cron_jobs(self):
        pass


# c = CronManager()
# job = c.cron.new(command="/bin/bash -c /Users/your_user_name/cronish/job.sh")
# job.setall('* * * * *')
# c.cron.write()
