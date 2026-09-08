# 📖 Tài liệu dự án – Smart E-Mobility Hub

## Mục lục

- [Tổng quan kiến trúc](#tổng-quan-kiến-trúc)
- [Mô tả các Subsystem](#mô-tả-các-subsystem)
- [Luồng dữ liệu](#luồng-dữ-liệu)
- [Hướng dẫn phát triển](#hướng-dẫn-phát-triển)

---

## Tổng quan kiến trúc

```
┌─────────────────────────────────────────────┐
│              Streamlit Frontend              │
│  ┌─────────┐ ┌─────────┐ ┌─────────┐       │
│  │  SS1-2  │ │  SS3-4  │ │  SS5-7  │ ...   │
│  │ Student │ │Operator │ │Charging │       │
│  └────┬────┘ └────┬────┘ └────┬────┘       │
│       │           │           │             │
│  ┌────▼───────────▼───────────▼────┐        │
│  │      st.session_state           │        │
│  │   (In-memory JSON Data Store)   │        │
│  └────────────────┬────────────────┘        │
│                   │                         │
│  ┌────────────────▼────────────────┐        │
│  │        Core Modules             │        │
│  │  scheduler.py  │  simulator.py  │        │
│  └─────────────────────────────────┘        │
└─────────────────────────────────────────────┘
```

## Mô tả các Subsystem

### SS1 – Quản lý & Đặt xe cho Sinh viên
- **File:** `src/components/student_booking.py`
- **Người phụ trách:** Thành viên 1 (PM)
- **Chức năng:** Tìm xe theo Hub, lọc theo loại xe / pin, đặt xe hoặc chỗ đỗ

### SS2 – Đăng ký dịch vụ Xe cá nhân
- **File:** `src/components/personal_ev.py`
- **Người phụ trách:** Thành viên 2
- **Chức năng:** Đăng ký xe EV cá nhân, đặt slot đỗ, yêu cầu sạc

### SS3 – Giám sát mạng lưới Hub
- **File:** `src/components/hub_monitor.py`
- **Người phụ trách:** Thành viên 3
- **Chức năng:** Dashboard KPI, bản đồ Hub, biểu đồ tình trạng, cảnh báo quá tải

### SS4 – Điều phối & Xử lý sự cố
- **File:** `src/components/dispatch_incident.py`
- **Người phụ trách:** Thành viên 4
- **Chức năng:** Chuyển xe giữa các Hub, báo cáo sự cố (va chạm, hết pin, hỏng)

### SS5 – Lập lịch sạc thông minh
- **File:** `src/components/smart_charging.py`
- **Người phụ trách:** Thành viên 5
- **Chức năng:** Hàng đợi sạc ưu tiên, thuật toán scoring, thêm/xoá yêu cầu

### SS6 – Mô phỏng nhu cầu SV
- **File:** `src/components/sim_demand.py`
- **Người phụ trách:** Thành viên 6
- **Chức năng:** Slider dự đoán nhu cầu, biểu đồ hàng đợi, Metro Surge simulation

### SS7 – Mô phỏng sự cố hạ tầng
- **File:** `src/components/sim_infrastructure.py`
- **Người phụ trách:** Thành viên 7
- **Chức năng:** Toggle cổng sạc, mô phỏng port failure, đề xuất rerouting

## Luồng dữ liệu

1. Ứng dụng khởi động → Load `mock_hubs.json` vào `st.session_state["hubs"]`
2. Mỗi subsystem đọc/ghi từ `st.session_state` → dữ liệu đồng bộ giữa các trang
3. Core modules (`scheduler.py`, `simulator.py`) xử lý logic phức tạp

## Hướng dẫn phát triển

1. Tạo branch: `git checkout -b feature/<mssv>-<tên-tính-năng>`
2. Code & test local: `streamlit run src/app.py`
3. Commit: `git commit -m "feat(ss<N>): <mô tả>"`
4. Push & tạo PR: tuân thủ PR template
5. Code review bởi ít nhất 1 thành viên khác
6. Merge vào `main` sau khi approve
