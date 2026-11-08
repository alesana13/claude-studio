#!/usr/bin/env python3
"""Generate README.md + SOURCES.md for claude-studio from manifest.json."""
import json
from pathlib import Path

OUT = Path('/home/hatch/workspace/claude-studio')
m = json.load(open(OUT / 'manifest.json'))

CAT_ORDER = ['VIDEO', 'MOTION', 'BLENDER', '3D WEB']
CAT_EMOJI = {'VIDEO': '🎬', 'MOTION': '✨', 'BLENDER': '🧊', '3D WEB': '🌐'}

def short(desc, n=180):
    d = ' '.join(desc.split())
    return d if len(d) <= n else d[:n].rstrip() + '…'

lines = []
lines.append('# Claude Studio')
lines.append('')
lines.append('Satu repo berisi **215 skill agen** untuk project **Video & 3D** — dikumpulkan dari 12 repo GitHub '
             '(“12 Repo Killer” dari video @jvri.sa di Threads). Tiap skill adalah folder berisi `SKILL.md` '
             'plus referensi/script pendukungnya, siap dibaca dan dipakai agen AI (Claude Code, Muse, dan agen lain).')
lines.append('')
lines.append('## Cara pakai')
lines.append('')
lines.append('**Untuk agen:** baca `skills/<nama-skill>/SKILL.md` saat mengerjakan tugas terkait. '
             'Tidak perlu install apa-apa — repo ini adalah katalog skill yang bisa dibaca langsung.')
lines.append('')
lines.append('**Untuk Claude Code (install permanen):** salin skill yang dibutuhkan ke folder skill Claude Code:')
lines.append('')
lines.append('```bash')
lines.append('cp -r skills/video-shotcraft ~/.claude/skills/')
lines.append('cp -r skills/gsap-core ~/.claude/skills/')
lines.append('# …atau semua skill sekaligus:')
lines.append('cp -r skills/* ~/.claude/skills/')
lines.append('```')
lines.append('')
lines.append('**Untuk agen lain (Muse / Hermes / dsb.):** arahkan agen ke repo ini dan minta ia membaca '
             '`skills/<nama>/SKILL.md` yang relevan, atau salin folder skill ke folder skill agen tersebut.')
lines.append('')
lines.append('## Isi repo')
lines.append('')
lines.append('| Folder | Isi |')
lines.append('|---|---|')
lines.append('| `skills/` | 215 skill (lihat indeks di bawah) |')
lines.append('| `tools/mcp-for-blender/` | MCP server Blender — jembatan agar agen bisa mengendalikan Blender (addon + server Python) |')
lines.append('| `SOURCES.md` | Daftar 12 repo asal + lisensi |')
lines.append('| `assemble.py` | Script yang merakit repo ini dari repo asal (bisa dijalankan ulang saat ada update) |')
lines.append('| `manifest.json` | Indeks skill dalam format JSON (nama, sumber, kategori, deskripsi) |')
lines.append('')
lines.append('## Indeks skill')
lines.append('')
for cat in CAT_ORDER:
    items = [x for x in m if x['category'] == cat]
    if not items:
        continue
    lines.append(f'### {CAT_EMOJI[cat]} {cat} ({len(items)} skill)')
    lines.append('')
    for x in items:
        lines.append(f"- **{x['name']}** — {short(x['description'])} _(sumber: {x['source']})_")
    lines.append('')

lines.append('## Catatan')
lines.append('')
lines.append('- Skill yang sama di beberapa repo asal hanya diambil **satu** (versi kanonik dari repo aslinya yang menang; '
             'salinan vendored di OpenMontage dilewati). Contoh: `gsap-core` diambil dari `greensock/gsap-skills`, '
             'bukan dari salinan di OpenMontage.')
lines.append('- Media demo berukuran besar (video mp4, BGM, galeri, folder `docs/` berisi video) **tidak** ikut disalin '
             'agar repo tetap ringan; media lengkap tetap ada di repo asal masing-masing.')
lines.append('- `tools/mcp-for-blender` adalah tool (bukan skill): butuh Blender + Python untuk jalan; '
             'lihat `tools/mcp-for-blender/README.md`.')
lines.append('- Lisensi tiap skill mengikuti repo asalnya (mayoritas MIT/Apache-2.0); lihat `SOURCES.md`.')
lines.append('')
lines.append('## Sumber')
lines.append('')
lines.append('Daftar lengkap 12 repo asal ada di [`SOURCES.md`](SOURCES.md).')
lines.append('')
(OUT / 'README.md').write_text('\n'.join(lines), encoding='utf-8')
print('README.md ditulis')

# ---- SOURCES.md ----
srcs = [
    ('heygen-com/hyperframes', 'VIDEO', 'https://github.com/heygen-com/hyperframes'),
    ('remotion-dev/skills', 'VIDEO', 'https://github.com/remotion-dev/skills'),
    ('calesthio/OpenMontage', 'VIDEO', 'https://github.com/calesthio/OpenMontage'),
    ('Vincentwei1021/video-shotcraft', 'VIDEO', 'https://github.com/Vincentwei1021/video-shotcraft'),
    ('greensock/gsap-skills', 'MOTION', 'https://github.com/greensock/gsap-skills'),
    ('Tejashmakwana/motionmaxxing', 'MOTION', 'https://github.com/Tejashmakwana/motionmaxxing'),
    ('ahujasid/mcp-for-blender', 'BLENDER', 'https://github.com/ahujasid/mcp-for-blender'),
    ('arjun988/blender-skills', 'BLENDER', 'https://github.com/arjun988/blender-skills'),
    ('achimala/dream-loop', 'BLENDER', 'https://github.com/achimala/dream-loop'),
    ('majidmanzarpour/threejs-game-skills', '3D WEB', 'https://github.com/majidmanzarpour/threejs-game-skills'),
    ('wheresryan22/anatomy', '3D WEB', 'https://github.com/wheresryan22/anatomy'),
    ('viettranx/3dviz-pro-max', '3D WEB', 'https://github.com/viettranx/3dviz-pro-max'),
]
from collections import Counter
cnt = Counter(x['source'] for x in m)
sl = []
sl.append('# Sumber — 12 repo asal')
sl.append('')
sl.append('Diambil 8 November 2026 (shallow snapshot, branch `main`). Lisensi mengikuti tiap repo asal; '
         'file `LICENSE` tiap skill (bila ada) ikut tersalin di folder skill-nya.')
sl.append('')
sl.append('| # | Repo | Kategori | Skill yang diambil | URL |')
sl.append('|---|---|---|---|---|')
for i, (repo, cat, url) in enumerate(srcs, 1):
    extra = ' (+ tool `tools/mcp-for-blender`)' if repo == 'ahujasid/mcp-for-blender' else ''
    sl.append(f'| {i:02d} | `{repo}` | {cat} | {cnt.get(repo, 0)} skill{extra} | {url} |')
sl.append('')
sl.append('Sumber daftar: video @jvri.sa di Threads — “12 skills, one 3D studio”.')
sl.append('')
(OUT / 'SOURCES.md').write_text('\n'.join(sl), encoding='utf-8')
print('SOURCES.md ditulis')
