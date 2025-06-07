def phep_cong(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Đầu vào cho phép cộng phải là số!")
    return a + b
