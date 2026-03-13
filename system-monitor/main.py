from monitor import get_cpu_usage, get_memory_usage, get_disk_usage


def main():
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    print("System Health Report")
    print("--------------------")
    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {memory}%")
    print(f"Disk Usage: {disk}%")


if __name__ == "__main__":
    main()
