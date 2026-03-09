from src import file_parser

PLAYBOOK_FILE = "example_playbook.yaml"
HOSTS_FILE = "example_hosts_file"

playbook = file_parser.parse_playbook(PLAYBOOK_FILE)
hosts = file_parser.parse_hosts(HOSTS_FILE)

print(playbook)
print(hosts)