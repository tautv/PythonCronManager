from crontab import CronTab

# Get the current user's crontab
cron = CronTab(user=True)

# List all existing cron jobs
print("Existing cron jobs:")
for job in cron:
    print('=' * len(job))
    print(job)
    print(f"\tMinutes:\t{job.minutes}")
    print(f"\tHour:\t{job.hours}")
    print(f"\tDay:\t{job.day}")
    print(f"\tMonth:\t{job.months}")
    print(f"\tDow:\t{job.dow}")
    print(f"\tCommand:\t{job.command}")

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
