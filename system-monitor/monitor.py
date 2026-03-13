import psutil


def get_cpu_usage():
    """Return CPU usage percentage"""
    return psutil.cpu_percent(interval=1)


def get_memory_usage():
    """Return memory usage percentage"""
    memory = psutil.virtual_memory()
    return memory.percent


def get_disk_usage():
    """Return disk usage percentage"""
    disk = psutil.disk_usage('/')
    return disk.percent
