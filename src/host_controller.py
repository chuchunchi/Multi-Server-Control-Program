import paramiko
from src.config import config_dict
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def connect_to_host(host, username, port):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) # TODO: check this for security later
    logger.info(f"Connect to {host} with username {username}, port {port}")
    try:
        ssh.connect(host, port=port, username=username) # will get password from system
    except Exception as e:
        logger.error(f"error connecting to {host}: {e}")
        return None
    return ssh

def execute_command(ssh, command):
    _, stdout, stderr = ssh.exec_command(command)
    stdout = str(stdout.read().decode("utf-8"))
    stderr = str(stderr.read().decode("utf-8"))
    if stdout != "":
        logger.info(" stdout: " + stdout)
    if stderr != "":
        logger.error(" stderr: " + stderr)
    return

def connect_and_execute_commands(host, commands, username, port):
    ssh = connect_to_host(host, username, port)
    try:
        for command in commands:
            logger.info(f"Execute command on {host}: {command['name']}")
            execute_command(ssh, command["bash"])
    finally:
        ssh.close()
    return