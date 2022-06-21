# -*- coding: utf-8 -*-
# from odoo import http


# class FaceDatas(http.Controller):
#     @http.route('/face_datas/face_datas/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/face_datas/face_datas/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('face_datas.listing', {
#             'root': '/face_datas/face_datas',
#             'objects': http.request.env['face_datas.face_datas'].search([]),
#         })

#     @http.route('/face_datas/face_datas/objects/<model("face_datas.face_datas"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('face_datas.object', {
#             'object': obj
#         })
