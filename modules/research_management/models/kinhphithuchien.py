from odoo import models, fields


class KinhPhiThucHien(models.Model):
    _name = 'research_project.kinhphithuchien'
    _description = 'Kinh Phí Thực Hiện'

    khoan_chi = fields.Text(string='Khoản Chi')
    tong_kinh_phi = fields.Float(string='Tổng Kinh Phí')
    nguon_kinh_phi_truong_cap = fields.Float(string='Nguồn Kinh Phí Trường Cấp')
    nguon_kinh_phi_khac = fields.Float(string='Nguồn Kinh Phí Khác')
    detai_id = fields.Many2one('research_project.detai', string='Đề Tài')
