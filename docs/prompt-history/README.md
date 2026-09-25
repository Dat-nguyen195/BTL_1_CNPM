# 📋 Prompt History – Smart E-Mobility Hub Sprint 1

Thư mục này lưu trữ nhật ký Prompt AI cá nhân của 7 thành viên, phục vụ minh bạch liêm chính học thuật theo **GenAI Policy** của môn CO3001 HK261.

## Cấu trúc thư mục

```
docs/prompt-history/
├── README.md                        # Hướng dẫn chung (file này)
├── TV1_NguyenThanhDat/              # Nguyễn Thành Đạt – SS1
├── TV2_NguyenAnhTai/                # Nguyễn Anh Tài – SS2
├── TV3_PhamTienDat/                  # Phạm Tiến Đạt – SS3
├── TV4_DangHoangQuyNhan/            # Đặng Hoàng Quý Nhân – SS4
├── TV5_DuongDangKhoa/               # Dương Đăng Khoa – SS5
├── TV6_HoangVanTan/                 # Hoàng Văn Tấn – SS6
└── TV7_NguyenTrungNguyen/                      # Nguyễn Trung Nguyên – SS7
```

## Quy trình nộp bài (Git Workflow)

```bash
# 1. Tạo nhánh riêng từ main
git checkout main && git pull origin main
git checkout -b feature/<mssv>-prompt-history

# 2. Đặt file vào đúng thư mục của mình
# Ví dụ TV1: docs/prompt-history/TV1_NguyenThanhDat/Prompt_History_Sprint1_2410709_NguyenThanhDat.pdf

# 3. Commit & Push
git add docs/prompt-history/
git commit -m "docs(prompt-history): add Sprint 1 prompt log by <mssv>"
git push origin feature/<mssv>-prompt-history

# 4. Tạo Pull Request vào main – gán Peer Reviewer theo bảng phân công Mục 3
```

## Yêu cầu nội dung file nhật ký

- Bao gồm **toàn bộ** lịch sử chat AI (ChatGPT, Gemini, Copilot, …).
- Ghi rõ: **timestamp**, **nội dung prompt**, **phản hồi AI**, và **các chỉnh sửa thực tế** so với đề xuất của AI.
- **Deadline nộp PR:** Trước hạn chót nội bộ **24–48 giờ**.
