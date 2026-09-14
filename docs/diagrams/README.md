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
└── <mssv>_<tên_use_case>.[drawio|png] # File sơ đồ use-case cá nhân đặt trực tiếp tại docs/diagrams/
```

> **Ghi chú:** Toàn bộ sơ đồ Use-case cá nhân được nộp trực tiếp vào thư mục `docs/diagrams/` trên nhánh `feature/<mssv>-usecase` theo đúng yêu cầu đề bài.

---

## 2. Quy chuẩn đặt tên file (File Naming Conventions)

1. **Mỗi Use-case bắt buộc nộp cả 2 định dạng:**
   - File nguồn: `.drawio` (hoặc `.puml` nếu dùng PlantUML) để phục vụ chỉnh sửa.
   - File ảnh xuất ra: `.png` (nền trong suốt hoặc nền trắng, độ phân giải cao $\geq 300$ DPI) để chèn vào báo cáo LaTeX / Markdown.
2. **Cú pháp đặt tên file:**
   - **File cá nhân (đặt tại `docs/diagrams/`):** `<MSSV>_<Mã_Use_Case>.<ext>`
     - Ví dụ TV1: `2410709_UC_Dat_Xe_Dung_Chung.drawio` và `2410709_UC_Dat_Xe_Dung_Chung.png`
     - Ví dụ TV1: `2410709_UC_Huy_Dat_Xe.drawio` và `2410709_UC_Huy_Dat_Xe.png`
   - **File toàn hệ thống:** `system_<tên_loại_sơ_đồ>.<ext>` (lưu tại `docs/diagrams/system/` hoặc `docs/diagrams/`)
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

# 3. Thêm file sơ đồ trực tiếp vào thư mục docs/diagrams/
# Ví dụ TV1:
# docs/diagrams/2410709_UC_Dat_Xe_Dung_Chung.drawio
# docs/diagrams/2410709_UC_Dat_Xe_Dung_Chung.png

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
   - [ ] Đặt đúng thư mục `docs/diagrams/`.
   - [ ] Đầy đủ các thành phần: Actor, System Boundary, Use-case name, quan hệ `<<include>>`, `<<extend>>`, `Generalization` (nếu có).
   - [ ] Khớp 100% với tên Use-case đã phân công trong Biên bản Họp #1.
3. **Thời hạn:**
   - Hoàn thành nộp PR trước hạn nộp nội bộ **24 – 48 giờ** để Peer Reviewer có đủ thời gian phản biện và yêu cầu chỉnh sửa.
