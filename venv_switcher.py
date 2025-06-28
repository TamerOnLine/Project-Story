import os
import platform
import subprocess

# Define your virtual environments
venvs = {
    "1": ("venv", "Main Environment"),
    "2": ("venv_dev", "Development Environment"),
    "3": ("venv_docs", "Documentation Environment")
}

print("🧠 Select the virtual environment you want to activate:\n")

for key, (env, desc) in venvs.items():
    print(f"{key}️⃣  {env:<12} ({desc})")

choice = input("\n🔢 Enter your choice: ").strip()

if choice not in venvs:
    print("❌ Invalid choice.")
    exit(1)

env_name, env_desc = venvs[choice]

# Determine OS-specific paths
is_windows = platform.system() == "Windows"
activate_script = "activate.bat" if is_windows else "activate"
activate_path = os.path.join(env_name, "Scripts" if is_windows else "bin", activate_script)

if not os.path.exists(activate_path):
    print(f"❌ Cannot find activate script at: {activate_path}")
    exit(1)

print(f"\n✅ To activate '{env_name}' ({env_desc}), run this in your terminal:\n")
if is_windows:
    print(f".\\{env_name}\\Scripts\\activate")
else:
    print(f"source {env_name}/bin/activate")
