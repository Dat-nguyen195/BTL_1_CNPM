with open("docs/report/submission_2/main.tex", "r", encoding="utf-8") as f:
    text = f.read()

figures_and_tables_section = r"""% ============================================================
%               DANH MỤC HÌNH ẢNH & BẢNG BIỂU
% ============================================================
\section*{Danh mục hình ảnh và bảng biểu}
\addcontentsline{toc}{section}{Danh mục hình ảnh và bảng biểu}

\subsection*{Danh mục hình ảnh (List of Figures)}
\renewcommand{\arraystretch}{1.15}
\small
\begin{longtable}{|c|p{8.5cm}|c|c|}
    \hline
    \textbf{Ký hiệu} & \textbf{Tên hình ảnh / Sơ đồ} & \textbf{Vị trí / Mục} & \textbf{Số trang} \\
    \hline
    \endfirsthead
    \hline
    \textbf{Ký hiệu} & \textbf{Tên hình ảnh / Sơ đồ} & \textbf{Vị trí / Mục} & \textbf{Số trang} \\
    \hline
    \endhead
    \hline
    \endfoot
    \textbf{Hình 1.1} & Sơ đồ Luồng Màn hình Điều hướng Tổng thể (Screen Navigation Flow) & Mục 1.3 & \pageref{fig:screen-flow} \\
    \hline
    \textbf{Hình 1.2} & Giao diện Thực tế: Đặt xe \& Quản lý Chỗ đỗ Sinh viên (Phân hệ SS1) & Mục 1.4 & \pageref{fig:ui-ss1-real} \\
    \hline
    \textbf{Hình 1.3} & Giao diện Thực tế: Đăng ký Phương tiện EV \& Bãi đỗ (Phân hệ SS2) & Mục 1.4 & \pageref{fig:ui-ss2-real} \\
    \hline
    \textbf{Hình 1.4} & Giao diện Thực tế: Bảng Điều khiển Giám sát Mạng lưới Hub (Phân hệ SS3) & Mục 1.5 & \pageref{fig:ui-ss3-real} \\
    \hline
    \textbf{Hình 1.5} & Giao diện Thực tế: Điều phối Cân bằng Tải \& Xử lý Sự cố (Phân hệ SS4) & Mục 1.5 & \pageref{fig:ui-ss4-real} \\
    \hline
    \textbf{Hình 1.6} & Giao diện Thực tế: Lập lịch Sạc Thông minh \& Quản lý Hàng đợi (Phân hệ SS5) & Mục 1.5 & \pageref{fig:ui-ss5-real} \\
    \hline
    \textbf{Hình 1.7} & Giao diện Thực tế: Mô phỏng Nhu cầu Đột biến Metro Surge (Phân hệ SS6) & Mục 1.6 & \pageref{fig:ui-ss6-real} \\
    \hline
    \textbf{Hình 1.8} & Giao diện Thực tế: Mô phỏng Sự cố Hạ tầng \& Gợi ý 1-chạm (Phân hệ SS7) & Mục 1.6 & \pageref{fig:ui-ss7-real} \\
    \hline
    \textbf{Hình 2.1} & Sơ đồ Tuần tự Chi tiết -- UC\_SS1\_01 (Đặt xe \& Quét nhận xe) & Mục 2.1 & \pageref{fig:seq-ss1-01} \\
    \hline
    \textbf{Hình 2.2} & Sơ đồ Tuần tự Chi tiết -- UC\_SS1\_02 (Trả xe 1-chiều \& Quyết toán ví) & Mục 2.1 & \pageref{fig:seq-ss1-02} \\
    \hline
    \textbf{Hình 2.3} & Sơ đồ Tuần tự Chi tiết -- UC\_SS1\_03 (Hủy đặt xe \& Hoàn cọc 100\%) & Mục 2.1 & \pageref{fig:seq-ss1-03} \\
    \hline
    \textbf{Hình 2.4} & Sơ đồ Tuần tự Chi tiết -- UC\_SS2\_01 (Đăng ký xe EV cá nhân) & Mục 2.2 & \pageref{fig:seq-ss2-01} \\
    \hline
    \textbf{Hình 2.5} & Sơ đồ Tuần tự Chi tiết -- UC\_SS2\_02 (Đặt chỗ đỗ \& Lịch sạc xe cá nhân) & Mục 2.2 & \pageref{fig:seq-ss2-02} \\
    \hline
    \textbf{Hình 2.6} & Sơ đồ Tuần tự Chi tiết -- UC\_SS2\_03 (Check-in xe EV cá nhân tại Hub) & Mục 2.2 & \pageref{fig:seq-ss2-03} \\
    \hline
    \textbf{Hình 2.7} & Sơ đồ Tuần tự Chi tiết -- UC\_SS2\_04 (Check-out \& Thanh toán dịch vụ xe) & Mục 2.2 & \pageref{fig:seq-ss2-04} \\
    \hline
    \textbf{Hình 2.8} & Sơ đồ Tuần tự Chi tiết -- UC\_SS3\_01 (Giám sát trạng thái Hub thời gian thực) & Mục 2.3 & \pageref{fig:seq-ss3-01} \\
    \hline
    \textbf{Hình 2.9} & Sơ đồ Tuần tự Chi tiết -- UC\_SS3\_02 (Cảnh báo quá tải \& Đề xuất điều phối) & Mục 2.3 & \pageref{fig:seq-ss3-02} \\
    \hline
    \textbf{Hình 2.10} & Sơ đồ Tuần tự Chi tiết -- UC\_SS4\_01 (Lập lệnh điều phối phương tiện) & Mục 2.4 & \pageref{fig:seq-ss4-01} \\
    \hline
    \textbf{Hình 2.11} & Sơ đồ Tuần tự Chi tiết -- UC\_SS4\_02 (Báo cáo \& Xử lý sự cố kỹ thuật xe) & Mục 2.4 & \pageref{fig:seq-ss4-02} \\
    \hline
    \textbf{Hình 2.12} & Sơ đồ Tuần tự Chi tiết -- UC\_SS5\_01 (Lập lịch ưu tiên sạc tự động) & Mục 2.5 & \pageref{fig:seq-ss5-01} \\
    \hline
    \textbf{Hình 2.13} & Sơ đồ Tuần tự Chi tiết -- UC\_SS5\_02 (Giám sát hàng đợi sạc \& Phí chiếm dụng) & Mục 2.5 & \pageref{fig:seq-ss5-02} \\
    \hline
    \textbf{Hình 2.14} & Sơ đồ Tuần tự Chi tiết -- UC\_SS6\_01 (Mô phỏng đợt tăng đột biến Metro Surge) & Mục 2.6 & \pageref{fig:seq-ss6-01} \\
    \hline
    \textbf{Hình 2.15} & Sơ đồ Tuần tự Chi tiết -- UC\_SS6\_02 (Dự báo nhu cầu theo giờ \& Phân tích hàng đợi) & Mục 2.6 & \pageref{fig:seq-ss6-02} \\
    \hline
    \textbf{Hình 2.16} & Sơ đồ Tuần tự Chi tiết -- UC\_SS7\_01 (Mô phỏng sự cố mất điện / lỗi trụ sạc) & Mục 2.7 & \pageref{fig:seq-ss7-01} \\
    \hline
    \textbf{Hình 2.17} & Sơ đồ Tuần tự Chi tiết -- UC\_SS7\_02 (Tự động phát cảnh báo \& Điều hướng 1-chạm) & Mục 2.7 & \pageref{fig:seq-ss7-02} \\
    \hline
    \textbf{Hình 3.1} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS1\_01 (Đặt \& Nhận xe) & Mục 3.1 & \pageref{fig:act-ss1-01} \\
    \hline
    \textbf{Hình 3.2} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS1\_02 (Trả xe 1-chiều) & Mục 3.1 & \pageref{fig:act-ss1-02} \\
    \hline
    \textbf{Hình 3.3} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS1\_03 (Hủy đặt xe) & Mục 3.1 & \pageref{fig:act-ss1-03} \\
    \hline
    \textbf{Hình 3.4} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS2\_01 (Đăng ký xe EV) & Mục 3.2 & \pageref{fig:act-ss2-01} \\
    \hline
    \textbf{Hình 3.5} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS2\_02 (Đặt chỗ đỗ/sạc) & Mục 3.2 & \pageref{fig:act-ss2-02} \\
    \hline
    \textbf{Hình 3.6} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS2\_03 (Check-in Hub) & Mục 3.2 & \pageref{fig:act-ss2-03} \\
    \hline
    \textbf{Hình 3.7} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS2\_04 (Check-out \& Thanh toán) & Mục 3.2 & \pageref{fig:act-ss2-04} \\
    \hline
    \textbf{Hình 3.8} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS3\_01 (Giám sát Hub) & Mục 3.3 & \pageref{fig:act-ss3-01} \\
    \hline
    \textbf{Hình 3.9} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS3\_02 (Cảnh báo quá tải) & Mục 3.3 & \pageref{fig:act-ss3-02} \\
    \hline
    \textbf{Hình 3.10} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS4\_01 (Lập lệnh điều xe) & Mục 3.4 & \pageref{fig:act-ss4-01} \\
    \hline
    \textbf{Hình 3.11} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS4\_02 (Xử lý sự cố kỹ thuật) & Mục 3.4 & \pageref{fig:act-ss4-02} \\
    \hline
    \textbf{Hình 3.12} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS5\_01 (Lập lịch ưu tiên sạc) & Mục 3.5 & \pageref{fig:act-ss5-01} \\
    \hline
    \textbf{Hình 3.13} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS5\_02 (Giám sát hàng đợi sạc) & Mục 3.5 & \pageref{fig:act-ss5-02} \\
    \hline
    \textbf{Hình 3.14} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS6\_01 (Mô phỏng Metro Surge) & Mục 3.6 & \pageref{fig:act-ss6-01} \\
    \hline
    \textbf{Hình 3.15} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS6\_02 (Dự báo nhu cầu theo giờ) & Mục 3.6 & \pageref{fig:act-ss6-02} \\
    \hline
    \textbf{Hình 3.16} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS7\_01 (Mô phỏng mất điện) & Mục 3.7 & \pageref{fig:act-ss7-01} \\
    \hline
    \textbf{Hình 3.17} & Sơ đồ Hoạt động Phân làn (Swimlane) -- UC\_SS7\_02 (Điều hướng 1-chạm) & Mục 3.7 & \pageref{fig:act-ss7-02} \\
    \hline
    \textbf{Hình 4.1} & Sơ đồ Trạng thái Vòng đời Phương tiện Điện dùng chung (EV Lifecycle) & Mục 4.1 & \pageref{fig:state-ev} \\
    \hline
    \textbf{Hình 4.2} & Sơ đồ Trạng thái Cổng sạc \& Phí chiếm dụng trụ sạc (Overstay Fee) & Mục 4.2 & \pageref{fig:state-charging} \\
    \hline
    \textbf{Hình 4.3} & Sơ đồ Trạng thái Vận hành Mạng lưới Mobility Hub (Metro Surge) & Mục 4.3 & \pageref{fig:state-hub} \\
    \hline
\end{longtable}

\vspace{0.4cm}
\subsection*{Danh mục bảng biểu (List of Tables)}
\begin{center}
\renewcommand{\arraystretch}{1.2}
\small
\begin{tabularx}{\textwidth}{|c|X|c|c|}
    \hline
    \textbf{Ký hiệu} & \textbf{Tên bảng biểu} & \textbf{Vị trí / Mục} & \textbf{Số trang} \\
    \hline
    \textbf{Bảng 0.1} & Danh sách Thành viên Nhóm 1, MSSV và Phân hệ Phụ trách & Trang bìa & 1 \\
    \hline
    \textbf{Bảng 1.1} & Ma trận Đáp ứng Yêu cầu Phi chức năng trên Giao diện UI/UX & Mục 1.1 & \pageref{tab:ui-nfr-matrix} \\
    \hline
    \textbf{Bảng 1.2} & Ma trận Phân bổ Phạm vi Hiện thực Prototype theo MoSCoW & Mục 1.2 & \pageref{tab:moscow-scope} \\
    \hline
    \textbf{Bảng 1.3} & Đặc tả Các Màn hình Chức năng Phân hệ Sinh viên & Mục 1.4 & \pageref{tab:ui-student-screens} \\
    \hline
    \textbf{Bảng 1.4} & Đặc tả Các Màn hình Bảng điều khiển Vận hành \& Điều phối & Mục 1.5 & \pageref{tab:ui-operator-screens} \\
    \hline
    \textbf{Bảng 1.5} & Đặc tả Màn hình Cấu hình \& Báo cáo Mô phỏng What-if & Mục 1.6 & \pageref{tab:ui-whatif-screens} \\
    \hline
    \textbf{Bảng 2.1} & Ma trận Phân công Thực hiện 17 Sequence Diagrams & Mục 2 & \pageref{tab:seq-assignment} \\
    \hline
    \textbf{Bảng 2.2} & Đặc tả Luồng Thông điệp Tương tác (Message Exchange) -- UC\_SS1\_01 & Mục 2.1 & \pageref{tab:msg-ss1-01} \\
    \hline
    \textbf{Bảng 3.1} & Ma trận Phân loại Luồng Nghiệp vụ trong 17 Activity Diagrams & Mục 3 & \pageref{tab:act-matrix} \\
    \hline
    \textbf{Bảng 4.1} & Bảng Đặc tả Chuyển Trạng thái Vòng đời Xe Điện & Mục 4.1 & \pageref{tab:state-ev-spec} \\
    \hline
    \textbf{Bảng 4.2} & Bảng Đặc tả Chuyển Trạng thái Cổng Sạc \& Trụ Sạc & Mục 4.2 & \pageref{tab:state-charger-spec} \\
    \hline
    \textbf{Bảng 4.3} & Bảng Đặc tả Chuyển Trạng thái Vận hành Mạng lưới Mobility Hub & Mục 4.3 & \pageref{tab:state-hub-spec} \\
    \hline
\end{tabularx}
\end{center}
\vspace*{\fill}
\newpage
"""

# Replace in text
start_idx = text.find(r"% ============================================================" + "\n" + r"%               DANH MỤC HÌNH ẢNH & BẢNG BIỂU")
end_idx = text.find(r"% ============================================================" + "\n" + r"%                       LỜI NÓI ĐẦU")

if start_idx != -1 and end_idx != -1:
    new_text = text[:start_idx] + figures_and_tables_section + text[end_idx:]
    with open("docs/report/submission_2/main.tex", "w", encoding="utf-8") as f:
        f.write(new_text)
    with open("docs/report/submission_2/REPORT_SUBMISSION_2.tex", "w", encoding="utf-8") as f:
        f.write(new_text)
    print("Successfully updated both List of Figures and List of Tables!")
else:
    print(f"Could not find section boundaries: start={start_idx}, end={end_idx}")
