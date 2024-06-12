from odoo import models, fields

class HopDongTrienKhai(models.Model):
    _name = 'research_project.hopdongtrienkhai'
    _description = 'Hợp Đồng Triển Khai'

    so_hop_dong = fields.Char(string='Số Hợp Đồng')
    ten_de_tai = fields.Char(string='Tên Đề Tài')
    dai_dien_ben_a = fields.Char(string='Đại Diện Bên A')
    dai_dien_ben_b = fields.Char(string='Đại Diện Bên B')
    thoi_gian_thuc_hien = fields.Date(string='Thời Gian Thực Hiện')
    gia_tri_hop_dong = fields.Float(string='Giá Trị Hợp Đồng')
    detai_id = fields.Many2one('research_project.detai', string='Đề Tài')
