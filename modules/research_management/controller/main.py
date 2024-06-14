# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class ResearchProject(http.Controller):

    @http.route('/detai_view', type='http', auth='public', website=True)
    def view_detai_web(self, **kw):
        detais = request.env['research_project.detai'].sudo().search([])
        return http.request.render('research_management.view_detai', {
            'detais': detais
        })

    @http.route('/kinh-phi', type='http', auth='public', website=True)
    def view_kinhphi(self, **kwargs):
        # Truy vấn danh sách các đề tài và kinh phí
        kinhphi_records = request.env['research_project.kinhphithuchien'].sudo().search([])

        # Truyền dữ liệu vào template để render
        values = {
            'kinhphi_records': kinhphi_records
        }
        return request.render('research_management.kinhphi_template', values)

    @http.route('/tiendothuchien', type='http', auth='public', website=True)
    def tiendothuchien(self, **kwargs):
        # Truy vấn danh sách tiến độ thực hiện
        tiendo_records = request.env['research_project.tiendothuchien'].sudo().search([])

        # Truyền dữ liệu vào template để render
        values = {
            'tiendo_records': tiendo_records
        }
        return request.render('research_management.tiendothuchien_template', values)