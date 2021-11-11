# -*- coding: utf-8 -*-
from odoo import api, fields, models


class AccountFiscalPosition(models.Model):
    _inherit = "account.fiscal.position"

    marginal_vat = fields.Boolean(string="Marginal VAT", copy=False)
