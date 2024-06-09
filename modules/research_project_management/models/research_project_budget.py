from odoo import models, fields, api


class ResearchProjectBudget(models.Model):
    _name = 'research.project.budget'
    _description = 'Dự toán kinh phí dự án nghiên cứu'

    project_id = fields.Many2one('research.project', string='Mã số đề tài')
    name = fields.Char(string='Tên đề tài')
    project_leader = fields.Char(string='Chủ nhiệm đề tài')
    total_budget = fields.Float(string='Tổng kinh phí', compute='_compute_total_budget', store=True)

    # Chi tiết các khoản chi
    expense_ids = fields.One2many('research.project.budget.expense', 'budget_id', string='Chi tiết kinh phí')


class ResearchProjectBudgetExpense(models.Model):
    _name = 'research.project.budget.expense'
    _description = 'Chi tiết kinh phí dự toán'

    budget_id = fields.Many2one('research.project.budget', string='Dự toán kinh phí')
    description = fields.Text(string='Nội dung chi')
    unit = fields.Char(string='Đơn vị tính')
    quantity = fields.Float(string='Số lượng')
    unit_price = fields.Float(string='Đơn giá')
    subtotal = fields.Float(string='Thành tiền')
