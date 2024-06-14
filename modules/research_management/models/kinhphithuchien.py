from odoo import models, fields, api

class KinhPhiThucHien(models.Model):
    _name = 'research_project.kinhphithuchien'
    _description = 'Kinh Phí Thực Hiện'

    khoan_chi = fields.Float(string='Khoản Chi')  # Đổi sang kiểu float để dễ tính toán
    nguon_kinh_phi_truong_cap = fields.Float(string='Nguồn Kinh Phí Trường Cấp')
    nguon_kinh_phi_khac = fields.Float(string='Nguồn Kinh Phí Khác')
    tong_kinh_phi = fields.Float(string='Tổng Kinh Phí', compute='_compute_tong_kinh_phi', store=True)
    detai_id = fields.Many2one('research_project.detai', string='Đề Tài')

    @api.depends('khoan_chi', 'nguon_kinh_phi_truong_cap', 'nguon_kinh_phi_khac')
    def _compute_tong_kinh_phi(self):
        for record in self:
            record.tong_kinh_phi = (record.khoan_chi or 0.0) + (record.nguon_kinh_phi_truong_cap or 0.0) + (record.nguon_kinh_phi_khac or 0.0)

    @api.model
    def create(self, vals):
        # Calculate total cost before creating the record
        vals['tong_kinh_phi'] = (vals.get('khoan_chi', 0.0) or 0.0) + (vals.get('nguon_kinh_phi_truong_cap', 0.0) or 0.0) + (vals.get('nguon_kinh_phi_khac', 0.0) or 0.0)
        return super(KinhPhiThucHien, self).create(vals)

    def write(self, vals):
        # Calculate total cost before writing the record
        for record in self:
            if 'khoan_chi' in vals:
                khoan_chi = vals['khoan_chi']
            else:
                khoan_chi = record.khoan_chi

            if 'nguon_kinh_phi_truong_cap' in vals:
                nguon_kinh_phi_truong_cap = vals['nguon_kinh_phi_truong_cap']
            else:
                nguon_kinh_phi_truong_cap = record.nguon_kinh_phi_truong_cap

            if 'nguon_kinh_phi_khac' in vals:
                nguon_kinh_phi_khac = vals['nguon_kinh_phi_khac']
            else:
                nguon_kinh_phi_khac = record.nguon_kinh_phi_khac

            vals['tong_kinh_phi'] = (khoan_chi or 0.0) + (nguon_kinh_phi_truong_cap or 0.0) + (nguon_kinh_phi_khac or 0.0)
        return super(KinhPhiThucHien, self).write(vals)
