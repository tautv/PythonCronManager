Simple GUI for crontab.
Mainly made for Mac in mind.

Some resources:
https://www.adminschoice.com/crontab-quick-reference




## TODOs:

### Custom logging type for success/failure tracking:

```cronexp
* * * * * /path/to/my_script.sh >/dev/null 2>&1 && touch /path/to/success.txt || touch /path/to/error.txt
```

### Invalid?
2>>&1 is not valid?
2>&1 works as overwrite
2>>&1 