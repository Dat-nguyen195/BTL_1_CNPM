import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Convert List of Figures from tabularx to longtable
    old_lof_pattern = re.compile(r'\\subsection\*\{Danh mục hình ảnh \(List of Figures\)\}.*?\\begin\{tabularx\}\{\\textwidth\}\{\|c\|X\|c\|c\|\}(.*?)\\end\{tabularx\}', re.DOTALL)
    
    def repl_lof(match):
        body = match.group(1).strip()
        # Clean up header
        # Find where table rows start (after first \hline)
        rows_match = re.search(r'\\hline\s*\\textbf\{Ký hiệu\}.*?\\hline', body, re.DOTALL)
        if rows_match:
            header_str = rows_match.group(0)
            rows_content = body[rows_match.end():].strip()
        else:
            header_str = "\\textbf{Ký hiệu} & \\textbf{Tên hình ảnh / Sơ đồ} & \\textbf{Vị trí / Mục} & \\textbf{Số trang} \\\\\n    \\hline"
            rows_content = body

        new_lof = f"""\\subsection*{{Danh mục hình ảnh (List of Figures)}}
\\renewcommand{{\\arraystretch}}{{1.15}}
\\small
\\begin{{longtable}}{{|c|p{{9.6cm}}|c|c|}}
    \\hline
    \\textbf{{Ký hiệu}} & \\textbf{{Tên hình ảnh / Sơ đồ}} & \\textbf{{Vị trí / Mục}} & \\textbf{{Số trang}} \\\\
    \\hline
    \\endfirsthead
    \\hline
    \\textbf{{Ký hiệu}} & \\textbf{{Tên hình ảnh / Sơ đồ}} & \\textbf{{Vị trí / Mục}} & \\textbf{{Số trang}} \\\\
    \\hline
    \\endhead
    \\hline
    \\endfoot
    {rows_content}
\\end{{longtable}}"""
        return new_lof

    content = old_lof_pattern.sub(repl_lof, content)

    # 2. Rewrite Section 1 completely with rich, realistic content and clean layout
    sec1_start = content.find(r"\section{Thiết kế Giao diện Người dùng -- UI Design \& Prototype Thực tế (Group Work)}")
    sec2_start = content.find(r"% ============================================================" + "\n" + r"%       MỤC 2: SƠ ĐỒ TUẦN TỰ")
    if sec2_start == -1:
        sec2_start = content.find(r"\section{Sơ đồ Tuần tự Chi tiết -- Sequence Diagrams")

    if sec1_start != -1 and sec2_start != -1:
        new_sec1 = r"""\section{Thiết kế Giao diện Người dùng -- UI Design \& Prototype Thực tế (Group Work)}

\subsection{Tổng quan nguyên tắc thiết kế UI/UX \& Điều hướng chung}
Hệ thống Smart E-Mobility Hub được xây dựng dựa trên nguyên lý tối giản thao tác, định hướng trải nghiệm người dùng hiện đại và tích hợp hoàn chỉnh các yêu cầu phi chức năng:
\begin{itemize}[nosep]
    \item \textbf{Đáp ứng đa nền tảng (NFR-07 Responsive):} Giao diện thích ứng linh hoạt từ màn hình điện thoại di động ($375\text{ px}$), máy tính bảng đến màn hình Dashboard điều hành lớn ($1920\text{ px}$).
    \item \textbf{Thao tác tối giản (NFR-08 User Journey):} Đảm bảo quy trình đặt xe hoặc đăng ký trụ sạc hoàn tất trong \textbf{không quá 03 bước tương tác chính}.
    \item \textbf{Bản địa hóa \& Trực quan (NFR-09 Usability):} 100\% giao diện hỗ trợ ngôn ngữ tiếng Việt chuẩn mực, tích hợp định dạng tiền tệ Việt Nam (VNĐ), mã màu phân định trạng thái pin (Xanh $\ge 50\%$, Vàng $20-49\%$, Đỏ $<20\%$) và mức độ lấp đầy Hub.
\end{itemize}

\begin{table}[H]
    \centering
    \renewcommand{\arraystretch}{1.25}
    \caption{Ma trận Đáp ứng Yêu cầu Phi chức năng trên Giao diện Người dùng}
    \label{tab:ui-nfr-matrix}
    \begin{tabularx}{\textwidth}{|l|l|X|}
        \hline
        \textbf{Mã NFR} & \textbf{Tiêu chí Phi chức năng} & \textbf{Giải pháp Hiện thực trên Giao diện UI/UX} \\
        \hline
        NFR-07 & Responsive đa kích thước & Tự động co giãn bố cục qua CSS Grid/Flexbox và Streamlit Layout columns. \\
        \hline
        NFR-08 & Đặt xe $\le 3$ bước & Bước 1: Chọn Hub \& Xe $\rightarrow$ Bước 2: Khóa cọc ví $\rightarrow$ Bước 3: Nhận mã QR/PIN. \\
        \hline
        NFR-09 & Ngôn ngữ \& Bản địa hóa & 100\% giao diện Tiếng Việt chuẩn, định dạng tiền tệ VNĐ và thời gian 24h. \\
        \hline
    \end{tabularx}
\end{table}

\subsection{Kế hoạch Hiện thực Hóa Prototype theo Mô hình MoSCoW (Cam kết $\ge 70\%$)}
Nhằm đảm bảo tính khả thi cao trong quá trình phát triển sản phẩm thực tế theo yêu cầu của môn học (hiện thực tối thiểu 70\% chức năng cốt lõi), nhóm tiến hành phân kỳ phạm vi tính năng thông qua ma trận \textbf{MoSCoW (Must-have, Should-have, Could-have, Won't-have)}. Toàn bộ các phân hệ từ SS1 đến SS5 thuộc phạm vi bắt buộc và ưu tiên cao ($85\%$ tổng khối lượng), trong khi các mô-đun mô phỏng nâng cao ở SS6 và SS7 đóng vai trò hoàn thiện năng lực phân tích.

\begin{table}[H]
    \centering
    \small
    \renewcommand{\arraystretch}{1.25}
    \caption{Ma trận Phân bổ Phạm vi Hiện thực Prototype theo MoSCoW (Cam kết $\ge 70\%$)}
    \label{tab:moscow-scope}
    \begin{tabularx}{\textwidth}{|l|c|X|c|}
        \hline
        \textbf{Phân loại MoSCoW} & \textbf{Tỷ trọng} & \textbf{Hạng mục Chức năng Hiện thực trong Prototype Streamlit} & \textbf{Mốc Nộp} \\
        \hline
        \textbf{Must-have} & $50\%$ & Đăng nhập VNU-SSO, Đặt cọc giữ xe 30p, Nhận xe (QR/PIN), Trả xe, Quyết toán ví nội bộ (SS1); Đăng ký xe EV cá nhân \& Check-in chỗ đỗ (SS2); Bản đồ giám sát 6 Hub thời gian thực (SS3). & Sub \#3 \& \#4 \\
        \hline
        \textbf{Should-have} & $25\%$ & Lập lệnh điều chuyển xe cân bằng mạng lưới, Báo cáo \& xử lý sự cố xe (SS4); Thuật toán sắp xếp hàng đợi sạc tự động theo SoC \& Phạt quá giờ Overstay Fee sau 15p (SS5). & Sub \#3 \& \#4 \\
        \hline
        \textbf{Could-have} & $15\%$ & Bảng điều khiển cấu hình tham số Monte Carlo mô phỏng Metro Surge (SS6) và Giả lập sự cố mất điện lưới trạm sạc \& Gợi ý điều hướng 1-chạm (SS7). & Sub \#4 \\
        \hline
        \textbf{Won't-have} & $10\%$ & Tích hợp phần cứng cảm biến IoT thực tế ngoài hiện trường (thay thế bằng API giả lập dữ liệu Telemetry thời gian thực). & Sau đồ án \\
        \hline
        \multicolumn{4}{|l|}{\textbf{Tổng mức độ cam kết hiện thực hóa của nhóm:} $\mathbf{90\%}$ khối lượng chức năng đặc tả.} \\
        \hline
    \end{tabularx}
\end{table}

\clearpage
\subsection{Sơ đồ Luồng Màn hình Điều hướng Tổng thể (Screen Navigation Flow)}
Sơ đồ dưới đây thể hiện luồng di chuyển tổng quan của người dùng từ bước đăng nhập định danh tập trung VNU-SSO đến các phân hệ nghiệp vụ tương ứng theo vai trò người dùng (Sinh viên vs Cán bộ Vận hành):

\begin{figure}[H]
    \centering
    \resizebox{0.72\textwidth}{!}{%
    \begin{tikzpicture}[
        node distance=0.85cm and 1.4cm,
        box/.style={rectangle, draw=blue!70!black, fill=blue!8, rounded corners=4pt, thick, align=center, font=\small\bfseries, minimum height=0.75cm, inner sep=5pt},
        subbox/.style={rectangle, draw=teal!70!black, fill=teal!8, rounded corners=4pt, thick, align=center, font=\small, minimum height=0.75cm, inner sep=5pt},
        opbox/.style={rectangle, draw=purple!70!black, fill=purple!8, rounded corners=4pt, thick, align=center, font=\small, minimum height=0.75cm, inner sep=5pt},
        arr/.style={-{Stealth[length=2.2mm]}, thick, draw=blue!80!black}
    ]
        % Root
        \node[box] (login) {Đăng nhập VNU-SSO\\(Xác thực tài khoản sinh viên / cán bộ)};
        
        % Branches
        \node[subbox, below left=0.9cm and 0.4cm of login] (student) {Cổng Sinh viên (Mobile UI)\\Đặt xe dùng chung \& Sạc cá nhân};
        \node[opbox, below right=0.9cm and 0.4cm of login] (operator) {Cổng Vận hành (Desktop UI)\\Giám sát Hub, Điều xe \& Lập lịch sạc};
        
        % Student Flow
        \node[subbox, below=0.75cm of student] (book) {Bản đồ 6 Hub \& Chọn xe\\(Thời gian thực)};
        \node[subbox, below=0.75cm of book] (qr) {Khóa cọc 50k \& Nhận QR/PIN\\(Hiệu lực 30 phút)};
        \node[subbox, below=0.75cm of qr] (return) {Cắm trả tại Hub bất kỳ\\\& Quyết toán ví e-Invoice};
        
        % Operator Flow
        \node[opbox, below=0.75cm of operator] (kpi) {Dashboard KPI Thời gian thực\\\& Cảnh báo quá tải (70\%/85\%)};
        \node[opbox, below=0.75cm of kpi] (dispatch) {Lệnh Điều xe \& Xử lý sự cố\\(Điều xe thừa $\rightarrow$ thiếu)};
        \node[opbox, below=0.75cm of dispatch] (whatif) {Mô phỏng What-if\\(Metro Surge \& Rerouting)};
        
        % Arrows
        \draw[arr] (login) -- (student);
        \draw[arr] (login) -- (operator);
        \draw[arr] (student) -- (book);
        \draw[arr] (book) -- (qr);
        \draw[arr] (qr) -- (return);
        \draw[arr] (operator) -- (kpi);
        \draw[arr] (kpi) -- (dispatch);
        \draw[arr] (dispatch) -- (whatif);
    \end{tikzpicture}%
    }
    \caption{Sơ đồ Luồng Màn hình Điều hướng Tổng thể (Screen Navigation Flow)}
    \label{fig:screen-flow}
\end{figure}

\clearpage
\subsection{Giao diện Thực tế Phân hệ Sinh viên (SS1 \& SS2)}
Phân hệ Sinh viên được triển khai trực tiếp trên ứng dụng web Streamlit (\texttt{src/components/student\_booking.py} và \texttt{src/components/personal\_ev.py}), hỗ trợ trải nghiệm tương tác với dữ liệu trạm Hub thời gian thực:

\subsubsection{Phân hệ SS1: Đặt xe \& Quản lý Chỗ đỗ Sinh viên (Hình \ref{fig:ui-ss1-real})}
Giao diện phân hệ SS1 thể hiện quy trình khép kín từ tra cứu đến nhận xe:
\begin{itemize}[nosep]
    \item \textbf{Định danh \& Ví điện tử:} Hiển thị danh tính sinh viên (Nguyễn Văn A - MSSV: 2211234), số dư ví khả dụng ($500.000\text{ VNĐ}$) và số dư tạm khóa cọc ($0\text{ VNĐ}$).
    \item \textbf{Hệ thống 4 Tabs nghiệp vụ:} Phân định rạch ròi 4 luồng thao tác: Đặt xe, Nhận xe (Pick-up), Trả xe \& Quyết toán, Hủy đặt xe.
    \item \textbf{Bước 1 -- Chọn Hub xuất phát:} Hiển thị tình trạng trạm KTX Khu A với các thẻ đo lường: $15/40$ chỗ đỗ trống, $4/10$ cổng sạc khả dụng, và $5$ xe điện sẵn sàng.
    \item \textbf{Bước 2 -- Tìm xe khả dụng:} Hỗ trợ bộ lọc loại phương tiện (E-Bike, E-Scooter, E-Car), thanh trượt mức pin tối thiểu ($\text{SoC} \ge 20\%$) và bảng danh sách xe trực quan.
    \item \textbf{Bước 3 -- Đặt giữ xe \& Khóa cọc 30 phút:} Lựa chọn xe cụ thể (\texttt{EV-A001} - Scooter, SoC 85\%), bảng giá thuê minh bạch (miễn phí 30 phút đầu, $1.000\text{ VNĐ/phút}$ sau 30p, cọc giữ chỗ $50.000\text{ VNĐ}$), hỗ trợ áp dụng mã giảm giá SVBK50.
    \item \textbf{Thông báo xác nhận thành công:} Tự động khóa $50.000\text{ VNĐ}$, sinh mã PIN 6 chữ số (\texttt{745768}) có hiệu lực trong 30 phút để sinh viên đến trạm mở khóa xe qua IoT.
\end{itemize}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,height=0.34\textheight,keepaspectratio]{screenshots/ss1_student_booking.png}
    \caption{Giao diện Thực tế Prototype: Đặt xe \& Quản lý Chỗ đỗ dành cho Sinh viên (Phân hệ SS1)}
    \label{fig:ui-ss1-real}
\end{figure}

\clearpage
\subsubsection{Phân hệ SS2: Đăng ký Phương tiện EV Cá nhân \& Quản lý Bãi đỗ (Hình \ref{fig:ui-ss2-real})}
Phân hệ SS2 cho phép sinh viên mang phương tiện điện cá nhân vào mạng lưới Hub để đỗ và sạc thông minh:
\begin{itemize}[nosep]
    \item \textbf{Hệ thống Tabs chức năng:} Gồm Đăng ký xe mới, Đặt chỗ \& Sạc, Danh sách xe đã đăng ký.
    \item \textbf{Biểu mẫu đăng ký phương tiện chuẩn hóa:} Thu thập đầy đủ thông tin định danh phương tiện gồm Họ tên chủ xe (Nguyễn Anh Tài), Mã số sinh viên (2213001), Biển số xe (59-X1 12345), Chủng loại phương tiện (scooter), Hãng/Model xe (VinFast Klara S 2026), Dung lượng pin thiết kế ($2.00\text{ kWh}$).
    \item \textbf{Kiểm soát an ninh \& Check-in thông minh:} Phương tiện sau khi đăng ký được cấp mã định danh \texttt{PEV-2026}, liên kết trực tiếp với mã QR Check-in để tự động nâng hạ barie ra vào trạm và lập lịch sạc theo biểu giá điện sinh viên.
\end{itemize}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,height=0.34\textheight,keepaspectratio]{screenshots/ss2_personal_ev.png}
    \caption{Giao diện Thực tế Prototype: Đăng ký Phương tiện EV Cá nhân \& Quản lý Bãi đỗ (Phân hệ SS2)}
    \label{fig:ui-ss2-real}
\end{figure}

\begin{table}[H]
    \centering
    \small
    \renewcommand{\arraystretch}{1.25}
    \caption{Đặc tả Các Màn hình Chức năng Phân hệ Sinh viên}
    \label{tab:ui-student-screens}
    \begin{tabularx}{\textwidth}{|l|l|X|}
        \hline
        \textbf{Màn hình} & \textbf{Mục đích Sử dụng} & \textbf{Các Thành phần Giao diện Chính} \\
        \hline
        M-01: Đăng nhập VNU-SSO & Xác thực danh tính sinh viên & Nút đăng nhập SSO, logo ĐHQG-HCM, xác thực 2 lớp OTP. \\
        \hline
        M-02: Bản đồ 6 Hub trung tâm & Định vị và kiểm tra trạng thái trạm & Bản đồ tương tác, thẻ đo lường số xe khả dụng và cổng sạc trống. \\
        \hline
        M-03: Đặt xe dùng chung (SS1) & Lập đơn đặt giữ xe 30 phút & Bộ chọn loại xe, bộ lọc mức pin $>20\%$, khóa cọc 50.000 VNĐ. \\
        \hline
        M-04: Nhận xe (Pick-up QR/PIN) & Mở khóa xe tại Hub xuất phát & Mã QR động, mã PIN 6 chữ số, đồng hồ đếm ngược 30 phút. \\
        \hline
        M-05: Đăng ký xe cá nhân (SS2) & Quản lý xe EV cá nhân vào Hub & Form nhập biển số, model xe, dung lượng pin và loại cổng sạc. \\
        \hline
        M-06: Check-in / Check-out bãi đỗ & Kiểm soát xe ra vào trạm & Quét QR check-in, tự động nâng hạ barie và tính phí đỗ/sạc tích hợp. \\
        \hline
    \end{tabularx}
\end{table}

\clearpage
\subsection{Giao diện Thực tế Phân hệ Vận hành \& Điều phối (SS3, SS4, SS5)}
Trung tâm giám sát và điều hành mạng lưới Hub (\texttt{hub\_monitor.py}, \texttt{dispatch\_incident.py}, \texttt{smart\_charging.py}) được tối ưu hóa cho màn hình lớn của Hub Operator:

\subsubsection{Phân hệ SS3: Giám sát Mạng lưới Hub Thời gian thực (Hình \ref{fig:ui-ss3-real})}
Màn hình giám sát trung tâm cung cấp góc nhìn toàn cảnh về năng lực vận hành:
\begin{itemize}[nosep]
    \item \textbf{Bộ thẻ KPI vận hành:} Tổng số xe hiện hữu trên mạng lưới ($40\text{ xe}$), tỷ lệ lấp đầy trung bình ($60.4\%$), tổng số chỗ trống khả dụng ($95/240\text{ chỗ}$), số lượng cổng sạc khả dụng ($25/59\text{ cổng}$).
    \item \textbf{Cảnh báo quá tải tự động (Visual Alert):} Hệ thống phát cảnh báo nổi bật màu vàng khi phát hiện trạm vượt ngưỡng $85\%$: \textit{"Hub KTX Khu B -- Tỉ lệ lấp đầy: 87\% $\rightarrow$ Cần điều phối!"}.
    \item \textbf{Bản đồ mạng lưới 6 Hub:} Phân bố địa lý thực tế tại ĐHQG-HCM, hỗ trợ phân loại màu sắc tải trọng và tích hợp chức năng \textbf{Bật/Tắt thiết bị (Activate/Deactivate)} theo thời gian thực.
\end{itemize}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,height=0.34\textheight,keepaspectratio]{screenshots/ss3_hub_monitor.png}
    \caption{Giao diện Thực tế Prototype: Bảng Điều khiển Giám sát Mạng lưới Hub Thời gian thực (Phân hệ SS3)}
    \label{fig:ui-ss3-real}
\end{figure}

\clearpage
\subsubsection{Phân hệ SS4: Điều phối Cân bằng Tải \& Xử lý Sự cố Kỹ thuật (Hình \ref{fig:ui-ss4-real})}
Hỗ trợ Operator xử lý trực tiếp tình trạng mất cân đối phương tiện và sự cố kỹ thuật:
\begin{itemize}[nosep]
    \item \textbf{Ma trận trạng thái 6 Hub:} Hiển thị chi tiết số lượng xe hiện có, chỗ trống, tỷ lệ lấp đầy và huy hiệu cảnh báo (Đỏ: Quá tải KTX Khu B $86.7\%$; Vàng: Mức cao KTX Khu A $62.5\%$; Xanh: Bình thường).
    \item \textbf{Biểu mẫu điều phối phương tiện:} Cho phép chọn Hub nguồn thừa xe, Hub đích thiếu xe, chọn danh sách xe điều chuyển (\texttt{EV-A001}, \texttt{EV-A003}), nhập lý do điều phối và xác nhận thực hiện.
    \item \textbf{Quản lý \& Nhật ký sự cố kỹ thuật:} Tiếp nhận phản ánh hư hỏng xe/cổng sạc, phân loại mức độ khẩn cấp (Khẩn cấp, Cao, Trung bình) và lưu vết lịch sử xử lý.
\end{itemize}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,height=0.34\textheight,keepaspectratio]{screenshots/ss4_dispatch_incident.png}
    \caption{Giao diện Thực tế Prototype: Điều phối Cân bằng Tải \& Xử lý Sự cố Kỹ thuật (Phân hệ SS4)}
    \label{fig:ui-ss4-real}
\end{figure}

\clearpage
\subsubsection{Phân hệ SS5: Lập lịch Sạc Thông minh \& Quản lý Hàng đợi (Hình \ref{fig:ui-ss5-real})}
Ứng dụng thuật toán lập lịch thông minh tối ưu hóa việc phân bổ công suất trạm sạc:
\begin{itemize}[nosep]
    \item \textbf{Thẻ đo lường hàng đợi sạc:} Tổng số xe chờ sạc ($14\text{ xe}$), số xe pin nguy hiểm $\text{SoC} < 20\%$ ($8\text{ xe}$), số lượng yêu cầu có liên kết lịch đặt xe trước của sinh viên.
    \item \textbf{Thuật toán ưu tiên đa mục tiêu:} Cộng $100$ điểm cho pin $<20\%$, cộng $60$ điểm cho xe có booking sinh viên, cộng điểm tuyến tính theo độ sâu xả pin $(100\% - \text{SoC}) \times 0.5$, áp dụng nguyên tắc FIFO khi đồng điểm.
    \item \textbf{Bảng hàng đợi trực quan:} Tô màu nền đỏ/hồng cho các xe ưu tiên đặc biệt gấp (\texttt{EV-B009} - điểm $177.5$, \texttt{EV-E005} - điểm $176.5$) và hiển thị thời gian yêu cầu chính xác.
    \item \textbf{Cơ chế phạt chiếm dụng cổng (Overstay Fee):} Tự động phát thông báo khi sạc đầy và tính phí phạt lũy tiến sau 15 phút ân hạn nhằm giải phóng trụ sạc.
\end{itemize}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,height=0.34\textheight,keepaspectratio]{screenshots/ss5_smart_charging.png}
    \caption{Giao diện Thực tế Prototype: Lập lịch Sạc Thông minh \& Quản lý Hàng đợi (Phân hệ SS5)}
    \label{fig:ui-ss5-real}
\end{figure}

\begin{table}[H]
    \centering
    \small
    \renewcommand{\arraystretch}{1.25}
    \caption{Đặc tả Các Màn hình Bảng điều khiển Vận hành \& Điều phối}
    \label{tab:ui-operator-screens}
    \begin{tabularx}{\textwidth}{|l|l|X|}
        \hline
        \textbf{Màn hình} & \textbf{Mục đích Sử dụng} & \textbf{Các Thành phần Giao diện Chính} \\
        \hline
        D-01: Bảng tổng quan KPIs (SS3) & Giám sát vận hành toàn đô thị & Thẻ đo lường số xe, tỷ lệ lấp đầy, cảnh báo ngưỡng tải $70\% / 85\%$. \\
        \hline
        D-02: Quản lý thiết bị (SS3) & Bật/Tắt cổng sạc và xe điện & Danh sách tài nguyên, nút Activate / Deactivate thiết bị thời gian thực. \\
        \hline
        D-03: Trung tâm điều phối xe (SS4) & Cân bằng lượng xe giữa các Hub & Bảng lệnh điều chuyển xe, chọn Hub nguồn / đích, chọn xe cần chuyển. \\
        \hline
        D-04: Quản lý sự cố kỹ thuật (SS4) & Tiếp nhận và khắc phục hỏng hóc & Danh sách sự cố, phân loại mức độ khẩn cấp, cập nhật trạng thái sửa chữa. \\
        \hline
        D-05: Lập lịch sạc thông minh (SS5) & Quản lý trụ sạc và hàng đợi & Hàng đợi sạc ưu tiên SoC, đồng hồ đếm ngược 15p ân hạn, tính phí Overstay Fee. \\
        \hline
    \end{tabularx}
\end{table}

\clearpage
\subsection{Giao diện Thực tế Phân hệ Mô phỏng What-if (SS6 \& SS7)}
Công cụ phân tích và giả lập chuyên sâu (\texttt{sim\_demand.py} và \texttt{sim\_infrastructure.py}) phục vụ công tác dự báo và chuẩn bị phương án ứng phó mạng lưới:

\subsubsection{Phân hệ SS6: Mô phỏng Nhu cầu Đột biến Metro Surge (Hình \ref{fig:ui-ss6-real})}
Giúp nhà vận hành thử nghiệm các kịch bản gia tăng hành khách đột ngột khi tuyến Metro Bến Thành -- Suối Tiên vận hành:
\begin{itemize}[nosep]
    \item \textbf{Cấu hình tham số linh hoạt:} Điều chỉnh tỷ lệ sinh viên đến cơ bản ($15\text{ SV/giờ}$), thanh trượt hệ số tăng đột biến (Surge Multiplier $1.00\times - 5.00\times$) và thời gian mô phỏng ($12\text{ giờ}$).
    \item \textbf{Biểu đồ Plotly tương tác 2 trục tung:} Cột màu lam hiển thị lượng sinh viên đến theo từng giờ, đường màu cam đỏ biểu diễn số lượng hàng đợi tích lũy dồn ứ tại các khung giờ cao điểm sáng (07:00--08:00) và tan trường (16:00--17:00 lên tới hơn 150 người).
    \item \textbf{Phân tích độ trễ:} Tự động tính toán giờ cao điểm cực đại, độ dài hàng đợi lớn nhất và thời gian chờ trung bình để hoạch định số xe cần điều chuyển dự phòng.
\end{itemize}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,height=0.34\textheight,keepaspectratio]{screenshots/ss6_sim_demand.png}
    \caption{Giao diện Thực tế Prototype: Bảng Điều khiển Mô phỏng Nhu cầu Metro Surge (Phân hệ SS6)}
    \label{fig:ui-ss6-real}
\end{figure}

\clearpage
\subsubsection{Phân hệ SS7: Mô phỏng Sự cố Hạ tầng \& Gợi ý Điều hướng 1-chạm (Hình \ref{fig:ui-ss7-real})}
Giả lập sự cố mất điện trạm sạc hoặc hư hỏng thiết bị và tự động kích hoạt kịch bản điều hướng:
\begin{itemize}[nosep]
    \item \textbf{Bảng điều khiển giả lập Port Failure:} Lựa chọn Hub bị sự cố (Hub Trường ĐH Bách Khoa) với số cổng bị hỏng ($3\text{ cổng}$) và bấm kích hoạt mô phỏng.
    \item \textbf{Nhật ký sự kiện thời gian thực:} Ghi nhận cảnh báo mất cổng sạc, tự động chuyển đổi trạng thái các xe đang sạc dở dang (\texttt{EV-D002}, \texttt{EV-D007}) về trạng thái chờ (\texttt{waiting}).
    \item \textbf{Đề xuất điều phối tự động \& Gợi ý 1-chạm:} Hệ thống tự động quét tìm Hub lân cận còn cổng sạc khả dụng (Hub Trường ĐH KHXH\&NV còn 6 cổng trống) và lập phương án chuyển hướng xe, hiển thị nút "Áp dụng kết quả mô phỏng" kèm thông báo điều hướng 1-chạm gửi đến ứng dụng di động của người dùng.
\end{itemize}

\begin{figure}[H]
    \centering
    \includegraphics[width=0.92\textwidth,height=0.34\textheight,keepaspectratio]{screenshots/ss7_sim_infrastructure.png}
    \caption{Giao diện Thực tế Prototype: Mô phỏng Sự cố Hạ tầng \& Gợi ý Điều hướng 1-chạm (Phân hệ SS7)}
    \label{fig:ui-ss7-real}
\end{figure}

\begin{table}[H]
    \centering
    \small
    \renewcommand{\arraystretch}{1.25}
    \caption{Đặc tả Màn hình Cấu hình \& Báo cáo Mô phỏng What-if}
    \label{tab:ui-whatif-screens}
    \begin{tabularx}{\textwidth}{|l|l|X|}
        \hline
        \textbf{Màn hình} & \textbf{Mục đích Sử dụng} & \textbf{Các Thành phần Giao diện Chính} \\
        \hline
        W-01: Cấu hình Metro Surge (SS6) & Thử nghiệm đợt tăng đột biến & Thanh trượt Surge Factor, số giờ mô phỏng, biểu đồ Plotly tương tác. \\
        \hline
        W-02: Phân tích hàng đợi (SS6) & Đánh giá mức độ thiếu hụt xe & KPI giờ cao điểm, độ dài hàng đợi cực đại, thời gian chờ trung bình. \\
        \hline
        W-03: Kích hoạt sự cố hạ tầng (SS7) & Giả lập mất điện / lỗi trạm sạc & Công tắc ngắt điện Hub, danh sách phiên xe đang di chuyển bị ảnh hưởng. \\
        \hline
        W-04: Gợi ý điều hướng 1-chạm (SS7) & Hỗ trợ sinh viên đổi lộ trình & Danh sách 02 Hub lân cận, nút chuyển trạm 1-chạm, miễn phí thêm 15 phút. \\
        \hline
    \end{tabularx}
\end{table}

\clearpage
"""
        content = content[:sec1_start] + new_sec1 + content[sec2_start:]
    else:
        print("Could not find section 1 boundaries!")

    # 3. Fix Sequence Diagrams, Activity Diagrams, State Diagrams to constrain height
    # Sequence diagrams:
    content = re.sub(
        r'\\includegraphics\[width=0\.88\\textwidth\]\{(Use-case detail-scenario/[^}]+?sequence\.png)\}',
        r'\\includegraphics[width=0.88\\textwidth,height=0.68\\textheight,keepaspectratio]{\1}',
        content
    )
    # Activity diagrams:
    content = re.sub(
        r'\\includegraphics\[width=0\.92\\textwidth\]\{(Use-case detail-scenario/[^}]+?activity\.png)\}',
        r'\\includegraphics[width=0.92\\textwidth,height=0.68\\textheight,keepaspectratio]{\1}',
        content
    )
    # State-chart diagrams:
    content = re.sub(
        r'\\includegraphics\[width=0\.92\\textwidth\]\{(Use-case detail-scenario/[^}]+?statechart\.png)\}',
        r'\\includegraphics[width=0.92\\textwidth,height=0.65\\textheight,keepaspectratio]{\1}',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Successfully updated {filepath}")

process_file("docs/report/submission_2/REPORT_SUBMISSION_2.tex")
process_file("docs/report/submission_2/REPORT_SUBMISSION_2.tex")
