# 📐 Hướng dẫn Nộp & Quản lý Sơ đồ (Diagrams Repository)

Thư mục này lưu trữ toàn bộ các sơ đồ thiết kế hệ thống (Use-case Diagram, Sequence Diagram, Activity Diagram, Class Diagram) cho Dự án **Smart E-Mobility Hub**.

---

## 1. Cấu trúc thư mục (Folder Hierarchy)

```
docs/diagrams/
├── README.md                      # Hướng dẫn quy chuẩn nộp và quản lý file sơ đồ
├── system/                        # Sơ đồ cấp toàn hệ thống (System-wide Level)
│   ├── system_usecase_diagram.drawio
│   └── system_usecase_diagram.png
└── subsystems/                    # Sơ đồ phân hệ & Use-case chi tiết từng cá nhân
    ├── SS1_student_booking/       # Phân hệ SS1 (TV1)
    │   ├── 2410709_UC_Dat_Xe_Dung_Chung.drawio
    │   ├── 2410709_UC_Dat_Xe_Dung_Chung.png
    │   ├── 2410709_UC_Huy_Dat_Xe.drawio
    │   └── 2410709_UC_Huy_Dat_Xe.png
    ├── SS2_personal_ev/           # Phân hệ SS2 (TV2)
    │   ├── <mssv>_UC_Dang_Ky_Gui_Xe_Ca_Nhan.[drawio|png]
    │   └── <mssv>_UC_Dat_Lich_Sac_Xe_Ca_Nhan.[drawio|png]
    ├── SS3_hub_monitor/           # Phân hệ SS3 (TV3)
    │   ├── <mssv>_UC_Giam_Sat_Trang_Thai_Hub.[drawio|png]
    │   └── <mssv>_UC_Canh_Bao_Qua_Tai.[drawio|png]
    ├── SS4_dispatch_incident/     # Phân hệ SS4 (TV4)
    │   ├── <mssv>_UC_Lap_Lenh_Dieu_Chuyen_Phuong_Tien.[drawio|png]
    │   └── <mssv>_UC_Bao_Cao_Su_Co_Phuong_Tien.[drawio|png]
    ├── SS5_smart_charging/        # Phân hệ SS5 (TV5)
    │   ├── <mssv>_UC_Lap_Lich_Uu_Tien_Sac_Tu_Dong.[drawio|png]
    │   └── <mssv>_UC_Giam_Sat_Hang_Cho_Sac.[drawio|png]
    ├── SS6_sim_demand/            # Phân hệ SS6 (TV6)
    │   ├── <mssv>_UC_Mo_Phong_Tang_Dot_Bien_Khach_Metro.[drawio|png]
    │   └── <mssv>_UC_Phan_Tich_Anh_Huong_Nhu_Cau.[drawio|png]
    └── SS7_sim_infrastructure/    # Phân hệ SS7 (TV7)
        ├── <mssv>_UC_Mo_Phong_Su_Co_Mat_Dien_Tram_Sac.[drawio|png]
        └── <mssv>_UC_Goi_Y_Dieu_Huong_Tu_Dong.[drawio|png]
```

---

## 2. Quy chuẩn đặt tên file (File Naming Conventions)

1. **Mỗi Use-case bắt buộc nộp cả 2 định dạng:**
   - File nguồn: `.drawio` (hoặc `.puml` nếu dùng PlantUML) để phục vụ chỉnh sửa.
   - File ảnh xuất ra: `.png` (nền trong suốt hoặc nền trắng, độ phân giải cao $\geq 300$ DPI) để chèn vào báo cáo LaTeX / Markdown.
2. **Cú pháp đặt tên file:**
   - **File cá nhân:** `<MSSV>_<Mã_Use_Case>.<ext>`
     - Ví dụ: `2410709_UC_Dat_Xe_Dung_Chung.drawio` và `2410709_UC_Dat_Xe_Dung_Chung.png`
   - **File toàn hệ thống:** `system_<tên_loại_sơ_đồ>.<ext>`
     - Ví dụ: `system_usecase_diagram.drawio` và `system_usecase_diagram.png`

---

## 3. Quy trình Git & Nộp bài (Git Workflow)

Mỗi thành viên tuân thủ nghiêm ngặt quy trình GitHub Flow sau:

```bash
# 1. Cập nhật nhánh main mới nhất
git checkout main
git pull origin main

# 2. Tạo nhánh làm việc theo đúng cú pháp quy định
git checkout -b feature/<mssv>-usecase

# 3. Thêm file sơ đồ vào đúng thư mục phân hệ tương ứng
# Ví dụ TV1:
# docs/diagrams/subsystems/SS1_student_booking/2410709_UC_Dat_Xe_Dung_Chung.drawio
# docs/diagrams/subsystems/SS1_student_booking/2410709_UC_Dat_Xe_Dung_Chung.png

# 4. Commit tuân thủ Conventional Commits
git add docs/diagrams/
git commit -m "docs(diagram): add use-case diagrams for SS1 by <mssv>"

# 5. Push lên remote repository
git push origin feature/<mssv>-usecase
```

---

## 4. Quy trình Tạo Pull Request & Peer Review chéo

1. **Tạo Pull Request:**
   - **Base branch:** `main` $\leftarrow$ **Compare branch:** `feature/<mssv>-usecase`
   - **Tiêu đề PR:** `[Sprint 1][Diagram] Nộp sơ đồ Use-case phân hệ SS<X> - <Họ và Tên> (<MSSV>)`
   - **Reviewer:** Gán trực tiếp **Người Review chéo** tương ứng theo bảng phân công Mục 3 Biên bản họp số 01:
     - TV1 $\leftrightarrow$ TV2
     - TV3 $\leftrightarrow$ TV4
     - TV5 $\rightarrow$ TV7 $\rightarrow$ TV6 $\rightarrow$ TV5
2. **Tiêu chí duyệt sơ đồ (Review Checklist):**
   - [ ] Đủ cả file nguồn `.drawio` và file ảnh `.png`.
   - [ ] Đặt đúng thư mục phân hệ `docs/diagrams/subsystems/SS<X>_.../`.
   - [ ] Đầy đủ các thành phần: Actor, System Boundary, Use-case name, quan hệ `<<include>>`, `<<extend>>`, `Generalization` (nếu có).
   - [ ] Khớp 100% với tên Use-case đã phân công trong Biên bản Họp #1.
3. **Thời hạn:**
   - Hoàn thành nộp PR trước hạn nộp nội bộ **24 – 48 giờ** để Peer Reviewer có đủ thời gian phản biện và yêu cầu chỉnh sửa.
