# -*- coding: utf-8 -*-

from odoo import api, models


class RatingAutomaticHelpdeskTicket(models.Model):
    _inherit = 'helpdesk.ticket'

    @api.multi
    def write(self, vals):
        if 'stage_id' in vals:
            helpdesk_stage_id = self.env['helpdesk.stage'].browse(vals['stage_id'])
            if helpdesk_stage_id.is_close and helpdesk_stage_id.fold and not self.env['rating.rating'].search(
                    [('res_model', '=', self._name), ('res_id', '=', self.id)]):
                record_model_id = self.env['ir.model'].sudo().search([('model', '=', self._name)], limit=1).id
                self.env['rating.rating'].create({
                    'rating': 10,
                    'res_model_id': record_model_id,
                    'res_id': self.id,
                    'consumed': True,
                    'partner_id': self.partner_id and self.partner_id.id or False,
                    'rated_partner_id': self.user_id and self.user_id.partner_id and self.user_id.partner_id.id or False
                })
        return super(RatingAutomaticHelpdeskTicket, self).write(vals)
