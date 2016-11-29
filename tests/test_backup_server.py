import os
import pytest

class TestIATIBackupServer():

    def test_ping(self):
        """
        Test that the server can be pinged. This indicates that it is
        at least online
        """
        server_address = "83.170.85.222"

        result = os.system("ping -c 1 {}".format(server_address))

        assert result == 0  # 0 indicates the network is active
