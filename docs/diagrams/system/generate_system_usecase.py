import os
import xml.etree.ElementTree as ET
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DRAWIO_FILE = os.path.join(BASE_DIR, "smartEhub.drawio")
SVG_FILE = os.path.join(BASE_DIR, "smartEhub.svg")
PNG_FILE = os.path.join(BASE_DIR, "smartEhub.png")
PDF_FILE = os.path.join(BASE_DIR, "smartEhub.pdf")

def create_drawio_xml():
    mxfile = ET.Element('mxfile', host='app.diagrams.net', modified='2026-10-19T22:50:00.000Z', agent='Antigravity UML Generator', version='24.0.0', type='device')
    diagram = ET.SubElement(mxfile, 'diagram', name='Sơ đồ Use-Case Tổng thể', id='smartEhub_v2')
    model = ET.SubElement(diagram, 'mxGraphModel', dx='1600', dy='1100', grid='1', gridSize='10', guides='1', tooltips='1', connect='1', arrows='1', fold='1', page='1', pageScale='1', pageWidth='1920', pageHeight='1200', math='0', shadow='0')
    root = ET.SubElement(model, 'root')
    
    ET.SubElement(root, 'mxCell', id='0')
    ET.SubElement(root, 'mxCell', id='1', parent='0')

    # Main System Boundary
    sys_bound = ET.SubElement(root, 'mxCell', id='sys_boundary', parent='1', 
        style='shape=mxgraph.sysml.package;whiteSpace=wrap;html=1;align=left;verticalAlign=top;spacingLeft=15;spacingTop=8;fillColor=#F8FAFC;strokeColor=#334155;strokeWidth=2.5;dashed=0;fontSize=16;fontStyle=1;fontColor=#0F172A;',
        value='HỆ THỐNG SMART E-MOBILITY HUB (ĐHQG-HCM)', vertex='1')
    ET.SubElement(sys_bound, 'mxGeometry', x='260', y='60', width='1220', height='1060', **{'as': 'geometry'})

    # Subsystem Packages
    subsystems = [
        ('pkg_ss1', 'Phân hệ SS1: Quản lý & Đặt xe điện dùng chung', 290, 110, 370, 290, '#ECFDF5', '#059669'),
        ('pkg_ss2', 'Phân hệ SS2: Dịch vụ Xe cá nhân & Bãi đỗ', 680, 110, 380, 290, '#FFFBEB', '#D97706'),
        ('pkg_shared', 'Dịch vụ Dùng chung Toàn hệ thống', 1080, 110, 370, 290, '#F1F5F9', '#475569'),
        ('pkg_ss3', 'Phân hệ SS3: Giám sát Mạng lưới & Vận hành', 290, 420, 370, 310, '#EFF6FF', '#2563EB'),
        ('pkg_ss4', 'Phân hệ SS4: Điều phối & Quản lý Sự cố', 680, 420, 380, 310, '#FDF2F8', '#DB2777'),
        ('pkg_ss5', 'Phân hệ SS5: Lập lịch Sạc Thông minh', 1080, 420, 370, 310, '#FAF5FF', '#7C3AED'),
        ('pkg_ss67', 'Phân hệ SS6 & SS7: Mô phỏng Kịch bản What-if', 290, 750, 560, 340, '#F0FDFA', '#0D9488'),
        ('pkg_admin', 'Quản trị Hệ thống & Phân quyền', 870, 750, 580, 340, '#F5F3FF', '#6D28D9'),
    ]

    for pid, pname, px, py, pw, ph, pfill, pstroke in subsystems:
        p_cell = ET.SubElement(root, 'mxCell', id=pid, parent='sys_boundary',
            style=f'shape=swimlane;whiteSpace=wrap;html=1;startSize=26;fillColor={pfill};strokeColor={pstroke};strokeWidth=1.5;fontSize=12;fontStyle=1;fontColor={pstroke};rounded=1;arcSize=4;',
            value=pname, vertex='1')
        ET.SubElement(p_cell, 'mxGeometry', x=str(px), y=str(py), width=str(pw), height=str(ph), **{'as': 'geometry'})

    # Use Cases
    use_cases = [
        # SS1
        ('uc_ss1_01', 'Tra cứu & Đặt giữ chỗ xe', 'pkg_ss1', 310, 150, 150, 50),
        ('uc_ss1_01b', 'Nhận xe qua QR/PIN', 'pkg_ss1', 485, 150, 155, 50),
        ('uc_ss1_02', 'Trả xe & Quyết toán', 'pkg_ss1', 310, 230, 150, 50),
        ('uc_ss1_03', 'Hủy đặt chỗ & Hoàn cọc', 'pkg_ss1', 485, 230, 155, 50),
        ('uc_ss1_note', 'Tự động hủy cọc quá 15p (Non-interactive)', 'pkg_ss1', 350, 310, 250, 35),
        # SS2
        ('uc_ss2_01', 'Đăng ký xe EV cá nhân', 'pkg_ss2', 705, 150, 155, 50),
        ('uc_ss2_02', 'Đặt trước chỗ đỗ & Lịch sạc', 'pkg_ss2', 885, 150, 155, 50),
        ('uc_ss2_03', 'Check-in bãi đỗ (QR)', 'pkg_ss2', 705, 230, 155, 50),
        ('uc_ss2_04', 'Check-out & Tính phí đỗ', 'pkg_ss2', 885, 230, 155, 50),
        # Shared Services
        ('uc_vnu_sso', 'Xác thực định danh\nVNU-SSO', 'pkg_shared', 1110, 160, 150, 55),
        ('uc_wallet', 'Quyết toán qua Ví điện tử nội bộ', 'pkg_shared', 1280, 160, 150, 55),
        # SS3
        ('uc_ss3_01', 'Giám sát mạng lưới Hub real-time', 'pkg_ss3', 310, 460, 160, 55),
        ('uc_ss3_02', 'Bật/Tắt & Quản lý thiết bị (Trụ/Xe)', 'pkg_ss3', 485, 460, 160, 55),
        ('uc_ss3_03', 'Tiếp nhận cảnh báo quá tải', 'pkg_ss3', 400, 550, 165, 50),
        # SS4
        ('uc_ss4_01', 'Lập lệnh điều chuyển xe cân bằng', 'pkg_ss4', 705, 470, 160, 55),
        ('uc_ss4_02', 'Báo cáo & Xử lý sự cố kỹ thuật', 'pkg_ss4', 885, 470, 160, 55),
        # SS5
        ('uc_ss5_01', 'Giám sát hàng đợi & Lịch sạc tối ưu', 'pkg_ss5', 1105, 470, 165, 55),
        ('uc_ss5_02', 'Cấu hình giới hạn công suất lưới (Peak Capping)', 'pkg_ss5', 1280, 470, 155, 55),
        ('uc_ss5_note', 'Background Scheduler:\n• Tối ưu SoC\n• Phạt quá giờ 15p', 'pkg_ss5', 1160, 560, 210, 55),
        # SS6 & SS7
        ('uc_sim_run', 'Thiết lập & Khởi chạy mô phỏng What-if', 'pkg_ss67', 320, 810, 180, 55),
        ('uc_sim_eval', 'Phân tích tác động & Đề xuất điều phối', 'pkg_ss67', 520, 810, 180, 55),
        ('uc_sim_note', 'Simulation Engines:\n• Metro Surge Generator\n• Grid Outage Simulator', 'pkg_ss67', 380, 900, 220, 55),
        # Admin
        ('uc_adm_users', 'Quản lý tài khoản &\nPhân quyền RBAC', 'pkg_admin', 900, 810, 160, 55),
        ('uc_adm_res', 'Quản lý danh mục\ntài nguyên ban đầu', 'pkg_admin', 1080, 810, 160, 55),
        ('uc_adm_conf', 'Cấu hình biểu phí\n& Chính sách hệ thống', 'pkg_admin', 1260, 810, 160, 55),
    ]

    for uid, uname, uparent, ux, uy, uw, uh in use_cases:
        if 'note' in uid:
            c = ET.SubElement(root, 'mxCell', id=uid, parent='sys_boundary',
                style='shape=note;whiteSpace=wrap;html=1;size=14;verticalAlign=middle;align=center;fillColor=#FEF3C7;strokeColor=#D97706;fontSize=10;fontColor=#92400E;dashed=1;',
                value=uname.replace('\n', '<br/>'), vertex='1')
        elif 'pkg_shared' in uparent:
            c = ET.SubElement(root, 'mxCell', id=uid, parent='sys_boundary',
                style='ellipse;whiteSpace=wrap;html=1;fillColor=#E2E8F0;strokeColor=#475569;strokeWidth=2;fontSize=11;fontStyle=1;fontColor=#1E293B;',
                value=uname.replace('\n', '<br/>'), vertex='1')
        else:
            c = ET.SubElement(root, 'mxCell', id=uid, parent='sys_boundary',
                style='ellipse;whiteSpace=wrap;html=1;fillColor=#FFFFFF;strokeColor=#1E293B;strokeWidth=1.5;fontSize=11;fontColor=#0F172A;',
                value=uname.replace('\n', '<br/>'), vertex='1')
        ET.SubElement(c, 'mxGeometry', x=str(ux), y=str(uy), width=str(uw), height=str(uh), **{'as': 'geometry'})

    # Actors outside boundary
    actors = [
        # Left Actors
        ('act_student', 'Sinh viên ĐHQG-HCM\n(Student)', 70, 210, 80, 110, '#0284C7'),
        ('act_tech', 'Kỹ thuật viên hiện trường\n(Technician)', 70, 540, 80, 110, '#D97706'),
        # Right Actors
        ('act_operator', 'Nhân viên Vận hành Hub\n(Hub Operator)', 1560, 360, 80, 110, '#2563EB'),
        ('act_admin', 'Quản trị viên Hệ thống\n(System Admin)', 1560, 780, 80, 110, '#7C3AED'),
        ('act_analyst', 'Chuyên viên Phân tích\n(Data Analyst)', 1560, 570, 80, 110, '#0D9488'),
        # Bottom Supporting Systems
        ('sys_sso', '«System»\nCổng VNU-SSO', 520, 1140, 140, 50, '#475569'),
        ('sys_iot', '«System»\nThiết bị & Cảm biến IoT', 1060, 1140, 160, 50, '#475569'),
    ]

    for aid, aname, ax, ay, aw, ah, acolor in actors:
        if aid.startswith('sys_'):
            a_cell = ET.SubElement(root, 'mxCell', id=aid, parent='1',
                style='shape=rectangle;rounded=1;whiteSpace=wrap;html=1;fillColor=#334155;strokeColor=#1E293B;strokeWidth=2;fontSize=11;fontStyle=1;fontColor=#FFFFFF;align=center;',
                value=aname.replace('\n', '<br/>'), vertex='1')
        else:
            a_cell = ET.SubElement(root, 'mxCell', id=aid, parent='1',
                style=f'shape=umlActor;verticalLabelPosition=bottom;verticalAlign=top;html=1;outlineConnect=0;fillColor={acolor};strokeColor={acolor};fontStyle=1;fontSize=11;fontColor=#0F172A;',
                value=aname.replace('\n', '<br/>'), vertex='1')
        ET.SubElement(a_cell, 'mxGeometry', x=str(ax), y=str(ay), width=str(aw), height=str(ah), **{'as': 'geometry'})

    # Connectors: Association
    associations = [
        ('act_student', 'uc_ss1_01'),
        ('act_student', 'uc_ss1_01b'),
        ('act_student', 'uc_ss1_02'),
        ('act_student', 'uc_ss1_03'),
        ('act_student', 'uc_ss2_01'),
        ('act_student', 'uc_ss2_02'),
        ('act_student', 'uc_ss2_03'),
        ('act_student', 'uc_ss2_04'),
        ('act_tech', 'uc_ss4_02'),
        ('act_tech', 'uc_ss3_02'),
        ('act_operator', 'uc_ss3_01'),
        ('act_operator', 'uc_ss3_02'),
        ('act_operator', 'uc_ss3_03'),
        ('act_operator', 'uc_ss4_01'),
        ('act_operator', 'uc_ss5_01'),
        ('act_operator', 'uc_sim_run'),
        ('act_analyst', 'uc_sim_run'),
        ('act_analyst', 'uc_sim_eval'),
        ('act_admin', 'uc_adm_users'),
        ('act_admin', 'uc_adm_res'),
        ('act_admin', 'uc_adm_conf'),
        ('act_admin', 'uc_ss5_02'),
        ('sys_sso', 'uc_vnu_sso'),
        ('sys_iot', 'uc_ss3_01'),
        ('sys_iot', 'uc_ss5_01'),
    ]

    edge_id = 1000
    for src, dst in associations:
        edge = ET.SubElement(root, 'mxCell', id=f'edge_{edge_id}', parent='1', source=src, target=dst,
            style='endArrow=none;html=1;strokeColor=#475569;strokeWidth=1.2;rounded=1;orthogonalLoop=1;jettySize=auto;', edge='1')
        ET.SubElement(edge, 'mxGeometry', relative='1', **{'as': 'geometry'})
        edge_id += 1

    # Include Relationships
    includes = [
        ('uc_ss1_01', 'uc_vnu_sso'),
        ('uc_ss2_01', 'uc_vnu_sso'),
        ('uc_adm_users', 'uc_vnu_sso'),
        ('uc_ss1_02', 'uc_wallet'),
        ('uc_ss2_04', 'uc_wallet'),
    ]

    for src, dst in includes:
        edge = ET.SubElement(root, 'mxCell', id=f'edge_{edge_id}', parent='1', source=src, target=dst,
            style='endArrow=classic;dashed=1;html=1;strokeColor=#0284C7;strokeWidth=1.5;rounded=1;edgeStyle=orthogonalEdgeStyle;', edge='1')
        ET.SubElement(edge, 'mxGeometry', relative='1', **{'as': 'geometry'})
        lbl = ET.SubElement(root, 'mxCell', id=f'lbl_{edge_id}', parent=f'edge_{edge_id}', connectable='0',
            style='edgeLabel;html=1;align=center;verticalAlign=middle;resizable=0;points=[];fontSize=10;fontColor=#0284C7;fontStyle=1;',
            value='«include»', vertex='1')
        ET.SubElement(lbl, 'mxGeometry', relative='1', **{'as': 'geometry'})
        edge_id += 1

    tree = ET.ElementTree(mxfile)
    tree.write(DRAWIO_FILE, encoding='utf-8', xml_declaration=True)
    print(f"Generated {DRAWIO_FILE} successfully.")

