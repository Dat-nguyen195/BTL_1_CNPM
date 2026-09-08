#!/bin/bash
# ============================================================
# setup_github.sh – Script tự động khởi tạo Git & push lên GitHub
# Smart E-Mobility Hub – ĐHQG-HCM
# ============================================================

set -e  # Dừng ngay nếu có lỗi

echo "============================================================"
echo "🚲 Smart E-Mobility Hub – Git Setup Script"
echo "============================================================"
echo ""

# ── Bước 1: Khởi tạo Git ──────────────────────────
echo "📦 Bước 1: Khởi tạo Git repository..."
git init
echo "   ✅ Git đã được khởi tạo."
echo ""

# ── Bước 2: Tạo .gitignore ────────────────────────
echo "📝 Bước 2: Tạo file .gitignore..."
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
*.egg-info/
dist/
build/
*.egg

# Virtual Environment
venv/
env/
.venv/

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Streamlit
.streamlit/secrets.toml

# Misc
*.log
.env
EOF
echo "   ✅ .gitignore đã được tạo."
echo ""

# ── Bước 3: Thêm tất cả file vào staging ──────────
echo "📂 Bước 3: Thêm tất cả file vào staging area..."
git add .
echo "   ✅ Đã add tất cả file."
echo ""

# ── Bước 4: Commit lần đầu ────────────────────────
echo "💾 Bước 4: Tạo initial commit..."
git commit -m "feat: bootstrap project with 7 subsystems boilerplate and mock data"
echo "   ✅ Initial commit đã tạo."
echo ""

# ── Bước 5: Đổi branch thành main ─────────────────
echo "🌿 Bước 5: Đổi branch thành 'main'..."
git branch -M main
echo "   ✅ Branch hiện tại: main"
echo ""

# ============================================================
# HƯỚNG DẪN PUSH LÊN GITHUB
# ============================================================
echo "============================================================"
echo "🎉 HOÀN TẤT! Repository đã sẵn sàng."
echo "============================================================"
echo ""
echo "📌 BƯỚC TIẾP THEO – Push lên GitHub:"
echo ""
echo "   1. Tạo repository mới trên GitHub (KHÔNG tick 'Add README')"
echo "      → https://github.com/new"
echo ""
echo "   2. Chạy lệnh sau (thay <URL> bằng URL repo của bạn):"
echo ""
echo "      git remote add origin <URL>"
echo "      git push -u origin main"
echo ""
echo "   Ví dụ:"
echo "      git remote add origin https://github.com/your-team/smart-emobility-hub.git"
echo "      git push -u origin main"
echo ""
echo "============================================================"
echo "🚀 Chúc nhóm phát triển thành công!"
echo "============================================================"
