"""Render traceability and the report scope from the generated manifest."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
data = json.loads((ROOT / 'docs/traceability/submission_2.json').read_text())
md = ['# Ma trận truy vết Submission #2', '', '**Baseline:** `docs/requirements-analysis.md`. VERIFIED chỉ xác thực luồng prototype trong phạm vi bằng chứng nêu dưới đây; không đồng nghĩa sản phẩm đã nghiệm thu triển khai thực tế.', '', '## 1. Danh mục 17 Use Case', '', '| UC | Phân hệ | Nghiệp vụ | Người phụ trách | Scenario |', '|---|---|---|---|---|']
for uid, uc in data['canonical_use_cases'].items():
    md.append(f"| {uid} | {uc['subsystem']} | {uc['name']} | {uc['owner']} | [Scenario](../../{uc['scenario_file']}) |")
md += ['', '## 2. Truy vết 30 User Story', '', '| US | Nội dung SRS | FR | UC | Ưu tiên / trọng số | Test | Trạng thái |', '|---|---|---|---|---|---|---|']
for uid, us in data['user_stories'].items():
    md.append(f"| {uid} | {us['title']} | {', '.join(us['fr_links'])} | {', '.join(us['canonical_ucs'])} | {us['moscow']} / {us['weight']} | `{us['test_id']}` | {us['status']} |")
md += ['', '## 3. Yêu cầu chức năng từ SRS', '', '| FR | Nội dung nguyên bản | US |', '|---|---|---|']
for uid, fr in data['functional_requirements'].items():
    md.append(f"| {uid} | {fr['description']} | {', '.join(fr['user_stories'])} |")
m = data['moscow_summary']
md += ['', '## 4. MoSCoW tính từ bằng chứng prototype', '', 'Tỷ lệ dưới đây dùng trọng số nội bộ của nhóm, không phải điểm hay trọng số do giảng viên công bố. PARTIAL được tính 0 điểm xác thực để tránh phóng đại kết quả.', '', '| Nhóm | Số US | Trọng số | US VERIFIED | Trọng số VERIFIED | Tỷ lệ theo trọng số |', '|---|---:|---:|---:|---:|---:|']
for key in ['must', 'should', 'could']:
    v = m[key]
    md.append(f"| {key.upper()} | {v['count']} | {v['weight']} | {v['verified_count']} | {v['verified_weight']} | {v['coverage_pct']:.2f}% |")
md.append(f"| Tổng | {m['total_user_stories']} | {m['total_weight']} | {m['verified_count']} | {m['overall_verified_weight']} | {m['overall_coverage_pct']:.2f}% |")
md += ['', '## 5. Phạm vi bằng chứng và giới hạn', '', '- SSO, QR/barie, IoT và thanh toán dùng dữ liệu mô phỏng trong phiên Streamlit; chưa phải tích hợp dịch vụ thật.', '- Test mở trang chỉ là smoke test, không được dùng riêng để xác thực các luồng điều chuyển, sự cố, dự báo hay điều hướng.', '- Các test `test_submission_2_acceptance.py` thực hiện hành động và kiểm tra thay đổi trạng thái, sức chứa, sổ cái, dự báo hoặc kết quả hiển thị.', '- Bằng chứng thực thi được lưu tại `docs/audit/submission_2/final/pytest.txt` và `pytest.xml`.', '']
for uid, us in data['user_stories'].items():
    if us['status'] != 'VERIFIED':
        md.append(f"- **{uid} — {us['status']}:** {us['evidence_scope']}")
(ROOT / 'docs/traceability/submission_2.md').write_text('\n'.join(md) + '\n')
# This small generated table is included in the final report; one source of counts.
tex = [r'\subsection{Phạm vi Prototype và Bằng chứng Kiểm thử (MoSCoW)}', r'Các tỷ lệ sau là phép tính theo trọng số nội bộ của nhóm, không phải rubric định lượng của môn học. Mục tiêu nhóm là xác thực ít nhất 90\% trọng số luồng prototype. VERIFIED chỉ áp dụng cho luồng mô phỏng có bằng chứng tự động; PARTIAL không được cộng vào trọng số đã xác thực. SSO, IoT, QR/barie và cổng thanh toán thật nằm ngoài phạm vi tích hợp của đợt nộp này.', r'\begin{table}[H]\centering\small', r'\caption{Mức xác thực luồng Prototype theo trọng số MoSCoW}\label{tab:moscow-scope}', r'\begin{tabularx}{\textwidth}{|X|r|r|r|r|}\hline', r'Nhóm & Số US & Trọng số & Điểm xác thực & Tỷ lệ \\\hline']
for key in ['must', 'should', 'could']:
    v = m[key]
    tex.append(f"{key.upper()} & {v['count']} & {v['weight']} & {v['verified_weight']} & {v['coverage_pct']:.2f}\\% \\\\\\hline")
tex += [f"Tổng & {m['total_user_stories']} & {m['total_weight']} & {m['overall_verified_weight']} & {m['overall_coverage_pct']:.2f}\\% \\\\\\hline", r'\end{tabularx}\end{table}', r'\noindent Ma trận chi tiết US--FR--UC--code--test được bàn giao trong \path{docs/traceability/submission_2.md}. Các tiêu chí còn một phần gồm: US-06 chưa đo quãng đường thực tế; US-12 chưa xác thực toàn bộ hành trình thanh toán riêng của nhân viên; US-21 chưa mô hình hóa biến động doanh thu. Những giới hạn này không được tính là VERIFIED.', r'\par Mỗi bản nộp kèm kết quả Pytest và kiểm tra cú pháp PlantUML; việc vượt kiểm tra không thay thế đánh giá nội dung thiết kế.']
(ROOT / 'docs/report/submission_2/generated_scope.tex').write_text('\n'.join(tex) + '\n')
print('Generated traceability Markdown and report scope')
