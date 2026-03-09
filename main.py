from src import file_parser
from src import host_controller
from concurrent.futures import ThreadPoolExecutor, as_completed

PLAYBOOK_FILE = "playbook.yaml"
HOSTS_FILE = "example_hosts_file"

def main():
    playbook = file_parser.parse_playbook(PLAYBOOK_FILE)
    hosts = file_parser.parse_hosts(HOSTS_FILE)
    # print(playbook)
    # print(hosts)

    with ThreadPoolExecutor(max_workers=10) as executor:
        works_queue = []
        for cmd in playbook:
            for host in hosts[cmd["hosts"]]:
                works_queue.append(executor.submit(host_controller.connect_and_execute_commands, host, cmd["tasks"]))
        for work in as_completed(works_queue):
            work.result()
    executor.shutdown(wait=True)

if __name__ == "__main__":
    main()