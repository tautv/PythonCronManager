import re


def split_cron_command(command):
    """
        Splits a cron command string into its constituent parts.

        Args:
            command (str): The cron command string to split.

        Returns:
            tuple: A tuple containing the command and its redirection settings.
                - cmd (str): The main command.
                - output_redirect (str): The output redirection operator ('>', '>>', or '').
                - output_file (str): The file to redirect standard output to, if any.
                - error_redirect (str): The error redirection operator ('2>', '2>>', or '').
                - error_file (str): The file to redirect standard error to, if any.

        Note:
            This function expects a cron command string in the following format:
            'command > output_file 2> error_file', where:
                - 'command' is the main command to execute.
                - '> output_file' redirects standard output to 'output_file'.
                - '2> error_file' redirects standard error to 'error_file'.
            If output or error redirection is not specified, the corresponding
            operator and file will be set to empty strings.

        Example:
            >> split_cron_command('ls > out.txt 2> err.txt')
            ('ls', '>', 'out.txt', '2>', 'err.txt')
    """
    # Regular expression pattern to match command + output redirect and error redirect
    # pattern = r'(.+?)\s*(?:(>[>]?)(.+?))?\s*(?:(2>[>]?)(.+?))?$'

    pattern = r'(.+?)\s*(?:(>[>]?)(.+?))?\s*(?:(2>[>]?)(.+?))?$'

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

        return cmd, output_redirect.strip(), output_file.strip(), error_redirect.strip(), error_file.strip()
    else:
        return None


def join_cron_command(command, output_redirect, output_file, error_redirect, error_file):
    """
    Joins the constituent parts of a cron command into a single string.

    Args:
        command (str): The main command.
        output_redirect (str): The output redirection operator ('>', '>>', or '').
        output_file (str): The file to redirect standard output to, if any.
        error_redirect (str): The error redirection operator ('2>', '2>>', or '').
        error_file (str): The file to redirect standard error to, if any.

    Returns:
        str: The joined cron command string.

    Example:
        >> join_cron_command('ls', '>', 'out.txt', '2>', 'err.txt')
        'ls > out.txt 2> err.txt'
    """
    # Join the command and its redirection settings into a single string
    cron_command = command
    if output_redirect:
        cron_command += f" {output_redirect} {output_file}"
    if error_redirect:
        cron_command += f" {error_redirect} {error_file}"
    return cron_command.strip()
