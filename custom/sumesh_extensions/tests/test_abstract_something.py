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
from odoo.tests.common import SingleTransactionCase


class AbstractSomethingTester(models.Model):
    """ It provides a real model object to test the abstract with """
    _name = 'abstract.something.tester'
    _description = 'Abstract Something Tester'
    _inherit = 'abstract.something'


class TestAbstractSomething(SingleTransactionCase):
    @classmethod
    def _init_test_model(cls, model_cls):
        """ It builds a model from model_cls in order to test abstract models

        Args:
            model_cls: (openerp.models.BaseModel) Class of model to initialize
        Returns:
            Model instance
        """
        model_cls._build_model(cls.registry, cls.cr)
        model = cls.env[model_cls._name].with_context(todo=[])
        model._prepare_setup()
        model._setup_base(partial=False)
        model._setup_fields(partial=False)
        model._setup_complete()
        model._auto_init()
        model.init()
        model._auto_end()
        return model

    @classmethod
    def setUpClass(cls):
        super(TestAbstractSomething, cls).setUpClass()
        cls.registry.enter_test_mode()
        cls.old_cursor = cls.cr
        cls.cr = cls.registry.cursor()
        cls.env = api.Environment(cls.cr, cls.uid, {})
        cls.test_model = cls._init_test_model(AbstractSomethingTester)

    @classmethod
    def tearDownClass(cls):
        cls.registry.leave_test_mode()
        cls.registry[cls.test_model._name]._abstract = True
        cls.registry[cls.test_model._name]._auto = False
        cls.cr = cls.old_cursor
        cls.env = api.Environment(cls.cr, cls.uid, {})
        super(TestAbstractSomething, cls).tearDownClass()
