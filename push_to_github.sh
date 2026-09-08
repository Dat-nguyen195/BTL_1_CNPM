#!/usr/bin/env bash
set -e

echo "🚀 Đang chuẩn bị push mã nguồn Smart E-Mobility Hub lên GitHub..."
cd "$(dirname "$0")"

# Đảm bảo remote origin trỏ đúng
git remote set-url origin https://github.com/Dat-nguyen195/BTL_1_CNPM

# Thực hiện push
echo "📤 Đang đẩy lên nhánh main..."
git push -u origin main

echo "✅ Hoàn tất! Repository đã được cập nhật thành công:"
echo "👉 https://github.com/Dat-nguyen195/BTL_1_CNPM"
