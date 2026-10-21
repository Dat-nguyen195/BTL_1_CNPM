"""
render_all_diagrams.py – Renders all 46 PlantUML diagrams using Smetana engine
"""

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
JAR_PATH = REPO_ROOT / "tools" / "plantuml.jar"

def main():
    puml_files = sorted(list(REPO_ROOT.glob("docs/diagrams/Use-case detail-scenario/**/*.puml")))
    print(f"Found {len(puml_files)} diagrams to render...")
    
    success = 0
    failed = 0
    
    for i, p in enumerate(puml_files, 1):
        print(f"[{i}/{len(puml_files)}] Rendering {p.name}...", end=" ", flush=True)
        cmd = [
            "java",
            "-DPLANTUML_LIMIT_SIZE=16384",
            "-jar", str(JAR_PATH),
            "-Playout=smetana",
            "-charset", "UTF-8",
            "-tpng",
            str(p)
        ]
        res = subprocess.run(cmd, capture_output=True, text=True)
        if res.returncode == 0:
            print("OK")
            success += 1
        else:
            print("FAILED")
            print(res.stderr)
            failed += 1
            
    print(f"\nRender completed: {success} succeeded, {failed} failed.")
    if failed > 0:
        sys.exit(1)

if __name__ == "__main__":
    main()
