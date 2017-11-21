# ansible-lxc-over-ssh

Plugin for LXC containers control on remote servers

## Description

This version based on [chifflier/ansible-lxc-ssh](/chifflier/ansible-lxc-ssh) idea.
Insead copy this version just extends standart conntection/ssh module.
Worked on Ansible 2.4

## Configuration

Add to `ansible.cfg`:
```
[defaults]
connection_plugins = <path_to_plugin_folder>
```

Then, modify your `hosts`:
```
container ansible_host=server:container ansible_connection=lxc_over_ssh
```
