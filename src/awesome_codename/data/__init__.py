from pkg_resources import resource_string


def load(name, package='awesome_codename'):
    """Load words from text file by given name."""
    content = resource_string(package, 'data/%s.txt' % name)
    return content.decode().splitlines()
