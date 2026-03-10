# Multi-Server-Control-Program

## Task
This is a command and control program that allows us to run tasks on multiple servers. The program is able to run a simple yaml format playbook (e.g., `playbook.yaml`) with the hosts group config in hosts file (`/etc/playbook/hosts`).

## Prerequisite
- Please run in Linus/MacOS.
- For every hosts in hosts file, you should make sure the host is inside `~/.ssh/known_hosts`. use `ssh-keygen` to generate the key pair in your current machine, and copy your public key to that host.

## Run the program

1. This repo use poetry to manage the packages, you should install the dependency first with

    ```
    cd Multi-Server-Control-Program
    poetry install
    ```

2. To run the script in virtual env
    ```
    poetry run python main.py
    ```
    or with CLI options
    ```
    poetry run python main.py --playbook path_to_playbook --hosts path_to_hosts_file --username ssh_username --port ssh_port
    ```

3. Run Tests
    ```
    poetry run pytest
    ```

4. Pre-commit installation (during development)
    ```
    pre-commit install
    pre-commit run --all-files
    ```

## Highlight of the Project
### Security Highlight
1. We don't save or transfer the ssh key in the program, instead we load it in ~/.ssh/id_rsa
2. We only allow known hosts to connect, avoid men in the middle attack.

### Others
1. We use threads pool to allow concurrent execution, making the program more efficient.
2. We use poetry to manage python packages, use pre-commit to point out potential issue in code (upon every commit).
