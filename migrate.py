import os
import shutil

src_root = r"c:\Users\LENOVO\Cetha AI"
dst_root = r"c:\Users\LENOVO\cethaa ai"

# Pastikan hapus file kosong yang dibuat tidak sengaja
for f in ["ai", "api", "insight", "models", "recommendation", "services", "main.py"]:
    p = os.path.join(dst_root, "backend", "app", f)
    if os.path.isfile(p):
        os.remove(p)

dirs_to_create = [
    "backend/app/api/endpoints",
    "backend/app/services",
    "backend/app/models",
    "backend/app/ai",
    "backend/app/insights",
    "backend/app/recommendations",
    "backend/app/core",
    "frontend"
]

for d in dirs_to_create:
    os.makedirs(os.path.join(dst_root, d), exist_ok=True)

# Copy and modify main.py
with open(os.path.join(src_root, "app", "main.py"), "r", encoding="utf-8") as f:
    main_content = f.read()

main_content = main_content.replace("app.services.categorization", "app.ai.categorization")
main_content = main_content.replace("app.services.analytics", "app.insights.analytics")
main_content = main_content.replace("app.services.recommendation", "app.recommendations.recommendation")

with open(os.path.join(dst_root, "backend", "app", "main.py"), "w", encoding="utf-8") as f:
    f.write(main_content)

# Copy config.py
shutil.copy(os.path.join(src_root, "app", "core", "config.py"), os.path.join(dst_root, "backend", "app", "core", "config.py"))

# Copy health.py
shutil.copy(os.path.join(src_root, "app", "api", "endpoints", "health.py"), os.path.join(dst_root, "backend", "app", "api", "endpoints", "health.py"))

# Copy prompting.py -> ai/prompting.py
with open(os.path.join(src_root, "app", "core", "prompting.py"), "r", encoding="utf-8") as f:
    prompt_content = f.read()
with open(os.path.join(dst_root, "backend", "app", "ai", "prompting.py"), "w", encoding="utf-8") as f:
    f.write(prompt_content)

# Copy categorization.py -> ai/categorization.py
with open(os.path.join(src_root, "app", "services", "categorization.py"), "r", encoding="utf-8") as f:
    cat_content = f.read()
cat_content = cat_content.replace("app.core.prompting", "app.ai.prompting")
with open(os.path.join(dst_root, "backend", "app", "ai", "categorization.py"), "w", encoding="utf-8") as f:
    f.write(cat_content)

# Copy ocr_service.py -> services/ocr_service.py
shutil.copy(os.path.join(src_root, "app", "services", "ocr_service.py"), os.path.join(dst_root, "backend", "app", "services", "ocr_service.py"))

# Copy analytics.py -> insights/analytics.py
with open(os.path.join(src_root, "app", "services", "analytics.py"), "r", encoding="utf-8") as f:
    ana_content = f.read()
ana_content = ana_content.replace("app.core.prompting", "app.ai.prompting")
with open(os.path.join(dst_root, "backend", "app", "insights", "analytics.py"), "w", encoding="utf-8") as f:
    f.write(ana_content)

# Copy recommendation.py -> recommendations/recommendation.py
with open(os.path.join(src_root, "app", "services", "recommendation.py"), "r", encoding="utf-8") as f:
    rec_content = f.read()
rec_content = rec_content.replace("app.core.prompting", "app.ai.prompting")
with open(os.path.join(dst_root, "backend", "app", "recommendations", "recommendation.py"), "w", encoding="utf-8") as f:
    f.write(rec_content)

# Copy root files
shutil.copy(os.path.join(src_root, "requirements.txt"), os.path.join(dst_root, "backend", "requirements.txt"))
if os.path.exists(os.path.join(src_root, ".env")):
    shutil.copy(os.path.join(src_root, ".env"), os.path.join(dst_root, "backend", ".env"))
if os.path.exists(os.path.join(src_root, "README.md")):
    shutil.copy(os.path.join(src_root, "README.md"), os.path.join(dst_root, "README.md"))

print("Migration completed successfully!")
