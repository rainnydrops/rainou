import os
import re
import shutil

# ─── CONFIG ───────────────────────────────────────────────
POSTS_DIR = "content/cyber"   # Change this if your folder is different
DRY_RUN   = True              # Set to True to preview changes without touching files
# ──────────────────────────────────────────────────────────

def bundle_notes(posts_dir, dry_run):
    entries = os.listdir(posts_dir)
    md_files = [f for f in entries if f.endswith(".md")]

    if not md_files:
        print("⚠️  No .md files found in", posts_dir)
        return

    top_resources = os.path.join(posts_dir, "_resources")

    print(f"Found {len(md_files)} note(s) to bundle.\n")
    if dry_run:
        print("🔎 DRY RUN — no files will be changed.\n")

    for filename in md_files:
        note_name  = filename[:-3]  # strip .md
        src_md     = os.path.join(posts_dir, filename)
        bundle_dir = os.path.join(posts_dir, note_name)
        dest_md    = os.path.join(bundle_dir, "index.md")

        print(f"📄 {filename}")

        # ── Read markdown and fix image paths ──
        with open(src_md, "r", encoding="utf-8") as f:
            content = f.read()

        changes = []

        def replace_path(match):
            alt      = match.group(1)
            img_path = match.group(2)

            # Skip external URLs
            if img_path.startswith("http://") or img_path.startswith("https://"):
                return match.group(0)

            img_filename = os.path.basename(img_path)
            new_path     = f"_resources/{img_filename}"

            if img_path != new_path:
                changes.append((img_path, new_path))

            return f"![{alt}]({new_path})"

        new_content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_path, content)

        for old, new in changes:
            print(f"   🖼️  {old}  →  {new}")

        if not dry_run:
            # ── Create bundle folder ──
            os.makedirs(bundle_dir, exist_ok=True)

            # ── Write index.md ──
            with open(dest_md, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"   ✅ Written → {dest_md}")

            # ── Copy _resources into bundle ──
            if os.path.exists(top_resources):
                dest_resources = os.path.join(bundle_dir, "_resources")
                if not os.path.exists(dest_resources):
                    shutil.copytree(top_resources, dest_resources)
                    print(f"   📁 Copied _resources → {dest_resources}")

            # ── Remove original .md ──
            os.remove(src_md)
            print(f"   🗑️  Removed original {filename}")
        else:
            print(f"   → Would create: {bundle_dir}/index.md")
            if os.path.exists(top_resources):
                print(f"   → Would copy _resources into: {bundle_dir}/")

        print()

    # ── Remove top-level _resources after all bundles are done ──
    if not dry_run and os.path.exists(top_resources):
        shutil.rmtree(top_resources)
        print("🗑️  Removed top-level _resources (already copied into each bundle)\n")

    print("✅ All done! Your notes are now Hugo page bundles.")


if __name__ == "__main__":
    if not os.path.exists(POSTS_DIR):
        print(f"❌ Directory not found: {POSTS_DIR}")
        print("   Make sure you run this script from the root of your Hugo site.")
    else:
        print(f"🔍 Scanning: {POSTS_DIR}\n")
        bundle_notes(POSTS_DIR, DRY_RUN)
