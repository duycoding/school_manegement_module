from odoo import models, fields

class ChuNhiemDeTai(models.Model):
    _name = 'research_project.chunhiemdetai'
    _description = 'Chủ Nhiệm Đề Tài'

    name = fields.Char(string='Họ và Tên', required=True)
    mscb = fields.Char(string='Mã Số Cán Bộ')
    chuc_danh_khoa_hoc = fields.Char(string='Chức Danh Khoa Học')
    hoc_vi = fields.Char(string='Học Vị')
    nam_sinh = fields.Integer(string='Năm Sinh')
    dien_thoai_di_dong = fields.Char(string='Điện Thoại Di Động')
    email = fields.Char(string='Email')
    dia_chi_co_quan = fields.Char(string='Địa Chỉ Cơ Quan')
    dien_thoai_co_quan = fields.Char(string='Điện Thoại Cơ Quan')

    detai_ids = fields.One2many('research_project.detai', 'chu_nhiem_detai_id', string='Đề Tài')
