import yaml


def parse_playbook(playbook_file):
    with open(playbook_file, "r") as file:
        playbook = yaml.safe_load(file)
    return playbook


def parse_hosts(hosts_file):
    hosts = {}
    with open(hosts_file, "r") as file:
        for line in file:
            if line.strip() == "":
                continue
            if line.startswith("["):
                current_group = line.strip()[1:-1]
                hosts[current_group] = []
            else:
                hosts[current_group].append(line.strip())
    return hosts
