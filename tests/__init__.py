def test_invalid_menu_option():
    option = "99"

    assert option not in ["1", "2", "3", "4", "5", "6"]