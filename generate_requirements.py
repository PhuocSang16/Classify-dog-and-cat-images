import pkg_resources

def generate_requirements(filename="requirements.txt"):
    # Lấy danh sách tất cả các gói và phiên bản
    installed_packages = pkg_resources.working_set
    packages = sorted(["{}=={}".format(pkg.key, pkg.version) for pkg in installed_packages])

    # Ghi vào tệp requirements.txt
    with open(filename, "w") as f:
        f.write("\n".join(packages))
    
    print(f"File '{filename}' đã được tạo thành công!")

# Gọi hàm để tạo requirements.txt
generate_requirements()
