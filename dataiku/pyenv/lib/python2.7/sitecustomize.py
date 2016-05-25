import site, pkg_resources
site.addsitedir('/data1/tools/dataiku-dss-2.0.1/python.packages')
pkg_resources.fixup_namespace_packages('/data1/tools/dataiku-dss-2.0.1/python.packages')
