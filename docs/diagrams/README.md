# 📐 Danh mục Sơ đồ Thiết kế (Diagrams Hub)

## Smart E-Mobility Hub (ĐHQG-HCM)

Thư mục này quản lý toàn bộ các sơ đồ thiết kế hệ thống và sơ đồ phân tích nghiệp vụ của 7 phân hệ.

---

## 1. Cấu trúc Thư mục

```
docs/diagrams/
├── system/
│   ├── generate_system_usecase.py      # Script sinh sơ đồ tổng thể tự động
│   ├── parse_drawio.py                 # Script phân tích cấu trúc Draw.io
│   ├── smartEhub.drawio                # File thiết kế Draw.io gốc (17 Canonical UCs)
│   ├── smartEhub.svg                   # Vector SVG phân giải cao
│   ├── smartEhub.png                   # Render PNG dùng cho tài liệu
│   └── smartEhub.pdf                   # Bản xuất PDF khổ lớn
└── Use-case detail-scenario/
    ├── SS1/  # Nguyễn Thành Đạt (3 UCs)
    │   ├── Activity diagrams/
    │   ├── Sequence diagrams/
    │   ├── State-chart diagrams/
    │   └── Usecase scenario/
    ├── SS2/  # Nguyễn Anh Tài (4 UCs)
    │   ├── Activity diagrams/
    │   ├── Sequence diagrams/
    │   ├── State-chart diagrams/
    │   └── Usecase scenario/
    ├── SS3/  # Phạm Tiến Đạt (2 UCs)
    │   ├── Activity diagrams/
    │   ├── Sequence diagrams/
    │   ├── State-chart diagrams/
    │   └── Usecase scenario/
    ├── SS4/  # Đặng Hoàng Quý Nhân (2 UCs)
    │   ├── Activity diagrams/
    │   ├── Sequence diagrams/
    │   ├── State-chart diagrams/
    │   └── Usecase scenario/
    ├── SS5/  # Dương Đăng Khoa (2 UCs)
    │   ├── Activity diagrams/
    │   ├── Sequence diagrams/
    │   ├── State-chart diagrams/
    │   └── Usecase scenario/
    ├── SS6/  # Hoàng Văn Tấn (2 UCs)
    │   ├── Activity diagrams/
    │   ├── Sequence diagrams/
    │   ├── State-chart diagrams/
    │   └── Usecase scenario/
    └── SS7/  # Nguyễn Trung Nguyên (2 UCs)
        ├── Activity diagrams/
        ├── Sequence diagrams/
        ├── State-chart diagrams/
        └── Usecase scenario/
```

---

## 2. Quy chuẩn Kỹ thuật
- **Định dạng nguồn:** PlantUML (`.puml`) mã hóa UTF-8.
- **Biên dịch hình ảnh:** PNG và SVG tương ứng được render tự động qua `plantuml.jar` với layout engine Smetana.
- **Chuẩn giao tiếp:**
  - Sequence diagrams: 6 lifelines chuẩn theo trách nhiệm.
  - Activity diagrams: 5 swimlanes chuẩn.
  - State-chart diagrams: Chuẩn hóa định danh trạng thái `UPPER_CASE`.
