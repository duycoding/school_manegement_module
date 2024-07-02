from odoo import models, fields, api
from odoo.exceptions import ValidationError


class DonViPhoiHop(models.Model):
    _name = 'research_project.donviphoihop'
    _description = 'Đơn Vị Phối Hợp'

    ten_don_vi = fields.Char(string='Tên Đơn Vị', required=True)
    dia_chi_lien_he = fields.Char(string='Địa Chỉ Liên Hệ')
    noi_dung_phoi_hop = fields.Text(string='Nội Dung Phối Hợp')
    dai_dien = fields.Char(string='Người Đại Diện')
    detai_id = fields.Many2one('research_project.detai', string='Đề Tài')

    @api.constrains('ten_don_vi', 'dia_chi_lien_he')
    def _check_required_fields(self):
        for record in self:
            if not record.ten_don_vi or not record.dia_chi_lien_he:
                raise ValidationError("Tên Đơn Vị và Địa Chỉ Liên Hệ không thể để trống!")
