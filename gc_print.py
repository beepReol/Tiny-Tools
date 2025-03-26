import psutil
import platform
import time
print("Searching for data...")
time.sleep(5)
try:
    import GPUtil
except ImportError:
    print("GPU was not found.")

def get_cpu_info():
    cpu_model = platform.processor()
    cpu_cores = psutil.cpu_count(logical=False)
    return f"CPU Model: {cpu_model}, Cores: {cpu_cores}"

def get_gpu_info():
    try:
        gpus = GPUtil.getGPUs()
        gpu_names = [gpu.name for gpu in gpus]
        return f"GPU Model(s): {', '.join(gpu_names)}"
    except NameError:
        return "GPU gegevens niet beschikbaar"

cpu_info = get_cpu_info()
gpu_info = get_gpu_info()

print(cpu_info)
print(gpu_info)

time.sleep(1)

print("Thank You for using GC Print!", flush=True)

