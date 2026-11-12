import platform, shutil, subprocess, sys

print("=== Layer 1: System ===")
print("OS:", platform.system(), platform.release(), platform.machine())

print("\n=== Layers 2 and 3: Package managers and runtimes ===")
print("Python:", sys.version.split()[0])
for tool in ["uv", "node", "pnpm", "rustc", "cargo"]:
    path = shutil.which(tool)
    if path:
        out = subprocess.run([path, "--version"], capture_output=True, text=True)
        print(f"{tool}: {out.stdout.strip()}")
    else:
        print(f"{tool}: NOT FOUND")

print("\n=== Layer 4: AI libraries ===")
import numpy as np
import torch
print("NumPy:", np.__version__)
print("PyTorch:", torch.__version__)

if torch.cuda.is_available():
    device = "cuda"
elif torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"
print("Device:", device)

a = torch.rand(3, 3, device=device)
b = torch.rand(3, 3, device=device)
print("\nTest tensor operation (a @ b, matrix multiplication):")
print(a @ b)
print("\nAll four layers working!")