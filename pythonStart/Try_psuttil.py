import psutil
for x in range(10):
    print(psutil.cpu_percent(interval=1, percpu=True))