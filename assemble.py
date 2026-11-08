#!/usr/bin/env python3
"""Assemble ~/workspace/claude-studio from the 12 upstream repos in _upstream/.
Rules:
- skills/<name>/ : one dir per UNIQUE skill (dedup by frontmatter name, canonical source wins)
- tools/mcp-for-blender/ : the runnable MCP server (small)
- Heavy demo media excluded (videos/demos/gallery/examples-assets, BGM mp3s, docs media)
- README.md + SOURCES.md generated from SKILL.md frontmatter.
"""
import os, re, shutil, json
from pathlib import Path

UP = Path('/home/hatch/workspace/claude-studio/_upstream')
OUT = Path('/home/hatch/workspace/claude-studio')
SKILLS = OUT / 'skills'
TOOLS = OUT / 'tools'

# name -> (source_repo, category)
SOURCES = {}

def fm(path):
    """Read name/description from SKILL.md frontmatter."""
    try:
        txt = Path(path).read_text(errors='ignore')
    except Exception:
        return None, None
    m = re.match(r'^---\n(.*?)\n---', txt, re.S)
    if not m:
        return None, None
    name = re.search(r'^name:\s*(.+)$', m.group(1), re.M)
    desc = re.search(r'^description:\s*(.+)$', m.group(1), re.M | re.S)
    d = desc.group(1).strip() if desc else ''
    # description may span lines; take first line-ish
    d = ' '.join(d.splitlines()).strip()
    d = re.sub(r'\s+', ' ', d)
    return (name.group(1).strip() if name else None), d

def copy_skill(src_dir, dest_name, source_repo, category, exclude=()):
    """Copy a skill dir (with SKILL.md) to skills/<dest_name>/, skipping excluded subdirs/files."""
    src = Path(src_dir)
    skill_md = src / 'SKILL.md'
    if not skill_md.exists():
        print(f'  SKIP (no SKILL.md): {src_dir}')
        return False
    name, desc = fm(skill_md)
    key = (name or dest_name).strip().lower()
    if key in SOURCES:
        print(f'  DUP {key} (sudah dari {SOURCES[key][0]}, lewati {source_repo})')
        return False
    dst = SKILLS / dest_name
    if dst.exists():
        shutil.rmtree(dst)
    def ignore(dirpath, names):
        out = []
        for n in names:
            if n in exclude:
                out.append(n)
            # skip big media files anywhere
            if re.search(r'\.(mp4|mov|webm|mkv)$', n, re.I):
                out.append(n)
        return out
    shutil.copytree(src, dst, ignore=ignore)
    SOURCES[key] = (source_repo, category, dest_name, desc or '')
    print(f'  OK {dest_name} <- {source_repo}')
    return True

def copy_collection(base, source_repo, category):
    """Copy every skill subdir of a collection (each has SKILL.md)."""
    base = Path(base)
    for d in sorted(base.iterdir()):
        if d.is_dir() and (d / 'SKILL.md').exists():
            copy_skill(d, d.name, source_repo, category)

SKILLS.mkdir(parents=True, exist_ok=True)
TOOLS.mkdir(parents=True, exist_ok=True)

print('== 1) KOLEKSI KANONIK (didahulukan, menang atas vendored copy) ==')
copy_collection(UP / 'heygen-com_hyperframes' / 'skills', 'heygen-com/hyperframes', 'VIDEO')
copy_collection(UP / 'remotion-dev_skills' / 'skills', 'remotion-dev/skills', 'VIDEO')
copy_collection(UP / 'greensock_gsap-skills' / 'skills', 'greensock/gsap-skills', 'MOTION')
copy_collection(UP / 'majidmanzarpour_threejs-game-skills' / 'skills', 'majidmanzarpour/threejs-game-skills', '3D WEB')
copy_collection(UP / 'arjun988_blender-skills' / '.claude' / 'skills', 'arjun988/blender-skills', 'BLENDER')

print('== 2) SKILL TUNGGAL ==')
copy_skill(UP / 'Vincentwei1021_video-shotcraft', 'video-shotcraft', 'Vincentwei1021/video-shotcraft', 'VIDEO',
           exclude={'assets', 'demos', 'gallery', 'videos', 'publish', 'jianying-export', '.git'})
copy_skill(UP / 'Tejashmakwana_motionmaxxing', 'motionmaxxing', 'Tejashmakwana/motionmaxxing', 'MOTION',
           exclude={'docs', '.git'})
copy_skill(UP / 'achimala_dream-loop', 'dream-loop', 'achimala/dream-loop', 'BLENDER',
           exclude={'.git'})
copy_skill(UP / 'viettranx_3dviz-pro-max' / 'skills' / '3dviz-pro-max', '3dviz-pro-max', 'viettranx/3dviz-pro-max', '3D WEB',
           exclude={'.git'})
copy_skill(UP / 'wheresryan22_anatomy', 'anatomy', 'wheresryan22/anatomy', '3D WEB',
           exclude={'examples', '.git'})

print('== 3) OPENMONTAGE (terakhir: hanya skill yang belum ada) ==')
copy_collection(UP / 'calesthio_OpenMontage' / '.agents' / 'skills', 'calesthio/OpenMontage', 'VIDEO')

print('== TOOLS ==')
# mcp-for-blender: runnable MCP server, small (2.4M)
mb = UP / 'ahujasid_mcp-for-blender'
dst = TOOLS / 'mcp-for-blender'
if dst.exists():
    shutil.rmtree(dst)
shutil.copytree(mb, dst, ignore=shutil.ignore_patterns('.git', '__pycache__', '*.pyc'))
print(f'  OK tools/mcp-for-blender <- ahujasid/mcp-for-blender')

# ---- summary ----
total = sum(1 for _ in SKILLS.iterdir())
size = sum(p.stat().st_size for p in SKILLS.rglob('*') if p.is_file())
print(f'\nTOTAL SKILL UNIK: {total}  |  ukuran skills/: {size/1024/1024:.1f} MB')
# save manifest for README generation
manifest = [{'name': k, 'source': v[0], 'category': v[1], 'dir': v[2], 'description': v[3]}
            for k, v in sorted(SOURCES.items(), key=lambda kv: (kv[1][1], kv[0]))]
(OUT / 'manifest.json').write_text(json.dumps(manifest, indent=2, ensure_ascii=False))
print('manifest.json ditulis:', len(manifest), 'entri')
