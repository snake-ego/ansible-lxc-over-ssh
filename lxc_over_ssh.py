# SSH + lxc-attach connection module for Ansible 2.0
#
# Extends ansible/plugins/connection/ssh.py
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#

from ansible.plugins.connection.ssh import Connection as SSHConnection


class Connection(SSHConnection):
    transport = 'lxc_over_ssh'

    def __init__(self, play_context, new_stdin, *args, **kwargs):
        super(Connection, self).__init__(play_context, new_stdin, *args, **kwargs)
        self._play_context.ssh_transfer_method = ('piped')
        self.host, self.container = self.host.split(":")

    def exec_command(self, cmd, in_data=None, sudoable=False):
        cmd = 'lxc-attach --elevated-privileges --name {} -- {}'.format(self.container, cmd)
        return super(Connection, self).exec_command(cmd, in_data=in_data, sudoable=sudoable)
