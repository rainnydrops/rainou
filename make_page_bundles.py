import os
import re
import shutil
from urllib.parse import unquote

# ─── CONFIG ───────────────────────────────────────────────
POSTS_DIR = "content/music"   # Change this if your folder is different
DRY_RUN   = False               # Set to False to apply changes for real
# ──────────────────────────────────────────────────────────

def get_image_extension(filename):
    """Return lowercase file extension e.g. '.png'"""
    _, ext = os.path.splitext(filename)
    return ext.lower()


def get_referenced_images(content):
    """Return list of decoded image filenames found in markdown, in order."""
    matches = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", content)
    seen   = []
    result = []
    for _, path in matches:
        if path.startswith("http://") or path.startswith("https://"):
            continue
        decoded = unquote(os.path.basename(path))
        if decoded not in seen:
            seen.append(decoded)
            result.append(decoded)
    return result


def bundle_notes(posts_dir, dry_run):
    entries       = os.listdir(posts_dir)
    md_files      = [f for f in entries if f.endswith(".md")]
    top_resources = os.path.join(posts_dir, "_resources")

    if not md_files:
        print("⚠️  No .md files found in", posts_dir)
        return

    if not os.path.exists(top_resources):
        print(f"⚠️  No _resources folder found at: {top_resources}")
        return

    print(f"Found {len(md_files)} note(s) to bundle.")
    print(f"Source _resources: {top_resources}\n")
    if dry_run:
        print("🔎 DRY RUN — no files will be changed.\n")

    for filename in md_files:
        note_name  = filename[:-3]          # strip .md
        src_md     = os.path.join(posts_dir, filename)
        bundle_dir = os.path.join(posts_dir, note_name)
        dest_md    = os.path.join(bundle_dir, "index.md")

        print(f"📄 {filename}  →  {bundle_dir}/")

        # ── Read source markdown ──
        with open(src_md, "r", encoding="utf-8") as f:
            content = f.read()

        # ── Build a mapping: original filename → numbered filename ──
        referenced = get_referenced_images(content)
        rename_map = {}  # original name → e.g. "1.png"

        if referenced:
            print(f"   🖼️  {len(referenced)} image(s) → renaming to numbers:")
            for i, img in enumerate(referenced, start=1):
                ext         = get_image_extension(img)
                new_name    = f"{i}{ext}"
                src_img     = os.path.join(top_resources, img)
                exists      = os.path.exists(src_img)
                status      = "✅" if exists else "❌ NOT FOUND"
                rename_map[img] = new_name
                print(f"      {status}  {img}  →  {new_name}")
        else:
            print("   (no images referenced)")

        # ── Rewrite image paths in markdown using numbered filenames ──
        def replace_path(match):
            alt      = match.group(1)
            img_path = match.group(2)
            if img_path.startswith("http://") or img_path.startswith("https://"):
                return match.group(0)
            original = unquote(os.path.basename(img_path))
            new_name = rename_map.get(original, original)
            return f"![{alt}]({new_name})"

        new_content = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", replace_path, content)

        if not dry_run:
            # ── Create bundle folder ──
            os.makedirs(bundle_dir, exist_ok=True)

            # ── Write index.md ──
            with open(dest_md, "w", encoding="utf-8") as f:
                f.write(new_content)
            print(f"   📝 index.md written")

            # ── Copy and rename images into bundle folder (same level as index.md) ──
            for original, new_name in rename_map.items():
                src_img  = os.path.join(top_resources, original)
                dest_img = os.path.join(bundle_dir, new_name)
                if os.path.exists(src_img):
                    shutil.copy2(src_img, dest_img)
                    print(f"   📁 {original}  →  {bundle_dir}/{new_name}")
                else:
                    print(f"   ⚠️  Skipped (not found): {original}")

            # ── Remove original .md ──
            os.remove(src_md)
            print(f"   🗑️  Removed source: {filename}")
        else:
            print(f"   → Would write: {bundle_dir}/index.md")
            for original, new_name in rename_map.items():
                src_img = os.path.join(top_resources, original)
                if os.path.exists(src_img):
                    print(f"   → Would copy+rename:  {original}  →  {bundle_dir}/{new_name}")
                else:
                    print(f"   → ⚠️  Not found in _resources: {original}")

        print()

    # ── Clean up top-level _resources if empty ──
    if not dry_run:
        remaining = os.listdir(top_resources)
        if remaining:
            print(f"ℹ️  _resources has {len(remaining)} unreferenced file(s) remaining:")
            for f in remaining:
                print(f"   - {f}")
        else:
            shutil.rmtree(top_resources)
            print("🗑️  Removed _resources (empty after bundling)")

    print("\n✅ Done! Example bundle structure:")
    print(f"   {posts_dir}/")
    print(f"   └── Gobuster/")
    print(f"       ├── index.md   ← ![alt](1.png)")
    print(f"       ├── 1.png")
    print(f"       └── 2.png")


if __name__ == "__main__":
    if not os.path.exists(POSTS_DIR):
        print(f"❌ Directory not found: {POSTS_DIR}")
        print("   Run this script from the root of your Hugo site.")
    else:
        print(f"🔍 Scanning: {POSTS_DIR}\n")
        bundle_notes(POSTS_DIR, DRY_RUN)