def create_svg():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1920 1220" width="1920" height="1220">
  <defs>
    <style>
      .title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 24px; font-weight: bold; fill: #0F172A; }
      .subtitle { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; fill: #475569; }
      .pkg-title { font-family: 'Segoe UI', Arial, sans-serif; font-size: 13px; font-weight: bold; }
      .uc-text { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11.5px; font-weight: 500; fill: #0F172A; text-anchor: middle; }
      .actor-name { font-family: 'Segoe UI', Arial, sans-serif; font-size: 12px; font-weight: bold; fill: #0F172A; text-anchor: middle; }
      .actor-role { font-family: 'Segoe UI', Arial, sans-serif; font-size: 11px; fill: #64748B; text-anchor: middle; }
      .note-text { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.5px; fill: #92400E; }
      .include-text { font-family: 'Segoe UI', Arial, sans-serif; font-size: 10.5px; font-weight: bold; fill: #0284C7; text-anchor: middle; }
    </style>
    <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="2" stdDeviation="3" flood-opacity="0.08"/>
    </filter>
    <filter id="card-shadow" x="-3%" y="-3%" width="106%" height="106%">
      <feDropShadow dx="0" dy="1" stdDeviation="2" flood-opacity="0.06"/>
    </filter>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M 0 1 L 10 5 L 0 9 z" fill="#0284C7"/>
    </marker>
  </defs>

  <rect width="100%" height="100%" fill="#FFFFFF"/>
  <rect x="250" y="20" width="1240" height="40" rx="8" fill="#F1F5F9" />
  <text x="870" y="47" class="title" text-anchor="middle">SƠ ĐỒ USE-CASE TỔNG THỂ HỆ THỐNG SMART E-MOBILITY HUB (ĐHQG-HCM)</text>

  <!-- SYSTEM BOUNDARY -->
  <rect x="250" y="75" width="1240" height="1035" rx="14" fill="#F8FAFC" stroke="#334155" stroke-width="2.5" filter="url(#shadow)"/>
  <rect x="250" y="75" width="380" height="32" rx="10" fill="#334155"/>
  <text x="270" y="97" font-family="'Segoe UI', Arial" font-size="13" font-weight="bold" fill="#FFFFFF">SYSTEM BOUNDARY: Smart E-Mobility Hub</text>

  <!-- SS1: Shared EV Booking -->
  <g transform="translate(280, 120)">
    <rect width="360" height="280" rx="10" fill="#ECFDF5" stroke="#059669" stroke-width="1.8" filter="url(#card-shadow)"/>
    <path d="M 0 0 L 260 0 L 275 24 L 0 24 Z" fill="#059669"/>
    <text x="14" y="17" class="pkg-title" fill="#FFFFFF">SS1: Quản lý &amp; Đặt xe điện dùng chung</text>
    <ellipse cx="90" cy="70" rx="75" ry="24" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
    <text x="90" y="74" class="uc-text">Tra cứu &amp; Đặt xe điện</text>
    <ellipse cx="265" cy="70" rx="78" ry="24" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
    <text x="265" y="74" class="uc-text">Nhận xe (QR/PIN)</text>
    <ellipse cx="90" cy="140" rx="75" ry="24" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
    <text x="90" y="144" class="uc-text">Trả xe &amp; Quyết toán</text>
    <ellipse cx="265" cy="140" rx="78" ry="24" fill="#FFFFFF" stroke="#059669" stroke-width="1.5"/>
    <text x="265" y="144" class="uc-text">Hủy đặt xe &amp; Hoàn cọc</text>
    <rect x="25" y="200" width="310" height="58" rx="6" fill="#FEF3C7" stroke="#D97706" stroke-dasharray="4 3"/>
    <text x="35" y="222" class="note-text" font-weight="bold">⚙ Background Service (Non-interactive):</text>
    <text x="35" y="242" class="note-text">• Tự động hủy cọc &amp; phạt nếu không nhận xe sau 15p</text>
  </g>

  <!-- SS2: Personal EV & Parking -->
  <g transform="translate(665, 120)">
    <rect width="365" height="280" rx="10" fill="#FFFBEB" stroke="#D97706" stroke-width="1.8" filter="url(#card-shadow)"/>
    <path d="M 0 0 L 260 0 L 275 24 L 0 24 Z" fill="#D97706"/>
    <text x="14" y="17" class="pkg-title" fill="#FFFFFF">SS2: Dịch vụ Xe cá nhân &amp; Bãi đỗ</text>
    <ellipse cx="95" cy="70" rx="80" ry="24" fill="#FFFFFF" stroke="#D97706" stroke-width="1.5"/>
    <text x="95" y="74" class="uc-text">Đăng ký xe EV cá nhân</text>
    <ellipse cx="270" cy="70" rx="80" ry="24" fill="#FFFFFF" stroke="#D97706" stroke-width="1.5"/>
    <text x="270" y="74" class="uc-text">Đặt trước chỗ đỗ &amp; sạc</text>
    <ellipse cx="95" cy="140" rx="80" ry="24" fill="#FFFFFF" stroke="#D97706" stroke-width="1.5"/>
    <text x="95" y="144" class="uc-text">Check-in bãi đỗ (QR)</text>
    <ellipse cx="270" cy="140" rx="80" ry="24" fill="#FFFFFF" stroke="#D97706" stroke-width="1.5"/>
    <text x="270" y="144" class="uc-text">Check-out &amp; Quyết toán</text>
    <rect x="25" y="200" width="315" height="58" rx="6" fill="#FEF3C7" stroke="#D97706" stroke-dasharray="4 3"/>
    <text x="35" y="222" class="note-text" font-weight="bold">⚙ Barrier Control (IoT Non-interactive):</text>
    <text x="35" y="242" class="note-text">• Tự động nâng/hạ barie theo tín hiệu quét hợp lệ</text>
  </g>

  <!-- SHARED SERVICES -->
  <g transform="translate(1055, 120)">
    <rect width="410" height="280" rx="10" fill="#F1F5F9" stroke="#475569" stroke-width="1.8" filter="url(#card-shadow)"/>
    <path d="M 0 0 L 250 0 L 265 24 L 0 24 Z" fill="#475569"/>
    <text x="14" y="17" class="pkg-title" fill="#FFFFFF">Dịch vụ Dùng chung Toàn hệ thống</text>
    <ellipse cx="110" cy="90" rx="95" ry="30" fill="#E2E8F0" stroke="#0284C7" stroke-width="2.2"/>
    <text x="110" y="87" class="uc-text" font-weight="bold" fill="#0369A1">Xác thực định danh</text>
    <text x="110" y="103" class="uc-text" font-weight="bold" fill="#0369A1">VNU-SSO</text>
    <ellipse cx="300" cy="90" rx="95" ry="30" fill="#E2E8F0" stroke="#059669" stroke-width="2.2"/>
    <text x="300" y="87" class="uc-text" font-weight="bold" fill="#065F46">Quyết toán qua</text>
    <text x="300" y="103" class="uc-text" font-weight="bold" fill="#065F46">Ví điện tử nội bộ</text>
    <rect x="20" y="160" width="370" height="98" rx="6" fill="#FFFFFF" stroke="#94A3B8"/>
    <text x="30" y="182" class="subtitle" font-weight="bold">Ghi chú quan hệ «include» chuẩn:</text>
    <text x="30" y="202" class="subtitle">• Đặt xe &amp; Đăng ký cá nhân «include» Xác thực SSO</text>
    <text x="30" y="222" class="subtitle">• Trả xe &amp; Check-out «include» Quyết toán Ví</text>
    <text x="30" y="242" class="subtitle">• Không lạm dụng include cho luồng tuần tự</text>
  </g>

  <!-- SS3: Monitoring & Real-time Operations -->
  <g transform="translate(280, 425)">
    <rect width="360" height="295" rx="10" fill="#EFF6FF" stroke="#2563EB" stroke-width="1.8" filter="url(#card-shadow)"/>
    <path d="M 0 0 L 270 0 L 285 24 L 0 24 Z" fill="#2563EB"/>
    <text x="14" y="17" class="pkg-title" fill="#FFFFFF">SS3: Giám sát Mạng lưới &amp; Vận hành</text>
    <ellipse cx="180" cy="70" rx="140" ry="25" fill="#FFFFFF" stroke="#2563EB" stroke-width="1.5"/>
    <text x="180" y="74" class="uc-text">Giám sát bản đồ &amp; Trạng thái Hub</text>
    <ellipse cx="180" cy="140" rx="150" ry="26" fill="#FEF2F2" stroke="#DC2626" stroke-width="2"/>
    <text x="180" y="137" class="uc-text" font-weight="bold" fill="#991B1B">Bật / Tắt &amp; Quản lý thiết bị</text>
    <text x="180" y="152" class="uc-text" fill="#991B1B">(Activate / Deactivate Trụ &amp; Xe)</text>
    <ellipse cx="180" cy="210" rx="140" ry="24" fill="#FFFFFF" stroke="#2563EB" stroke-width="1.5"/>
    <text x="180" y="214" class="uc-text">Tiếp nhận cảnh báo phân cấp quá tải</text>
    <text x="180" y="265" font-family="'Segoe UI', Arial" font-size="11" fill="#1E40AF" text-anchor="middle" font-style="italic">Thao tác trực tiếp trên danh sách thời gian thực</text>
  </g>

  <!-- SS4: Dispatch & Incident -->
  <g transform="translate(665, 425)">
    <rect width="365" height="295" rx="10" fill="#FDF2F8" stroke="#DB2777" stroke-width="1.8" filter="url(#card-shadow)"/>
    <path d="M 0 0 L 260 0 L 275 24 L 0 24 Z" fill="#DB2777"/>
    <text x="14" y="17" class="pkg-title" fill="#FFFFFF">SS4: Điều phối &amp; Quản lý Sự cố</text>
    <ellipse cx="182" cy="80" rx="145" ry="26" fill="#FFFFFF" stroke="#DB2777" stroke-width="1.5"/>
    <text x="182" y="84" class="uc-text">Lập lệnh điều chuyển xe cân bằng tải</text>
    <ellipse cx="182" cy="165" rx="145" ry="26" fill="#FFFFFF" stroke="#DB2777" stroke-width="1.5"/>
    <text x="182" y="169" class="uc-text">Báo cáo &amp; Tiếp nhận xử lý sự cố</text>
    <rect x="25" y="220" width="315" height="55" rx="6" fill="#FEF3C7" stroke="#D97706" stroke-dasharray="4 3"/>
    <text x="35" y="242" class="note-text" font-weight="bold">⚙ Khóa phương tiện tự động (INCIDENT):</text>
    <text x="35" y="258" class="note-text">• Ẩn lập tức khỏi SS1 khi tiếp nhận sự cố</text>
  </g>

  <!-- SS5: Smart Charging -->
  <g transform="translate(1055, 425)">
    <rect width="410" height="295" rx="10" fill="#FAF5FF" stroke="#7C3AED" stroke-width="1.8" filter="url(#card-shadow)"/>
    <path d="M 0 0 L 260 0 L 275 24 L 0 24 Z" fill="#7C3AED"/>
    <text x="14" y="17" class="pkg-title" fill="#FFFFFF">SS5: Lập lịch Sạc Thông minh</text>
    <ellipse cx="205" cy="70" rx="160" ry="26" fill="#FFFFFF" stroke="#7C3AED" stroke-width="1.5"/>
    <text x="205" y="74" class="uc-text">Giám sát hàng đợi &amp; Tiến độ sạc xe</text>
    <ellipse cx="205" cy="135" rx="160" ry="26" fill="#FFFFFF" stroke="#7C3AED" stroke-width="1.5"/>
    <text x="205" y="139" class="uc-text">Cấu hình giới hạn công suất lưới (Peak Capping)</text>
    <rect x="20" y="185" width="370" height="90" rx="6" fill="#FEF3C7" stroke="#D97706" stroke-dasharray="4 3"/>
    <text x="30" y="206" class="note-text" font-weight="bold">⚙ Core Optimization Engine (Non-interactive FR):</text>
    <text x="30" y="225" class="note-text">• Tự động xếp lịch tối ưu dựa trên SoC &amp; Biểu giá điện</text>
    <text x="30" y="244" class="note-text">• Tự động phạt Overstay Fee sau 15 phút ân hạn</text>
    <text x="30" y="263" class="note-text">• Tự động đẩy thông báo khi có cổng sạc trống</text>
  </g>

  <!-- SS6 & SS7: What-if Simulation -->
  <g transform="translate(280, 745)">
    <rect width="560" height="340" rx="10" fill="#F0FDFA" stroke="#0D9488" stroke-width="1.8" filter="url(#card-shadow)"/>
    <path d="M 0 0 L 320 0 L 335 24 L 0 24 Z" fill="#0D9488"/>
    <text x="14" y="17" class="pkg-title" fill="#FFFFFF">SS6 &amp; SS7: Mô phỏng Kịch bản What-if</text>
    <ellipse cx="280" cy="80" rx="180" ry="28" fill="#FFFFFF" stroke="#0D9488" stroke-width="1.5"/>
    <text x="280" y="77" class="uc-text" font-weight="bold">Thiết lập &amp; Khởi chạy mô phỏng What-if</text>
    <text x="280" y="93" class="uc-text" fill="#0F766E">(Metro Demand Surge &amp; Lỗi mất điện trạm)</text>
    <ellipse cx="280" cy="165" rx="180" ry="28" fill="#FFFFFF" stroke="#0D9488" stroke-width="1.5"/>
    <text x="280" y="162" class="uc-text" font-weight="bold">Phân tích tác động phụ tải &amp;</text>
    <text x="280" y="178" class="uc-text" fill="#0F766E">Đề xuất phương án điều phối mạng lưới</text>
    <rect x="30" y="225" width="500" height="95" rx="6" fill="#FEF3C7" stroke="#D97706" stroke-dasharray="4 3"/>
    <text x="45" y="248" class="note-text" font-weight="bold">⚙ Non-interactive Simulation Subcomponents (Point 3):</text>
    <text x="45" y="268" class="note-text">• Hệ thống tự động snapshot dữ liệu lưới điện &amp; vị trí xe hiện tại</text>
    <text x="45" y="288" class="note-text">• Thuật toán Monte Carlo tự động tính toán ma trận phân bổ phụ tải 24h</text>
    <text x="45" y="308" class="note-text">• Tự động sinh lộ trình gợi ý điều hướng thông minh (Auto-rerouting)</text>
  </g>

  <!-- ADMIN & GOVERNANCE -->
  <g transform="translate(865, 745)">
    <rect width="600" height="340" rx="10" fill="#F5F3FF" stroke="#6D28D9" stroke-width="1.8" filter="url(#card-shadow)"/>
    <path d="M 0 0 L 300 0 L 315 24 L 0 24 Z" fill="#6D28D9"/>
    <text x="14" y="17" class="pkg-title" fill="#FFFFFF">Quản trị Hệ thống &amp; Phân quyền (Admin Scope)</text>
    <ellipse cx="300" cy="75" rx="200" ry="28" fill="#EDE9FE" stroke="#6D28D9" stroke-width="2"/>
    <text x="300" y="72" class="uc-text" font-weight="bold" fill="#5B21B6">Quản lý Tài khoản &amp; Phân quyền RBAC</text>
    <text x="300" y="88" class="uc-text" fill="#5B21B6">(Student, Operator, Technician, Analyst, Admin)</text>
    <ellipse cx="300" cy="155" rx="200" ry="28" fill="#EDE9FE" stroke="#6D28D9" stroke-width="2"/>
    <text x="300" y="152" class="uc-text" font-weight="bold" fill="#5B21B6">Quản lý Danh mục Tài nguyên ban đầu</text>
    <text x="300" y="168" class="uc-text" fill="#5B21B6">(Cấu hình Hub mới, Đăng ký trụ sạc &amp; Đội xe)</text>
    <ellipse cx="300" cy="235" rx="200" ry="28" fill="#EDE9FE" stroke="#6D28D9" stroke-width="2"/>
    <text x="300" y="232" class="uc-text" font-weight="bold" fill="#5B21B6">Cấu hình Biểu phí &amp; Ngưỡng vận hành</text>
    <text x="300" y="248" class="uc-text" fill="#5B21B6">(Biểu giá điện, Cước quá giờ, Ngưỡng cảnh báo tải)</text>
    <text x="300" y="305" font-family="'Segoe UI', Arial" font-size="11.5" fill="#6D28D9" text-anchor="middle" font-weight="bold">Phân định rõ: Admin cấu hình mức hệ thống, Operator vận hành thời gian thực</text>
  </g>

  <!-- ACTORS -->
  <g transform="translate(100, 220)">
    <circle cx="45" cy="25" r="16" fill="#0284C7"/>
    <path d="M 45 41 L 45 75 M 25 52 L 65 52 M 45 75 L 25 105 M 45 75 L 65 105" stroke="#0284C7" stroke-width="3" stroke-linecap="round"/>
    <text x="45" y="125" class="actor-name">Sinh viên ĐHQG-HCM</text>
    <text x="45" y="142" class="actor-role">End-User (Mobile App)</text>
  </g>

  <g transform="translate(100, 560)">
    <circle cx="45" cy="25" r="16" fill="#D97706"/>
    <path d="M 45 41 L 45 75 M 25 52 L 65 52 M 45 75 L 25 105 M 45 75 L 65 105" stroke="#D97706" stroke-width="3" stroke-linecap="round"/>
    <text x="45" y="125" class="actor-name">Kỹ thuật viên</text>
    <text x="45" y="142" class="actor-role">Field Staff (Mobile/Web)</text>
  </g>

  <g transform="translate(1620, 320)">
    <circle cx="50" cy="25" r="16" fill="#2563EB"/>
    <path d="M 50 41 L 50 75 M 30 52 L 70 52 M 50 75 L 30 105 M 50 75 L 70 105" stroke="#2563EB" stroke-width="3" stroke-linecap="round"/>
    <text x="50" y="125" class="actor-name">Nhân viên Vận hành Hub</text>
    <text x="50" y="142" class="actor-role">Hub Operator (Real-time Console)</text>
  </g>

  <g transform="translate(1620, 580)">
    <circle cx="50" cy="25" r="16" fill="#0D9488"/>
    <path d="M 50 41 L 50 75 M 30 52 L 70 52 M 50 75 L 30 105 M 50 75 L 70 105" stroke="#0D9488" stroke-width="3" stroke-linecap="round"/>
    <text x="50" y="125" class="actor-name">Chuyên viên Phân tích</text>
    <text x="50" y="142" class="actor-role">Data / Strategic Analyst</text>
  </g>

  <g transform="translate(1620, 830)">
    <circle cx="50" cy="25" r="16" fill="#7C3AED"/>
    <path d="M 50 41 L 50 75 M 30 52 L 70 52 M 50 75 L 30 105 M 50 75 L 70 105" stroke="#7C3AED" stroke-width="3" stroke-linecap="round"/>
    <text x="50" y="125" class="actor-name">Quản trị viên Hệ thống</text>
    <text x="50" y="142" class="actor-role">System Admin (RBAC &amp; Config)</text>
  </g>

  <!-- SUPPORTING SYSTEMS -->
  <g transform="translate(560, 1130)">
    <rect width="260" height="50" rx="8" fill="#1E293B" stroke="#0F172A" stroke-width="2"/>
    <text x="130" y="24" font-family="'Segoe UI', Arial" font-size="11" fill="#94A3B8" text-anchor="middle">«External System»</text>
    <text x="130" y="41" font-family="'Segoe UI', Arial" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Cổng Xác thực VNU-SSO</text>
  </g>

  <g transform="translate(940, 1130)">
    <rect width="280" height="50" rx="8" fill="#1E293B" stroke="#0F172A" stroke-width="2"/>
    <text x="140" y="24" font-family="'Segoe UI', Arial" font-size="11" fill="#94A3B8" text-anchor="middle">«External Telemetry System»</text>
    <text x="140" y="41" font-family="'Segoe UI', Arial" font-size="13" font-weight="bold" fill="#FFFFFF" text-anchor="middle">Hệ thống Trạm sạc &amp; Cảm biến IoT</text>
  </g>

  <!-- SOLID LINES (ASSOCIATIONS) -->
  <path d="M 180 270 C 230 240, 280 210, 370 190" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 180 280 C 230 270, 280 260, 370 260" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 180 290 C 350 290, 500 240, 760 190" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 180 300 C 350 320, 500 280, 760 260" fill="none" stroke="#64748B" stroke-width="1.3"/>

  <path d="M 180 610 C 220 580, 240 540, 460 565" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 180 630 C 350 630, 500 600, 847 590" fill="none" stroke="#64748B" stroke-width="1.3"/>

  <path d="M 1620 370 C 1450 420, 950 460, 460 495" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 1620 380 C 1450 480, 950 540, 460 565" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 1620 390 C 1400 480, 1100 500, 847 505" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 1620 400 C 1500 450, 1400 480, 1260 495" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 1620 410 C 1400 650, 900 800, 560 825" fill="none" stroke="#64748B" stroke-width="1.3"/>

  <path d="M 1620 640 C 1300 700, 950 780, 560 825" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 1620 650 C 1300 750, 950 850, 560 910" fill="none" stroke="#64748B" stroke-width="1.3"/>

  <path d="M 1620 880 C 1500 850, 1400 830, 1165 820" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 1620 890 C 1500 880, 1400 880, 1165 900" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 1620 900 C 1500 930, 1400 950, 1165 980" fill="none" stroke="#64748B" stroke-width="1.3"/>
  <path d="M 1620 870 C 1520 650, 1420 590, 1260 560" fill="none" stroke="#64748B" stroke-width="1.3"/>

  <path d="M 690 1130 L 1165 240" fill="none" stroke="#475569" stroke-width="1.4" stroke-dasharray="3 3"/>
  <path d="M 1080 1130 C 1080 850, 950 560, 460 495" fill="none" stroke="#475569" stroke-width="1.4" stroke-dasharray="3 3"/>
  <path d="M 1080 1130 C 1150 900, 1220 650, 1260 495" fill="none" stroke="#475569" stroke-width="1.4" stroke-dasharray="3 3"/>

  <!-- DASHED INCLUDES -->
  <path d="M 445 190 C 650 160, 900 180, 1070 210" fill="none" stroke="#0284C7" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#arrow)"/>
  <rect x="710" y="165" width="70" height="18" rx="4" fill="#FFFFFF" stroke="#0284C7" stroke-width="1"/>
  <text x="745" y="178" class="include-text">«include»</text>

  <path d="M 840 190 C 920 180, 1000 190, 1070 210" fill="none" stroke="#0284C7" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#arrow)"/>
  <rect x="930" y="175" width="70" height="18" rx="4" fill="#FFFFFF" stroke="#0284C7" stroke-width="1"/>
  <text x="965" y="188" class="include-text">«include»</text>

  <path d="M 445 260 C 700 290, 1050 270, 1260 210" fill="none" stroke="#059669" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#arrow)"/>
  <rect x="830" y="270" width="70" height="18" rx="4" fill="#FFFFFF" stroke="#059669" stroke-width="1"/>
  <text x="865" y="283" class="include-text" fill="#059669">«include»</text>

  <path d="M 1015 260 C 1100 260, 1180 240, 1260 210" fill="none" stroke="#059669" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#arrow)"/>
  <rect x="1115" y="240" width="70" height="18" rx="4" fill="#FFFFFF" stroke="#059669" stroke-width="1"/>
  <text x="1150" y="253" class="include-text" fill="#059669">«include»</text>

  <path d="M 1165 820 C 1165 600, 1165 400, 1165 240" fill="none" stroke="#0284C7" stroke-width="1.6" stroke-dasharray="5 4" marker-end="url(#arrow)"/>
  <rect x="1130" y="520" width="70" height="18" rx="4" fill="#FFFFFF" stroke="#0284C7" stroke-width="1"/>
  <text x="1165" y="533" class="include-text">«include»</text>
</svg>'''

    with open(SVG_FILE, 'w', encoding='utf-8') as f:
        f.write(svg)
    print(f"Generated {SVG_FILE} successfully.")

def export_png_and_pdf():
    cmd = f'google-chrome --headless --disable-gpu --window-size=2400,1525 --screenshot="{PNG_FILE}" "{SVG_FILE}"'
    os.system(cmd)
    
    if os.path.exists(PNG_FILE) and os.path.getsize(PNG_FILE) > 1000:
        print(f"Generated {PNG_FILE} successfully ({os.path.getsize(PNG_FILE)} bytes).")
        im = Image.open(PNG_FILE).convert('RGB')
        im.save(PDF_FILE, 'PDF', resolution=150.0)
        print(f"Generated {PDF_FILE} successfully ({os.path.getsize(PDF_FILE)} bytes).")
    else:
        print("Error generating PNG from SVG!")

if __name__ == '__main__':
    create_drawio_xml()
    create_svg()
    export_png_and_pdf()
