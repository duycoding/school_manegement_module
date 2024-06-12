from odoo import models, fields

class TienDoThucHien(models.Model):
    _name = 'research_project.tiendothuchien'
    _description = 'Tiến Độ Thực Hiện'

    noi_dung_cong_viec = fields.Text(string='Nội Dung Công Việc')
    san_pham = fields.Text(string='Sản Phẩm')
    thoi_gian_bat_dau = fields.Date(string='Thời Gian Bắt Đầu')
    thoi_gian_ket_thuc = fields.Date(string='Thời Gian Kết Thúc')
    nguoi_thuc_hien = fields.Char(string='Người Thực Hiện')
    detai_id = fields.Many2one('research_project.detai', string='Đề Tài')
