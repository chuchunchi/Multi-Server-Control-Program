# Multi-Server-Control-Program

## Task
This is a command and control program that allows us to run tasks on multiple servers. The program is able to run a simple yaml format playbook (e.g., `example_playbook.yaml`) with the hosts group config in hosts file (`/etc/playbook/hosts`).

## Prerequest
For every hosts in hosts file, you should make sure the host has your public key. use `ssh-keygen` to generate the key pair in your current machine, and copy your public key to that host.

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


