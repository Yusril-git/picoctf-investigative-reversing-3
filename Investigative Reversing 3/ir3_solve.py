# solve_ir3.py
def solve_ir3():
    with open('encoded.bmp', 'rb') as f:
        # Lewati header file BMP sebanyak 723 byte
        f.seek(723)
        flag = ""
        # Flag terdiri dari 50 karakter
        for i in range(50):
            char_byte = 0
            # Rekonstruksi 1 karakter dari 8 byte gambar
            for j in range(8):
                img_byte = f.read(1)
                lsb = ord(img_byte) & 1
                char_byte = (char_byte << 1) | lsb
            
            flag += chr(int(bin(char_byte)[2:].zfill(8)[::-1], 2))
            # Lewati 1 byte sesuai pola
            f.read(1)
    print(flag)

solve_ir3()