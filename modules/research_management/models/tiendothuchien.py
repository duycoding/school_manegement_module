from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TienDoThucHien(models.Model):
    _name = 'research_project.tiendothuchien'
    _description = 'Tiến Độ Thực Hiện'

    noi_dung_cong_viec = fields.Text(string='Nội Dung Công Việc', required=True)
    san_pham = fields.Text(string='Sản Phẩm', required=True)
    thoi_gian_bat_dau = fields.Date(string='Thời Gian Bắt Đầu', required=True)
    thoi_gian_ket_thuc = fields.Date(string='Thời Gian Kết Thúc', required=True)
    nguoi_thuc_hien = fields.Char(string='Người Thực Hiện', required=True)
    detai_id = fields.Many2one('research_project.detai', string='Đề Tài', required=True)

    @api.constrains('thoi_gian_bat_dau', 'thoi_gian_ket_thuc')
    def _check_dates(self):
        for record in self:
            if record.thoi_gian_bat_dau and record.thoi_gian_ket_thuc and record.thoi_gian_bat_dau > record.thoi_gian_ket_thuc:
                raise ValidationError("Thời gian bắt đầu không được lớn hơn thời gian kết thúc.")

