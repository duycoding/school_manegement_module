from odoo import models, fields


class DeTai(models.Model):
    _name = 'research_project.detai'
    _description = 'Đề Tài'

    name = fields.Char(string='Tên Đề Tài', required=True)
    maso_detai = fields.Char(string='Mã Số Đề Tài', required=True)
    chuong_trinh = fields.Char(string='Chương Trình')
    maso_chuong_trinh = fields.Char(string='Mã Số Chương Trình')

    LINH_VUC_UU_TIEN_SELECTION = [
        ('khoa_hoc_co_ban', 'Khoa học cơ bản'),
        ('cong_nghe_cao_nong_nghiep', 'Công nghệ cao trong nông nghiệp, thủy sản và phát triển bền vững'),
        ('moi_truong', 'Môi trường, tài nguyên thiên nhiên và biến đổi khí hậu'),
        ('cong_nghe_thong_tin', 'Công nghệ, công nghệ thông tin và chuyển đổi số'),
        ('khoa_hoc_giao_duc', 'Khoa học giáo dục, luật và xã hội nhân văn'),
        ('phat_trien_kinh_te', 'Phát triển kinh tế, thị trường và nông thôn'),
        ('cong_nghe_sinh_hoc', 'Công nghệ sinh học và thực phẩm'),
        ('khong_thuoc_uu_tien', 'Không thuộc 7 Lĩnh vực ưu tiên'),
    ]
    linh_vuc_uu_tien = fields.Selection(LINH_VUC_UU_TIEN_SELECTION, string='Lĩnh Vực Ưu Tiên')

    LINH_VUC_NGHIEN_CUU_SELECTION = [
        ('khoa_hoc_tu_nhien', 'Khoa học Tự nhiên'),
        ('khoa_hoc_ky_thuat', 'Khoa học Kỹ thuật và Công nghệ'),
        ('khoa_hoc_y_duoc', 'Khoa học Y, dược'),
        ('khoa_hoc_nong_nghiep', 'Khoa học Nông nghiệp'),
        ('khoa_hoc_xa_hoi', 'Khoa học Xã hội'),
        ('khoa_hoc_nhan_van', 'Khoa học Nhân văn'),
    ]
    linh_vuc_nghien_cuu = fields.Selection(LINH_VUC_NGHIEN_CUU_SELECTION, string='Lĩnh Vực Nghiên Cứu')

    LOAI_HINH_NGHIEN_CUU_SELECTION = [
        ('co_ban', 'Cơ bản'),
        ('ung_dung', 'Ứng dụng'),
        ('trien_khai', 'Triển khai'),
    ]
    loai_hinh_nghien_cuu = fields.Selection(LOAI_HINH_NGHIEN_CUU_SELECTION, string='Loại Hình Nghiên Cứu')

    thoi_gian_bat_dau = fields.Date(string='Thời Gian Bắt Đầu')
    thoi_gian_ket_thuc = fields.Date(string='Thời Gian Kết Thúc')
    don_vi_chu_nhiem = fields.Char(string='Đơn Vị Chủ Nhiệm')
    dien_thoai_don_vi = fields.Char(string='Điện Thoại Đơn Vị')
    email_don_vi = fields.Char(string='Email Đơn Vị')
    dia_chi_don_vi = fields.Char(string='Địa Chỉ Đơn Vị')
    thu_truong_don_vi = fields.Char(string='Thủ Trưởng Đơn Vị')
    tinh_cap_thiet = fields.Text(string='Tính Cấp Thiết')
    muc_tieu_detai = fields.Text(string='Mục Tiêu Đề Tài')
    doi_tuong_nghien_cuu = fields.Text(string='Đối Tượng Nghiên Cứu')
    pham_vi_nghien_cuu = fields.Text(string='Phạm Vi Nghiên Cứu')
    cach_tiep_can = fields.Text(string='Cách Tiếp Cận')
    phuong_phap_nghien_cuu = fields.Text(string='Phương Pháp Nghiên Cứu')
    san_pham = fields.Text(string='Sản Phẩm')
    phuong_thuc_chuyen_giao = fields.Text(string='Phương Thức Chuyển Giao')
    dia_chi_ung_dung = fields.Text(string='Địa Chỉ Ứng Dụng')
    tac_dong = fields.Text(string='Tác Động và Lợi Ích')
    kinh_phi_thuc_hien = fields.Float(string='Kinh Phí Thực Hiện')
    nguon_kinh_phi = fields.Text(string='Nguồn Kinh Phí')

    chu_nhiem_detai_id = fields.Many2one('research_project.chunhiemdetai', string='Chủ Nhiệm Đề Tài')
    thanh_vien_ids = fields.One2many('research_project.thanhvien', 'detai_id', string='Thành Viên')
    don_vi_phoi_hop_ids = fields.One2many('research_project.donviphoihop', 'detai_id', string='Đơn Vị Phối Hợp')
    tong_quan_nghien_cuu_id = fields.Many2one('research_project.tongquannghiencuu', string='Tổng Quan Nghiên Cứu')
    tien_do_thuc_hien_ids = fields.One2many('research_project.tiendothuchien', 'detai_id', string='Tiến Độ Thực Hiện')
    kinh_phi_thuc_hien_id = fields.Many2one('research_project.kinhphithuchien', string='Kinh Phí Thực Hiện')
    hop_dong_trien_khai_id = fields.Many2one('research_project.hopdongtrienkhai', string='Hợp Đồng Triển Khai')
    du_toan_kinh_phi_id = fields.Many2one('research_project.dutoankinhphi', string='Dự Toán Kinh Phí')
