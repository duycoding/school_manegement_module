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

    @http.route('/dangkydetai', type='http', auth='public', website=True)
    def dangky_detai(self, **kwargs):
        return request.render('research_management.dangkydetai_template', {})

    @http.route('/dangkydetai/submit', type='http', auth='public', website=True, methods=['POST'])
    def dangky_detai_submit(self, **kwargs):
        request.env['research_project.detai'].sudo().create({
            'name': kwargs.get('name'),
            'maso_detai': kwargs.get('maso_detai'),
            'chuong_trinh': kwargs.get('chuong_trinh'),
            'maso_chuong_trinh': kwargs.get('maso_chuong_trinh'),
            'linh_vuc_uu_tien': kwargs.get('linh_vuc_uu_tien'),
            'linh_vuc_nghien_cuu': kwargs.get('linh_vuc_nghien_cuu'),
            'loai_hinh_nghien_cuu': kwargs.get('loai_hinh_nghien_cuu'),
            'thoi_gian_bat_dau': kwargs.get('thoi_gian_bat_dau'),
            'thoi_gian_ket_thuc': kwargs.get('thoi_gian_ket_thuc'),
            'don_vi_chu_nhiem': kwargs.get('don_vi_chu_nhiem'),
            'dien_thoai_don_vi': kwargs.get('dien_thoai_don_vi'),
            'email_don_vi': kwargs.get('email_don_vi'),
            'dia_chi_don_vi': kwargs.get('dia_chi_don_vi'),
            'thu_truong_don_vi': kwargs.get('thu_truong_don_vi'),
            'tinh_cap_thiet': kwargs.get('tinh_cap_thiet'),
            'muc_tieu_detai': kwargs.get('muc_tieu_detai'),
            'doi_tuong_nghien_cuu': kwargs.get('doi_tuong_nghien_cuu'),
            'pham_vi_nghien_cuu': kwargs.get('pham_vi_nghien_cuu'),
            'cach_tiep_can': kwargs.get('cach_tiep_can'),
            'phuong_phap_nghien_cuu': kwargs.get('phuong_phap_nghien_cuu'),
            'san_pham': kwargs.get('san_pham'),
            'phuong_thuc_chuyen_giao': kwargs.get('phuong_thuc_chuyen_giao'),
            'dia_chi_ung_dung': kwargs.get('dia_chi_ung_dung'),
            'tac_dong': kwargs.get('tac_dong'),
            'kinh_phi_thuc_hien': kwargs.get('kinh_phi_thuc_hien'),
            'nguon_kinh_phi': kwargs.get('nguon_kinh_phi'),
            # Add other fields as needed
        })
        return request.redirect('/dangkydetai')
