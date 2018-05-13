def test_mink_can_be_imported():
    import mink
    assert mink is not None


def test_mink_defines_version():
    import mink
    assert hasattr(mink, "__version__")
    assert isinstance(mink.__version__, str)
    assert len(mink.__version__) > 1
