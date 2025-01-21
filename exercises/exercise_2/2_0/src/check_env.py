import sys
import pkg_resources

print("Python version:")
print(sys.version)
print("\nInstalled packages:")
installed_packages = pkg_resources.working_set
for package in installed_packages:
    print(f"{package.key} ({package.version})")