# 🤖 BẢN CAM KẾT & TUYÊN BỐ MINH BẠCH SỬ DỤNG GENERATIVE AI
## (GENAI TRANSPARENCY & ACADEMIC INTEGRITY DISCLOSURE STATEMENT)

> **Môn học:** Công nghệ Phần mềm (Software Engineering – CO3001) – Học kỳ 1 / 2026–2027 (HK261)  
> **Khoa:** Khoa học & Kỹ thuật Máy tính – Trường Đại học Bách Khoa, ĐHQG-HCM  
> **Dự án:** Smart E-Mobility Hub (Hệ thống Trạm Điều phối Phương tiện Điện – Khu Đô thị ĐHQG-HCM)  
> **Thời gian:** Tháng 09/2026  

---

## 1. DANH SÁCH THÀNH VIÊN CAM KẾT

Tập thể nhóm 7 thành viên cam kết tuân thủ nghiêm ngặt Quy chế Liêm chính Học thuật (Academic Integrity) và Hướng dẫn Sử dụng Generative AI theo Quy định của Trường Đại học Bách Khoa – ĐHQG-HCM và Đề cương Môn học CO3001:

| STT | Họ và Tên | MSSV | Email sinh viên | Vai trò | Phân hệ (Subsystem) | Công cụ AI sử dụng |
|:---:|:---|:---:|:---|:---|:---|:---|
| **1** | **Nguyễn Thành Đạt** | **2410709** | dat.nguyen19052006@hcmut.edu.vn | **Project Manager / Lead** | SS1: Quản lý & Đặt xe SV | Claude, Antigravity |
| **2** | **Nguyễn Anh Tài** | **2413035** | tai.nguyenanh1906@hcmut.edu.vn | Developer / Analyst | SS2: Dịch vụ Xe cá nhân | ChatGPT, Claude |
| **3** | **Phạm Tiến Đạt** | **2410724** | dat.phamkhmtk24@hcmut.edu.vn | Developer / Analyst | SS3: Giám sát mạng lưới Hub | Gemini, ChatGPT |
| **4** | **Đặng Hoàng Quý Nhân** | **2412401** | nhan.dangcs06@hcmut.edu.vn | Developer / Analyst | SS4: Điều phối & Sự cố | ChatGPT, Claude |
| **5** | **Dương Đăng Khoa** | **2411589** | khoa.duong272dk@hcmut.edu.vn | Developer / Analyst | SS5: Lập lịch sạc thông minh | ChatGPT, Claude |
| **6** | **Hoàng Văn Tấn** | **2213074** | tan.hoang0815@hcmut.edu.vn | Developer / Simulation | SS6: Mô phỏng Nhu cầu SV | ChatGPT, Gemini |
| **7** | **Nguyễn Trung Nguyên** | **2011710** | nguyen.nguyen1111@hcmut.edu.vn | Developer / Infrastructure | SS7: Mô phỏng Sự cố Hạ tầng | ChatGPT, Claude |

---

## 2. CHÍNH SÁCH & NGUYÊN TẮC CỐT LÕI

Căn cứ Mục 2 & Hướng dẫn Liêm chính Học thuật tại tài liệu *BTL_SoftwareEngineering_HK261_v1.pdf*:
1. **Minh bạch Tuyệt đối (Full Transparency):** Việc sử dụng các công cụ AI tạo sinh (Generative AI) như ChatGPT, Gemini, Claude, GitHub Copilot... được công khai rõ ràng, không che giấu.
2. **AI là Trợ lý, Không thay thế Tư duy Con người:** AI chỉ được xem như một cộng sự hỗ trợ (AI Pair-programmer / Technical Assistant) trong việc tìm kiếm thông tin, gợi ý cú pháp, định dạng văn bản bảng biểu, và khởi tạo boilerplate.
3. **Trách nhiệm Cá nhân (Individual Accountability):** Mỗi thành viên trong nhóm phải nắm vững 100% nội dung phân tích nghiệp vụ, kịch bản Use-Case và từng dòng mã nguồn thuộc phân hệ của mình; tuyệt đối không sao chép nguyên văn nội dung AI tạo ra khi chưa qua quá trình phản biện, kiểm chứng và chỉnh sửa kỹ thuật.

---

