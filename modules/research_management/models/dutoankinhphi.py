from odoo import models, fields

class DuToanKinhPhi(models.Model):
    _name = 'research_project.dutoankinhphi'
    _description = 'Dự Toán Kinh Phí'

    maso_detai = fields.Char(string='Mã Số Đề Tài')
    ten_de_tai = fields.Char(string='Tên Đề Tài')
    chu_nhiem_detai_id = fields.Many2one('research_project.chunhiemdetai', string='Chủ Nhiệm Đề Tài')
    tong_kinh_phi = fields.Float(string='Tổng Kinh Phí')
    chi_tiet_khoan_chi = fields.Text(string='Chi Tiết Khoản Chi')
    detai_id = fields.Many2one('research_project.detai', string='Đề Tài')
