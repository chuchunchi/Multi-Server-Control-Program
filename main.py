from src import file_parser
from src import host_controller

PLAYBOOK_FILE = "playbook.yaml"
HOSTS_FILE = "example_hosts_file"

def main():
    playbook = file_parser.parse_playbook(PLAYBOOK_FILE)
    hosts = file_parser.parse_hosts(HOSTS_FILE)
    # print(playbook)
    # print(hosts)

    for cmd in playbook:
        for host in hosts[cmd["hosts"]]:
            print(f"Executing command on {host}")
            ssh = host_controller.connect_to_host(host)
            for task in cmd["tasks"]:
                host_controller.execute_command(ssh, task["bash"])


if __name__ == "__main__":
    main()