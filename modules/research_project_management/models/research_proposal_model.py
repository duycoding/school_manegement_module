from odoo import models, fields, api


class ResearchProject(models.Model):
    _name = 'research.project'
    _description = 'Research Project'

    name = fields.Char(string='Tên đề tài', required=True)
    code = fields.Char(string='Mã số đề tài')
    program = fields.Char(string='Chương trình Khoa học và Công nghệ')
    program_code = fields.Char(string='Mã số Chương trình')
    priority_field = fields.Selection([
        ('science', 'Khoa học cơ bản'),
        ('technology', 'Công nghệ cao trong nông nghiệp, thủy sản và phát triển bền vững'),
        ('environment', 'Môi trường, tài nguyên thiên nhiên và biến đổi khí hậu'),
        ('it', 'Công nghệ, công nghệ thông tin và chuyển đổi số'),
        ('education', 'Khoa học giáo dục, luật và xã hội nhân văn'),
        ('economy', 'Phát triển kinh tế, thị trường và nông thôn'),
        ('biotech', 'Công nghệ sinh học và thực phẩm'),
        ('none', 'Không thuộc 7 Lĩnh vực ưu tiên')
    ], string='Lĩnh vực ưu tiên')
    research_field = fields.Selection([
        ('natural', 'Khoa học Tự nhiên'),
        ('engineering', 'Khoa học Kỹ thuật và Công nghệ'),
        ('medicine', 'Khoa học Y, dược'),
        ('agriculture', 'Khoa học Nông nghiệp'),
        ('social', 'Khoa học Xã hội'),
        ('humanities', 'Khoa học Nhân văn')
    ], string='Lĩnh vực nghiên cứu')
    research_type = fields.Selection([
        ('basic', 'Cơ bản'),
        ('application', 'Ứng dụng'),
        ('deployment', 'Triển khai')
    ], string='Loại hình nghiên cứu')
    start_date = fields.Date(string='Ngày bắt đầu')
    end_date = fields.Date(string='Ngày kết thúc')
    duration = fields.Integer(string='Thời gian thực hiện (tháng)', compute='_compute_duration', store=True)
    organization_name = fields.Char(string='Tên đơn vị')
    organization_phone = fields.Char(string='Điện thoại đơn vị')
    organization_email = fields.Char(string='E-mail đơn vị')
    organization_address = fields.Char(string='Địa chỉ đơn vị')
    organization_head = fields.Char(string='Họ và tên thủ trưởng đơn vị')
    project_leader = fields.Char(string='Họ và tên Chủ nhiệm đề tài')
    project_leader_id = fields.Char(string='MSCB')
    project_leader_title = fields.Char(string='Chức danh khoa học')
    project_leader_office_address = fields.Char(string='Địa chỉ cơ quan')
    project_leader_office_phone = fields.Char(string='Điện thoại cơ quan')
    project_leader_degree = fields.Char(string='Học vị')
    project_leader_birth_year = fields.Integer(string='Năm sinh')
    project_leader_mobile = fields.Char(string='Điện thoại di động')
    project_leader_email = fields.Char(string='E-mail chủ nhiệm đề tài')
    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for record in self:
            if record.start_date and record.end_date:
                delta = fields.Date.from_string(record.end_date) - fields.Date.from_string(record.start_date)
                record.duration = delta.days // 30  # tính số tháng
            else:
                record.duration = 0

    @api.model
    def action_edit(self, vals):
        for record in self:
            return {
                'type': 'ir.actions.act_window',
                'name': 'Edit Research Project',
                'res_model': 'research.project',
                'view_mode': 'form',
                'res_id': record.id,
                'target': 'current',
            }

    @api.model
    def action_delete(self):
        for record in self:
            # Xóa bản ghi hiện tại
            record.unlink()
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
