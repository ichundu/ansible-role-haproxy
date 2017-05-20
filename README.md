Role Name: HAProxy
==================


[![Build Status](https://travis-ci.org/ichundu/ansible-role-haproxy.svg?branch=master)](https://travis-ci.org/ichundu/ansible-role-haproxy.svg?branch=master)

This role installs and configures HAProxy on RedHat family systems. The configuration is the default provided with HAProxy when installed, which can be customized as needed. Also logging is enabled for HAProxy via rsyslog.

Requirements
------------

None.

Role Variables
--------------

Variables in `defaults/main.yml` mainly contain sections for configuring HAProxy, devided in groups: `haproxy_global`, `haproxy_defaults`, `haproxy_frontend`, `haproxy_backend_static` and `haproxy_backends`:

|	Variable name	|	Description	|
|-------------------|---------------|
| `haproxy_global` | Configuration options for the 'global' section |
| `haproxy_defaults` | Configuration options for the 'defaults' section |
| `haproxy_frontend` | Configuration options for the 'frontend' section |
| `haproxy_backend_static` | Configuration options for the 'static backend' section |
| `haproxy_backends` | Configuration options for the 'backend' section |
| `haproxy_log_file` | Path to the file where HAProxy logs are stored |

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
