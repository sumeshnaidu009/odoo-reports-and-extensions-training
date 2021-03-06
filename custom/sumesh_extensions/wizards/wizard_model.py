# -*- coding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2019 Openfellas (http://openfellas.com) All Rights Reserved.
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsibility of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# guarantees and support are strongly advised to contract support@openfellas.com
#
##############################################################################

from odoo import api, models


class WizardModel(models.TransientModel):
    _name = 'module.wizard_model'

    @api.multi
    def action_accept(self):
        self.ensure_one()
        self.do_something_useful()
