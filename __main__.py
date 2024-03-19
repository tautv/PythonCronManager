from crontab import CronTab

# Get the current user's crontab
cron = CronTab(user=True)

# List all existing cron jobs
print("Existing cron jobs:")
for job in cron:
    print(job)

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
