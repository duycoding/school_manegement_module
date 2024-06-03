from odoo import models, fields

class Student(models.Model):
    _name = 'student.student'
    _description = 'Student'

    name = fields.Char(string='Full Name', required=True)
    age = fields.Integer(string='Age', required=True)
    address = fields.Char(string='Address')
    phone_number = fields.Char(string='Phone Number')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other')
    ], string='Gender')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
