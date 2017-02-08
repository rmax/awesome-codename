from awesome_codename import generate_codename


def test_genrate_codename():
    assert generate_codename() != generate_codename()
