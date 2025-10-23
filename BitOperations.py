val = 0xCAFE
print(f"Initial Value (Hex): 0x{val:X}")
check_lsb_condition = (
    ((val & 0xF) == 0xF) or 
    ((val & 0xF) == 0xE) or 
    ((val & 0xF) == 0xD) or 
    ((val & 0xF) == 0xB) or 
    ((val & 0xF) == 0x7)
)

print("-" * 30)
print("1. At least 3 of last 4 bits are on (0xCAFE ends in E (1110)):")
print(f"   Result (True/False): {check_lsb_condition}")
reversed_bytes_val = ((val & 0x00FF) << 8) | ((val & 0xFF00) >> 8)

print("-" * 30)
print("2. Reverse byte order (0xCAFE -> 0xFECA):")
print(f"   Expression: ((val & 0x00FF) << 8) | ((val & 0xFF00) >> 8)")
print(f"   Result (Hex): 0x{reversed_bytes_val:X}") 
rotated_val = ((val & 0x0FFF) << 4) | ((val & 0xF000) >> 12)

print("-" * 30)
print("3. Rotate four bits (0xCAFE -> 0xECAF):")
print(f"   Expression: ((val & 0x0FFF) << 4) | ((val & 0xF000) >> 12)")
print(f"   Result (Hex): 0x{rotated_val:X}") 