# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ResearchProject(http.Controller):

    @http.route('/detai_webform', type='http', auth='user', website=True)
    def detai_webform(self, **kw):
        return http.request.render('research_project.create_detai', {})

    @http.route('/create/webdetai', type="http", auth="user", website=True)
    def create_webdetai(self, **kw):
        request.env['research_project.detai'].sudo().create(kw)
        return request.render("research_project.detai_thanks", {})

    @http.route('/detai_view', type='http', auth='public', website=True)
    def view_detai_web(self, **kw):
        detais = request.env['research_project.detai'].sudo().search([])
        return http.request.render('research_management.view_detai', {
            'detais': detais
        })
