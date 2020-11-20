import psutil

print("CPU Percent : ", psutil.cpu_percent(interval=None),"%")
print("RAM Used : ", psutil.virtual_memory().percent,"%")

net = psutil.net_io_counters(pernic=False)
tx = net[2] / 1000
rx = net[3] / 1000
print("TX/RX :", tx, "kbps /", rx, "kbps")
