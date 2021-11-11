# -*- coding: utf-8 -*-
from odoo import api, fields, models
import logging
_logger = logging.getLogger(__name__)


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.depends("product_uom_qty", "discount", "price_unit", "tax_id")
    def _compute_amount(self):
        super(SaleOrderLine, self)._compute_amount()
        #for record in self:
        #    if record.lot_id:
        #        record.price_tax = (record.price_unit - record.lot_id.cost_price) * 0.2
                #record.price_total = 98
                #record.price_subtotal = 98
