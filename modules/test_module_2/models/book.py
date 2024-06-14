# library_management/models/book.py
from odoo import models, fields

class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    published_date = fields.Date(string='Published Date')
    isbn = fields.Char(string='ISBN')
