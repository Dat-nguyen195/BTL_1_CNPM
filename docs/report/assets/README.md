# Shared Report Assets

Thư mục lưu trữ các tài nguyên dùng chung (hình ảnh, logo, template bìa) cho tất cả các báo cáo nộp định kỳ (`submission_1`, `submission_2`, `submission_3`, `submission_4`).

## Danh mục tài nguyên:
- `mau.png`: Logo chuẩn Đại học Bách Khoa – ĐHQG-HCM (độ phân giải cao: 3508 x 2481) dùng cho trang bìa các bài báo cáo LaTeX.

## Hướng dẫn sử dụng trong mã LaTeX:
Trong bất kỳ file `.tex` nào thuộc các thư mục con (`submission_x/`), bạn có thể chèn `mau.png` theo một trong các cách sau:

### Cách 1 (Khuyến nghị chuẩn LaTeX):
Khai báo đường dẫn tìm kiếm hình ảnh ở phần Preamble:
```latex
\usepackage{graphicx}
\graphicspath{{../assets/}{../../diagrams/}{./}}
```
Sau đó gọi hình bình thường:
```latex
\includegraphics[width=8cm]{mau.png}
```

### Cách 2 (Dùng trực tiếp symlink có sẵn):
Mỗi thư mục `submission_x/` đã được tạo sẵn symlink `mau.png` trỏ về `../assets/mau.png`, do đó bạn có thể viết trực tiếp:
```latex
\includegraphics[width=8cm]{mau.png}
```
hoặc:
```latex
\includegraphics[width=8cm]{../assets/mau.png}
```
