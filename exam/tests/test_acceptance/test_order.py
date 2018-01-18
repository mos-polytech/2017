# -*- coding: utf-8 -*-

import pytest


@pytest.mark.acceptance
def test_create_new_order(client):
    """
    This test should create a new order.

    This test should assert that order is saved with the required fields.
    Also, this test should assert the response code.
    Which should equal to `201`.
    """
    raise NotImplemented('Acceptance test failed')


@pytest.mark.acceptance
def test_create_new_order_unauthorized(client):
    """
    This test should try to create a new order without authentication.

    This test should assert that order is not saved.
    Also, this test should assert the response code.
    Which should equal to `401`.
    """
    raise NotImplemented('Acceptance test failed')
