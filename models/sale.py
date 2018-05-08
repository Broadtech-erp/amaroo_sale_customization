# -*- coding: utf-8 -*-


from odoo import api, fields, models, _
from odoo.tools import float_compare


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'


    @api.onchange('product_uom_qty', 'product_uom', 'route_id')
    def _onchange_product_id_check_availability(self):
        if not self.product_id or not self.product_uom_qty or not self.product_uom:
            self.product_packaging = False
            return {}
        if self.product_id.type == 'product':
            precision = self.env['decimal.precision'].precision_get('Product Unit of Measure')
            product = self.product_id.with_context(warehouse=self.order_id.warehouse_id.id)
            product_qty = self.product_uom._compute_quantity(self.product_uom_qty, self.product_id.uom_id)
            if float_compare(product.qty_available_not_res, product_qty, precision_digits=precision) == -1:
                is_available = self._check_routing()
                if not is_available:
                    message =  _('You plan to sell %s %s but you only have %s %s available in %s warehouse of which %s %s are available to sell.'\
                            '\nThe forecast level is %s %s check POs for expected delivery date.') % \
                            (self.product_uom_qty, self.product_uom.name, product.qty_available, product.uom_id.name, self.order_id.warehouse_id.name,\
                              product.qty_available_not_res, product.uom_id.name, product.virtual_available, product.uom_id.name)
                            
                    warning_mess = {
                        'title': _('Not enough inventory!'),
                        'message' : message
                    }
                    return {'warning': warning_mess}
        return {}
