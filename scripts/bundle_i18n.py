import os
import json

base_dir = "/mnt/d/proyects/profile/i18n"
config_file = os.path.join(base_dir, "config.json")
with open(config_file, "r", encoding="utf-8") as f:
    config = json.load(f)

bundle = {
    "config": config,
    "languages": {}
}

for lang in config["languages"]:
    code = lang["code"]
    lang_file = os.path.join(base_dir, f"{code}.json")
    if os.path.exists(lang_file):
        with open(lang_file, "r", encoding="utf-8") as f:
            bundle["languages"][code] = json.load(f)

bundle_path = os.path.join(base_dir, "bundle.js")
with open(bundle_path, "w", encoding="utf-8") as f:
    f.write("window.__I18N_BUNDLE__ = " + json.dumps(bundle, ensure_ascii=False) + ";\n")

print(f"Generated i18n/bundle.js successfully with {len(bundle['languages'])} languages.")
