from Maix import freq

cpu_freq, kpu_freq = freq.get()

print(cpu_freq, kpu_freq)

print(freq.get_cpu(), freq.get_kpu())
