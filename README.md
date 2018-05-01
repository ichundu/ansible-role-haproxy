Role Name: HAProxy
==================

[![Build Status](https://travis-ci.org/ichundu/ansible-role-haproxy.svg?branch=master)](https://travis-ci.org/ichundu/ansible-role-haproxy.svg?branch=master)

This role installs and configures HAProxy on RedHat family systems. The configuration is the default provided with HAProxy when installed, which can be customized as needed. Also logging is enabled for HAProxy via rsyslog.

Requirements
------------

None.

Role Variables
--------------

Variables in `defaults/main.yml`:

|	Variable name	|	Default value | Description	|
|---------------|---------------|-------------|
| `haproxy_logs_dir` | `/var/log/haproxy` | Path to the directory where HAProxy logs are stored |
| `haproxy_log_file` | `{{ haproxy_logs_dir }}/haproxy.log` |HAProxy logfile path |
| `haproxy_syslog_facility` | `local2` | Syslog facility to use, one of `local0` to `local7` |
| `haproxy_stats_socket` | `/var/lib/haproxy/stats level admin` | Unix socket file and commands for HAProxy statistics page |
| `haproxy_stats_uri` | `/haproxy?stats` | URI for HAProxy statistics page |

The HAProxy configuration is parametrized with variable blocks for each section to allow high flexibility in configuration options:

|	Variable name	|	Description	|
|---------------|-------------|
| `haproxy_global` | HAProxy configuration global block |
| `haproxy_defaults` | HAProxy configuration global block |
| `haproxy_frontends` | HAProxy configuration global block |
| `haproxy_backends` | HAProxy configuration global block |
| `haproxy_listen` | HAProxy configuration listen block |

Dependencies
------------

None.

Example Playbook
----------------

```yaml
- hosts: servers
  roles:
     - ichundu.haproxy
```

License
-------

GPLv2

Author Information
------------------

https://github.com/ichundu
