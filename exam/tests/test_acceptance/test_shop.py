# -*- coding: utf-8 -*-

import pytest


@pytest.mark.acceptance
def test_show_categories(client):
    """
    This test should get the all the categories.

    This test should assert that response has correct values.
    Also, this test should assert the response code.
    Which should equal to `200`.
    """
    raise NotImplemented('Acceptance test failed')


@pytest.mark.acceptance
def test_show_products_by_category(client):
    """
    This test should get the all the products in a single category.

    This test should assert that response has correct values.
    Also, this test should assert the response code.
    Which should equal to `200`.
    """
    raise NotImplemented('Acceptance test failed')


@pytest.mark.acceptance
def test_search_by_name(client):
    """
    This test should search products by name.

    This test should assert that response has correct values.
    Also, this test should assert the response code.
    Which should equal to `200`.
    """
    raise NotImplemented('Acceptance test failed')


@pytest.mark.acceptance
def test_search_by_name_category_price(client):
    """
    This test should search products by name, category, and price.

    This test should assert that response has correct values.
    Also, this test should assert the response code.
    Which should equal to `200`.
    """
    raise NotImplemented('Acceptance test failed')
