import paramiko
from src.config import config_dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_host(host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # TODO: check this for security later
    ssh.connect(host, port=config_dict["port"], username=config_dict["username"]) # TODO: auto get these
    return ssh

def execute_command(ssh, command):
    _, stdout, stderr = ssh.exec_command(command)
    logger.info(" stdout: " + stdout.read().decode("utf-8"))
    logger.error(" stderr: " + stderr.read().decode("utf-8"))
    return

def connect_and_execute_commands(host, commands):
    ssh = connect_to_host(host)
    try:
        for command in commands:
            logger.info(f"Execute command on {host}: {command['name']}")
            execute_command(ssh, command["bash"])
    finally:
        ssh.close()
    return