## 3. PHẠM VI SỬ DỤNG GENAI TRONG DỰ ÁN

| Hạng mục công việc | Mức độ sử dụng AI | Mục đích cụ thể | Trách nhiệm kiểm chứng của Con người (Human Verification) |
|:---|:---:|:---|:---|
| **Cấu trúc thư mục & Boilerplate** | 40% | Tạo khung sườn repository, mẫu Streamlit pages ban đầu | Nhóm tự tổ chức lại module theo kiến trúc 3 lớp, chuẩn hoá session state |
| **Soạn thảo Đặc tả Use-Case** | 30% | Hỗ trợ định dạng bảng 14 trường theo mẫu chuẩn `mau.png`, gợi ý luồng ngoại lệ | Từng thành viên tự định nghĩa luồng sự kiện nghiệp vụ, tiền điều kiện, hậu điều kiện và quy tắc nghiệp vụ đặc thù |
| **Mã nguồn Prototype (Streamlit)** | 35% | Gợi ý component giao diện (forms, metrics, plots) và khung hàm xử lý | Nhóm viết các hàm nghiệp vụ thực tế, kiểm soát race condition, state transitions |
| **Kiểm định & Rà soát Lỗi (QA Audit)** | 50% | So sánh chéo văn bản SRS với Use-case Diagram và Prototype | Lead Analyst xác thực từng phát hiện, quyết định cập nhật logic và sửa lỗi kỹ thuật |

---

## 4. QUY TRÌNH XÁC MINH CỦA CON NGƯỜI (HUMAN VERIFICATION PROCESS)

Mọi kết quả đầu ra có sự tham gia của công cụ AI đều bắt buộc trải qua quy trình xác minh 3 bước:
1. **Bước 1 — Tự kiểm tra độc lập (Self-check):** Thành viên phụ trách phân hệ trực tiếp đọc hiểu từng câu chữ, kiểm tra tính logic của các bước trong luồng sự kiện (Normal, Alternative, Exception Flows) và chạy thử mã nguồn cục bộ.
2. **Bước 2 — Rà soát chéo (Peer Review):** Thành viên được phân công theo Ma trận Kiểm tra chéo (Mục 3 Biên bản Họp #1) tiến hành review tài liệu và code thông qua Pull Request trên GitHub trước khi merge vào nhánh chính `main`.
3. **Bước 3 — Tổng duyệt hệ thống (System Integration Review):** Nhóm trưởng và Technical Lead kiểm tra tính nhất quán giữa Sơ đồ Use-case toàn hệ thống (`smartEhub.drawio`), báo cáo SRS (`requirements-analysis.md`) và ứng dụng chạy thực tế (`src/app.py`).

---

## 5. LƯU TRỮ VÀ QUẢN LÝ NHẬT KÝ PROMPT (PROMPT HISTORY LOG)

Nhóm thực hiện nghiêm túc quy định lưu vết Prompt:
- **Thư mục lưu trữ:** Toàn bộ nhật ký câu lệnh prompt cá nhân được lưu trữ theo cấu trúc thư mục quy chuẩn tại:
  `docs/prompt-history/TV<X>_<TenThanhVien>/Prompt_History_Sprint1_<MSSV>_<TenThanhVien>.pdf` (hoặc `.txt`).
- **File tổng hợp phiên làm việc chính:** File `docs/prompt_history_antigravity.txt` lưu giữ toàn bộ 49+ prompt tương tác trong suốt quá trình phân tích và xây dựng hệ thống.
- **Nội dung lưu vết:** Bao gồm mốc thời gian (timestamp), nội dung câu lệnh gốc (user prompt), ngữ cảnh phân hệ và mục tiêu kỹ thuật.

---

## 6. LỜI CAM ĐOAN

> Chúng tôi – tập thể 7 thành viên nhóm thực hiện dự án Smart E-Mobility Hub – xin cam đoan rằng toàn bộ nội dung trong Báo cáo Đặc tả Yêu cầu (Submission #1), Sơ đồ Use-case và Mã nguồn Prototype phản ánh đúng tư duy phân tích, công sức lao động trí tuệ và sự phối hợp của các thành viên. Các nội dung tham khảo công cụ AI đều đã được khai báo trung thực, đầy đủ và chịu sự kiểm soát hoàn toàn của nhóm.
