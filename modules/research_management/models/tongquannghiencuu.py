from odoo import models, fields

class TongQuanNghienCuu(models.Model):
    _name = 'research_project.tongquannghiencuu'
    _description = 'Tổng Quan Tình Hình Nghiên Cứu'

    trong_nuoc = fields.Text(string='Tổng Quan Nghiên Cứu Trong Nước')
    ngoai_nuoc = fields.Text(string='Tổng Quan Nghiên Cứu Ngoài Nước')
    cong_trinh_cong_bo_chu_nhiem = fields.Text(string='Công Trình Công Bố của Chủ Nhiệm Đề Tài')
    cong_trinh_cong_bo_thanh_vien = fields.Text(string='Công Trình Công Bố của Các Thành Viên')
    detai_id = fields.Many2one('research_project.detai', string='Đề Tài')
