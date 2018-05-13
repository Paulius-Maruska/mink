"""Make sense of schemaless data dictionaries.
"""

try:
    import pkg_resources

    __version__ = pkg_resources.get_distribution("mink").version
except pkg_resources.DistributionNotFound:
    # package is not installed
    __version__ = "unknown"

__all__ = (
    "__version__",
)
