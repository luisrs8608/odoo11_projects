# -*- coding: utf-8 -*-

from odoo import api, models


class RatingAutomaticTask(models.Model):
    _inherit = 'project.task'

    @api.multi
    def write(self, vals):
        if 'stage_id' in vals:
            project_task_type = self.env['project.task.type'].browse(vals['stage_id'])
            if project_task_type.fold and not self.env['rating.rating'].search(
                    [('res_model', '=', self._name), ('res_id', '=', self.id), ('consumed', '=', True)]):
                record_model_id = self.env['ir.model'].sudo().search([('model', '=', self._name)], limit=1).id
                self.env['rating.rating'].create({
                    'rating': 10,
                    'res_model_id': record_model_id,
                    'res_id': self.id,
                    'consumed': True,
                    'partner_id': self.partner_id and self.partner_id.id or False,
                    'rated_partner_id': self.user_id and self.user_id.partner_id and self.user_id.partner_id.id or False
                })
        return super(RatingAutomaticTask, self).write(vals)
