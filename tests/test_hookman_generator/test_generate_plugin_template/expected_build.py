import os
import sys
import shutil
import subprocess
from pathlib import Path

current_dir = Path(os.getcwd())

artifacts_dir = current_dir / "artifacts"
assets = current_dir / "assets"
build_dir = current_dir / "build"
package_dir = current_dir / "package"

if sys.platform == 'win32':
    shared_lib = artifacts_dir / "acme.dll"
else:
    shared_lib = artifacts_dir / "libacme.so"

if build_dir.exists():
    shutil.rmtree(build_dir)

build_dir.mkdir()

binary_directory_path = f"-B{str(build_dir)}"
home_directory_path = f"-H{current_dir}"

if artifacts_dir.exists():
    shutil.rmtree(artifacts_dir)

subprocess.run(["cmake", binary_directory_path, home_directory_path])
subprocess.run(["cmake", "--build", str(build_dir), "--config", "Release", "--target", "install"])

if package_dir.exists():
    shutil.rmtree(package_dir)

shutil.copytree(src=assets, dst=package_dir)
shutil.copy2(src=shared_lib, dst=package_dir)