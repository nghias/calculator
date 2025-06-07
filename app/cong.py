def phep_cong(*numbers):
  if not numbers:
    return 0
  for num in numbers:
    if not isinstance(num, (int, float)):
      raise TypeError(f"Lỗi: Tất cả đầu vào phải là số, nhưng tìm thấy '{num}' có kiểu {type(num).__name__}.")

  return sum(numbers)
