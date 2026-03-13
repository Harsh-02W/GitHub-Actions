from monitor import get_cpu_usage, get_memory_usage, get_disk_usage


def test_cpu_usage():
    cpu = get_cpu_usage()
    assert 0 <= cpu <= 100


def test_memory_usage():
    memory = get_memory_usage()
    assert 0 <= memory <= 100


def test_disk_usage():
    disk = get_disk_usage()
    assert 0 <= disk <= 100
