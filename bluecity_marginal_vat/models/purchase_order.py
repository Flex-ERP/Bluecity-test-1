# -*- coding: utf-8 -*-

from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    marginal_vat = fields.Boolean(string="Marginal VAT", copy=False)
    fiscal_tax_ids = fields.Many2many("account.tax", string="Fiscal Taxes", copy=False)

    @api.onchange("marginal_vat")
    def update_fiscal_position(self):
        for rec in self:
            if rec.marginal_vat:
                rec.fiscal_position_id = self.env.ref("bluecity_marginal_vat.margin_vat_fiscal").id
                rec.fiscal_tax_ids = [(5, 0, 0)]
            else:
                rec.fiscal_position_id = False
                rec.fiscal_tax_ids = [(5, 0, 0)]

    @api.onchange("fiscal_position_id")
    def onchange_fiscal_position(self):
        for record in self:
            fiscal_tax = []
            if record.fiscal_position_id and record.marginal_vat:
                if record.fiscal_position_id.tax_ids:
                    for taxes in record.fiscal_position_id.tax_ids:
                        fiscal_tax.append(taxes.tax_src_id.id)
                    record.fiscal_tax_ids = fiscal_tax
            else:
                taxes_ids = self.env["account.tax"].search([
                    ("type_tax_use", "=", "purchase"), 
                    ("company_id", "=", record.company_id.id)
                ])
                for tax in taxes_ids:
                    fiscal_tax.append(tax.id)
                record.fiscal_tax_ids = fiscal_tax


#class PurchaseOrderLine(models.Model):
#    _inherit = "purchase.order.line"

#    def _compute_tax_id(self):
#        for line in self:
#            if line.order_id.second_hand_tax:
#                line.taxes_id = [(5,)]
#            else:
#                super()._compute_tax_id()