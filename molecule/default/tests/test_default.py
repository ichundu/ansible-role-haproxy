import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_haproxy_is_installed(host):
    pkg = host.package('haproxy')
    assert pkg.is_installed


def test_haproxy_conf_file(host):
    f = host.file('/etc/haproxy/haproxy.cfg')
    assert f.exists


def test_haproxy_running_and_enabled(host):
    svc = host.service('haproxy')
    assert svc.is_running
    assert svc.is_enabled


def test_haproxy_rsyslog_file(host):
    f = host.file('/etc/rsyslog.d/haproxy.conf')
    assert f.exists


def test_rsyslog_running_and_enabled(host):
    svc = host.service('rsyslog')
    assert svc.is_running
    assert svc.is_enabled


def test_haproxy_logrotate_file(host):
    f = host.file('/etc/logrotate.d/haproxy')
    assert f.exists
