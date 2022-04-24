# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models


class ReportPosHashIntegrity(models.AbstractModel):
    _name = 'report.l10n_fr_pos_cert_v14.report_pos_hash_integrity'
    _description = 'Get french pos hash integrity result as PDF.'

    @api.model
    def _get_report_values(self, docids, data=None):
        # <GRAP Patch Backport>
        # replace various env.company by env.user.company_id
        if data:
            data.update(self.env.user.company_id._check_pos_hash_integrity())
        else:
            data = self.env.user.company_id._check_hash_pos_integrity()
        return {
            'doc_ids' : docids,
            'doc_model' : self.env['res.company'],
            'data' : data,
            'docs' : self.env['res.company'].browse(self.env.user.company_id.id),
        }
        # </GRAP Patch Backport>
