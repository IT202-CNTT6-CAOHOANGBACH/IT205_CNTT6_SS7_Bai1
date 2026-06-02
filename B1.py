student_name = "  nguYEn vAn a  "
student_code = "  rk-001-python  "
email = "  Student01@GMAIL.COM  "

student_name_reset = student_name.title().strip()
student_code_reset = student_code.upper().strip()
email_reset = email.lower().strip()
print("Họ tên:", student_name_reset)
print("Mã học viên:", student_code_reset)
print("Email:", email_reset)

# Vì sao student_name.strip() không làm thay đổi trực tiếp biến student_name?
# Vì sao student_name.title() không tạo ra kết quả "Nguyen Van A" trong chương trình hiện tại?
# Vì sao student_code.upper() không làm mã học viên chuyển thành chữ hoa?
# Vì sao email.lower() không làm email chuyển thành chữ thường?
# Muốn các phương thức xử lý chuỗi có hiệu lực, cần làm gì?
# đáp án
# vì nó chưa dc gán giá trị mới vậy nên cần gán giá trị mới sau khi sự dụng