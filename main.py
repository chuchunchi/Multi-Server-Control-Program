from src import file_parser
from src import host_controller
from concurrent.futures import ThreadPoolExecutor, as_completed
import click
from src.config import config_dict

@click.command()
@click.option("--playbook", type=click.Path(exists=True), default="playbook.yaml")
@click.option("--hosts", type=click.Path(exists=True), default="/etc/playbook/hosts")
@click.option("--username", type=str, default=None)
@click.option("--port", type=int, default=None)
def click_main(playbook, hosts, username, port):
    if username is None:
        username = config_dict["username"]
    if port is None:
        port = config_dict["port"]
    playbook = file_parser.parse_playbook(playbook)
    hosts = file_parser.parse_hosts(hosts)

    with ThreadPoolExecutor(max_workers=10) as executor:
        works_queue = []
        for cmd in playbook:
            for host in hosts[cmd["hosts"]]:
                works_queue.append(executor.submit(host_controller.connect_and_execute_commands, host, cmd["tasks"], username, port))
        for work in as_completed(works_queue):
            work.result()
    executor.shutdown(wait=True)

def main():
    click_main()

if __name__ == "__main__":
    main()