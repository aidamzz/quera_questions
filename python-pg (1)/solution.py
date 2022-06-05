def sort_dependencies(packages, package_name):
    package_dependencies = []
    if packages[package_name] != []:
        package_dependencies = package_dependencies + packages[package_name]
        for i in package_dependencies:
            
            package_dependencies += sort_dependencies(packages,i)
    package_dependencies1 = package_dependencies
    package_dependencies = []
    for i in package_dependencies1[::-1]:
        if i not in package_dependencies:
            package_dependencies.append(i)
            
    return package_dependencies
