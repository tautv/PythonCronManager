from crontab import CronTab

cron = CronTab(user=True)

# Get the current user's crontab

# List all existing cron jobs
# print("Existing cron jobs:")
# for job in cron:
#     print('=' * len(str(job)))
#     print(job)
#     print(f"\tMinutes:\t{job.minutes}")
#     print(f"\tHour:\t\t{job.hours}")
#     print(f"\tDay:\t\t{job.day}")
#     print(f"\tMonth:\t\t{job.months}")
#     print(f"\tDow:\t\t{job.dow}")
#     print(f"\tCommand:\t{job.command}")
#     print(f"\tUser:\t\t{job.user}")
#     print(f"\tComment:\t{job.comment}")
#     print(f"\tEnabled:\t{job.enabled}")
#     print(f"\tSpecial:\t{job.special}")
#     print(f"\tLast Run:\t{job.last_run}")
#     print(f"\tEnvironment:\t{job.env}")
#     print(f"\tPre-Comment:\t{job.pre_comment}")
#     print(f"\tMarker:\t\t{job.marker}")
#     print(f"\tStandard Input:\t{job.stdin}")
#     print(f"\tLog:\t\t{job._log}")

# # Add a new cron job
# new_job = cron.new(command='/path/to/your/command', comment='Your comment here')
# new_job.minute.on(0)
# new_job.hour.on(12)
#
# # Write the new job to crontab
# cron.write()

# Remove a specific cron job (if needed)
# for job in cron:
#     if job.comment == 'Your comment here':
#         cron.remove(job)
#         cron.write()

# print("New cron job added.")
