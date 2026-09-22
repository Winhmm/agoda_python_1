# utils/validation.py

def validate_score(score_input):
    try:
        # Điểm phải nằm từ 0.0 đến 10.0
        score = float(score_input)
        if 0.0 <= score <= 10.0:
            return score
        else:
            raise ValueError(f"Điểm {score} không hợp lệ. Điểm phải từ 0 đến 10.")
    except ValueError as e:
        # Bắt cả lỗi ép kiểu (VD: nhập chữ) và lỗi ngoài khoảng 0-10
        raise ValueError(f"Lỗi dữ liệu điểm: {e}")

    