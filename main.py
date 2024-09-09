import os
from Crypto.Random import get_random_bytes

exe_path = input(f'[#] Enter FileName: ')
increase_size = int(input(f'[#] Enter How Much KB You Need: ')) * 1024
if not os.path.exists(exe_path):
    print(f"[-] Error: '{exe_path}' does not exist.")
    os._exit(-1)
with open(exe_path, 'rb+') as file:
    file.seek(0, os.SEEK_END)
    if input(f'[?] Random Bytes Or Null Bytes? (R/N) N For Null : ').lower() == 'r':
        for i in range(increase_size):
            file.write(get_random_bytes(1))
    else:
        file.write(b'\00' * increase_size)
        
print(f'\n[+] Final File Size : {round(os.stat(exe_path).st_size / 1024)} KB')
print()
os.system('pause')