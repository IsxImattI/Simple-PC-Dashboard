import psutil

def cpu_usage():
    return psutil.cpu_percent(interval=1)

def memory_usage():
    return psutil.virtual_memory().percent