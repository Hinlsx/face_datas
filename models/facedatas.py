# -*- coding: utf-8 -*-

from odoo import models, fields, api


class FDatas(models.Model):
    _name = "face.datas"
    _description = 'FDatas'

    name = fields.Char('Data', required=True)
    json = fields.Text()

    datasresult_id = fields.Many2one('datas.result', string="DResult_ID")

    def button_send(self):
        # res = self.env['datas.result'].create([{
        #     'name': self.name,
        # }])

        return {
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'datas.result',
            'res_id': self.datasresult_id.id,
        }


class DResult(models.Model):
    _name = "datas.result"
    _description = "DResult"

    name = fields.Char('Result', required=True)

    datasresult_ids = fields.One2many('face.datas', 'datasresult_id')

# class DJson(models.Model):
#     _name = "datas.json"
#     _description = "DJson"
#
#     name = fields.Char('Json', required=True)


#       print_facedatas_id = fields.Many2one('face.datas')

#     @api.multi
#     def button_send_ids(self):
#         return {
#             'name': 'Button Send IDs',
#             'view_type': 'form',
#             'view_mode': 'tree,form',
#             'res_model': 'face.datas',
#             'view_id': False,
#             'type': 'ir.action.act_window',
#             'domain': [('json_id', '=', self.id)],
#         }
