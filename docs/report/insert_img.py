import re

with open("REPORT_SUBMISSION_1.md", "r", encoding="utf-8") as f:
    content = f.read()

img_md = """
## SƠ ĐỒ USE-CASE TỔNG THỂ HỆ THỐNG

![Sơ đồ Use-Case Tổng thể của Hệ thống](./diagrams/system/smartEhub.png)

"""

# Insert before "## 3. MẠNG LƯỚI YÊU CẦU CHỨC NĂNG"
content = content.replace("## 3. MẠNG LƯỚI YÊU CẦU CHỨC NĂNG", img_md + "## 3. MẠNG LƯỚI YÊU CẦU CHỨC NĂNG")

with open("REPORT_SUBMISSION_1.md", "w", encoding="utf-8") as f:
    f.write(content)
