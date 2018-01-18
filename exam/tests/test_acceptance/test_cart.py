# -*- coding: utf-8 -*-

import pytest


@pytest.mark.acceptance
def test_show_cart_empty(client):
    """
    This test should fetch empty cart contents.

    This test should assert that cart is indeed empty.
    Also, this test should assert the response code.
    Which should equal to `200`.
    """
    raise NotImplemented('Acceptance test failed')


@pytest.mark.acceptance
def test_show_cart_with_items(client):
    """
    This test should fetch cart contents with some items inside.

    Also, this test should assert the response code.
    Which should equal to `200`.
    """
    raise NotImplemented('Acceptance test failed')


@pytest.mark.acceptance
def test_add_item_to_cart(client):
    """
    This test should add one item to a cart.

    This test should assert that cart now has this item inside.
    Also, this test should assert the response code.
    Which should equal to `201`.
    """
    raise NotImplemented('Acceptance test failed')


@pytest.mark.acceptance
def test_login_with_nonempty_cart(client):
    """
    This test should cover a situation when user had a cart before login.

    But after user put something inside this cart,
    he went through the login process.
    This test should assert that cart still has all the items inside.
    Also, this test should assert the response code.
    Which should equal to `200`.
    """
    raise NotImplemented('Acceptance test failed')
