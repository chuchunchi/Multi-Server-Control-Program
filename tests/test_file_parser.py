from src.file_parser import parse_hosts, parse_playbook


def test_parse_playbook():
    playbook = parse_playbook("example_playbook.yaml")
    assert playbook is not None
    assert len(playbook) > 0
    assert playbook[0]["hosts"] == "dbservers"
    assert playbook[0]["tasks"] is not None
    assert len(playbook[0]["tasks"]) > 0
    assert playbook[0]["tasks"][0]["name"] == "Server uptime"
    assert playbook[0]["tasks"][0]["bash"] == "uptime"


def test_parse_hosts():
    hosts = parse_hosts("example_hosts_file")
    assert hosts is not None
    assert len(hosts) == 2
    assert hosts["dbservers"] is not None
    assert len(hosts["dbservers"]) == 3
    assert hosts["dbservers"][0] == "one.example.com"
