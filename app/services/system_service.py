import platform
import psutil


def get_system_info():
    return {
        "hostname": platform.node(),
        "operating_system": platform.system(),
        "operating_system_version": platform.release(),
        "cpu_usage": psutil.cpu_percent(interval=1),
        "memory_usage": psutil.virtual_memory().percent,
        "disk_usage": psutil.disk_usage("C:\\").percent,
    }