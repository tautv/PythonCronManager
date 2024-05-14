# TODO:
#   Need to find a way to parse 'command' part from cronjobs:
#   Needs to be split into:
#       Command = 'python /some/path/to/script.py'
#       Output Redirect Symbol = '>' or '>>' or None
#       Output Redirect Path = '/path/to/some/output.log'
#       Error Redirect Symbol = '2>' or '2>>' or None
#       Error Redirect Path = '/some/path/to/error logs.log' or '&1' (for same as output red. path)
