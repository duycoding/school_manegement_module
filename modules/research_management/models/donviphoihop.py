from odoo import models, fields

class DonViPhoiHop(models.Model):
    _name = 'research_project.donviphoihop'
    _description = 'Đơn Vị Phối Hợp'

    ten_don_vi = fields.Char(string='Tên Đơn Vị', required=True)
    dia_chi_lien_he = fields.Char(string='Địa Chỉ Liên Hệ')
    noi_dung_phoi_hop = fields.Text(string='Nội Dung Phối Hợp')
    dai_dien = fields.Char(string='Người Đại Diện')
    detai_id = fields.Many2one('research_project.detai', string='Đề Tài')
