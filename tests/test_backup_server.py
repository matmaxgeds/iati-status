from datetime import datetime, timedelta, timezone
import os
import pytest
import paramiko
from paramiko.ssh_exception import AuthenticationException, SSHException, BadHostKeyException
import re

class TestIATIBackupServer:

    @classmethod
    def setup_class(self):
        """
        Create a SSH client for use by test methods.
        Login credentials are stored as environment variables.
        """
        hostname = os.environ["backup_server_hostname"]
        username = os.environ["backup_server_username"]
        password = os.environ["backup_server_password"]

        try:
            self.client = paramiko.SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(
                paramiko.AutoAddPolicy()
                )
            self.client.connect(hostname, username=username, password=password, timeout=5)
        except AuthenticationException:
            print("Authentication failed, please verify your credentials: %s")
        except SSHException as sshException:
            print("Unable to establish SSH connection: %s" % sshException)
        except BadHostKeyException as badHostKeyException:
            print("Unable to verify server's host key: %s" % badHostKeyException)
        except Exception as e:
            print("Operation error: %s" % e)

    def test_ping(self):
        """
        Test that the server can be pinged. This indicates that it is
        at least online
        """
        server_address = "83.170.85.222"

        result = os.system("ping -c 1 {}".format(server_address))

        assert result == 0  # 0 indicates the network is active

    def _get_directory_contents(self, dir_path):
        """
        Returns a dictionary of files/directories present within a given directory
        path.

        Input:
          dir_path -- Path to to directory

        Returns:
          Dictionary with file/directory name as key, then dictionary containing
          filesizes (in bytes) and last modified time as a datetime object.

          Returns None if no file/directory present.
        """
        stdin, stdout, stderr = self.client.exec_command(
            "find {} -maxdepth 1 -print0 | xargs -0 stat -c '%y %s %n' | perl -pe 'chomp if eof'".format(dir_path)
            )
        stdout_unicode = stdout.read().decode('utf-8')
        stdout_lines = stdout_unicode.split("\n")

        if len(stdout_lines) > 0:
            output = dict()
            for line in stdout_lines:
                line_parts = line.split(" ")
                relative_path = line_parts[4].replace(dir_path, ".")
                output[relative_path] = {
                    "last_modified": datetime.strptime(
                        "{} {} {}".format(line_parts[0], line_parts[1][0:15], line_parts[2]),
                        '%Y-%m-%d %H:%M:%S.%f %z'
                        ),
                    "filesize": int(line_parts[3])
                    }
            return output
        else:
            return None

    def test_github_backups_made(self):
        """
        Tests that Github backups have been made in the expected way - i.e.
        - There are at least 115 files present
        - Every file is greater than 0 bytes
        - All files have been modified (i.e. updated) the past day
        """
        datetime_yesterday = datetime.now(timezone.utc) - timedelta(days=1)
        github_backups = self._get_directory_contents("/home/backups/backup-github/github-backups")

        github_backups_filesizes = [v['filesize'] for v in github_backups.values()]
        github_backups_last_modified_dates =  [v['last_modified'] for v in github_backups.values()]
        smallest_backup_filesize = min(github_backups_filesizes)
        oldest_last_modified_date = min(github_backups_last_modified_dates)

        assert len(github_backups) >= 115
        assert smallest_backup_filesize > 0
        #TODO Check behaviour of backup script, so that following test is reliable
        # assert oldest_last_modified_date > datetime_yesterday

    def test_csv2iati_backup_made_daily(self):
        """
        Tests that a csv2iati backups has been made within the past 24 hours, and
        that this file has:
        - a filesize greater than 0 bytes
        - a filename matching a regex pattern (which defines the expected filename)

        #TODO Possibly refactor (if appropriate, so that this test uses
            self._get_directory_contents
        """
        stdin, stdout, stderr = self.client.exec_command(
            "find /home/backups/csv2iati -maxdepth 1 -type f -mtime -1 -print0 | xargs -0 du -b | xargs echo -n"
            )
        stdout_unicode = stdout.read().decode('utf-8')
        filesize_str, filename = stdout_unicode.split(" ")

        filesize = int(filesize_str)
        result = re.search(r"\d{4}-\d{2}-\d{2}.sqlite", filename)  # Returns True is the regex pattern is found in the filename

        assert filesize > 0
        assert result

    def test_at_least_1GB_disk_space_available(self):
        """
        Test that there is sufficient space available for future backups.
        Filters the output of 'df' to return the KBs available to the server's main disk.
        """

        stdin, stdout, stderr = self.client.exec_command("df /dev/xvda1 | awk '{print $4}' | sed -n 2p | xargs echo -n")

        disk_space_available = int(stdout.read())

        assert disk_space_available > 1000000  # 1000000KB ~ 1GB
