from odoo import models, fields

class ThanhVien(models.Model):
    _name = 'research_project.thanhvien'
    _description = 'Thành Viên Tham Gia Nghiên Cứu'

    name = fields.Char(string='Họ và Tên', required=True)
    msvc = fields.Char(string='Mã Số Viên Chức')
    chuc_danh = fields.Char(string='Chức Danh')
    don_vi_cong_tac = fields.Char(string='Đơn Vị Công Tác')
    linh_vuc_chuyen_mon = fields.Char(string='Lĩnh Vực Chuyên Môn')
    nhiem_vu = fields.Text(string='Nhiệm Vụ')
    detai_id = fields.Many2one('research_project.detai', string='Đề Tài')
