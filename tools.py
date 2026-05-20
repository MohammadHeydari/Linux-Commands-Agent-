TOOLS = {
    # system info
    "time": "date",
    "hostname": "hostname",
    "uptime": "uptime",
    "system": "uname -a",

    # user
    "user": "whoami",

    # files
    "list_files": "ls -lah",
    "list_sorted": "ls -lhS",
    "tree": "ls -R",
    "find_py": "find . -name '*.py'",

    # disk / memory
    "disk": "df -h",
    "mem": "free -h",

    # network
    "ip": "ip addr show",
    "ports": "ss -tulnp",

    # processes
    "processes": "ps aux",
    "top_cpu": "ps -eo pid,ppid,cmd,%mem,%cpu --sort=-%cpu | head",

    # directory
    "pwd": "pwd",

    # docker safe commands
    "docker_ps": "docker ps",
    "docker_images": "docker images",
    "docker_stats": "docker stats --no-stream",
    "docker_version": "docker --version",
    "docker_info": "docker info",

    # container inspection (safe)
    "docker_all_containers": "docker ps -a",
}