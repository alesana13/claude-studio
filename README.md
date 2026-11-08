# Claude Studio

Satu repo berisi **215 skill agen** untuk project **Video & 3D** — dikumpulkan dari 12 repo GitHub (“12 Repo Killer” dari video @jvri.sa di Threads). Tiap skill adalah folder berisi `SKILL.md` plus referensi/script pendukungnya, siap dibaca dan dipakai agen AI (Claude Code, Muse, dan agen lain).

## Cara pakai

**Untuk agen:** baca `skills/<nama-skill>/SKILL.md` saat mengerjakan tugas terkait. Tidak perlu install apa-apa — repo ini adalah katalog skill yang bisa dibaca langsung.

**Untuk Claude Code (install permanen):** salin skill yang dibutuhkan ke folder skill Claude Code:

```bash
cp -r skills/video-shotcraft ~/.claude/skills/
cp -r skills/gsap-core ~/.claude/skills/
# …atau semua skill sekaligus:
cp -r skills/* ~/.claude/skills/
```

**Untuk agen lain (Muse / Hermes / dsb.):** arahkan agen ke repo ini dan minta ia membaca `skills/<nama>/SKILL.md` yang relevan, atau salin folder skill ke folder skill agen tersebut.

## Isi repo

| Folder | Isi |
|---|---|
| `skills/` | 215 skill (lihat indeks di bawah) |
| `tools/mcp-for-blender/` | MCP server Blender — jembatan agar agen bisa mengendalikan Blender (addon + server Python) |
| `SOURCES.md` | Daftar 12 repo asal + lisensi |
| `assemble.py` | Script yang merakit repo ini dari repo asal (bisa dijalankan ulang saat ada update) |
| `manifest.json` | Indeks skill dalam format JSON (nama, sumber, kategori, deskripsi) |

## Indeks skill

### 🎬 VIDEO (100 skill)

- **3d-asset-generation** — Generate, reconstruct, inspect, and route production 3D assets for OpenMontage worlds using Atlas Cloud, fal.ai, licensed catalogs, and Blender. _(sumber: calesthio/OpenMontage)_
- **acestep** — AI music generation with ACE-Step 1.5 — background music, vocal tracks, covers, stem extraction for video production. Use when generating music, soundtracks, jingles, or working wi… _(sumber: calesthio/OpenMontage)_
- **agents** — Build voice AI agents with ElevenLabs. Use when creating voice assistants, customer service bots, interactive voice characters, or any real-time voice conversation experience. lice… _(sumber: calesthio/OpenMontage)_
- **ai-video-gen** — | Generate AI videos from text prompts using multiple provider gateways. Use when: (1) Generating videos from text descriptions, (2) Creating AI-generated video clips for content p… _(sumber: calesthio/OpenMontage)_
- **atlas-cloud** — Generate or edit images and videos through the Atlas Cloud gateway. Use for Atlas-hosted Seedance 2.5/2.0, Gemini Omni Flash, MiniMax H3, Seedream 5.0, GPT Image 2, Nano Banana 2,… _(sumber: calesthio/OpenMontage)_
- **avatar-video** — | Create AI avatar videos with precise control over avatars, voices, scripts, scenes, and backgrounds using HeyGen's v2 API. Use when: (1) Choosing a specific avatar and voice for… _(sumber: calesthio/OpenMontage)_
- **azure-speech-to-text** — Transcribe audio to text using Azure AI Speech (Fast Transcription REST API). Use when converting audio/video to text, generating subtitles, or processing spoken content in OpenMon… _(sumber: calesthio/OpenMontage)_
- **azure-text-to-speech** — Generate neural narration audio using Azure AI Speech (REST text-to-speech). Use when synthesizing voiceovers or narration in OpenMontage. Optional cloud TTS provider — preferred w… _(sumber: calesthio/OpenMontage)_
- **beautiful-mermaid** — Render Mermaid diagrams as SVG and PNG using the Beautiful Mermaid library. Use when the user asks to render a Mermaid diagram. _(sumber: calesthio/OpenMontage)_
- **bfl-api** — BFL FLUX API integration guide covering endpoints, async polling patterns, rate limiting, error handling, webhooks, and regional endpoints with Python and TypeScript code examples.… _(sumber: calesthio/OpenMontage)_
- **canvas-procedural-animation** — Use p5.js/canvas for local procedural character effects: particles, weather, squash/stretch, walk cycles, and environmental motion. license: MIT _(sumber: calesthio/OpenMontage)_
- **character-animation-qa** — Review local character animation with schema checks, Playwright browser previews, frame sampling, and FFmpeg/ffprobe final output checks. license: MIT _(sumber: calesthio/OpenMontage)_
- **character-rigging** — Build data-driven 2D character rigs for local animation: parts, pivots, layers, constraints, views, and reusable rig packages. license: MIT _(sumber: calesthio/OpenMontage)_
- **comfyui** — Use when working with ComfyUI workflows in OpenMontage, including comfyui_image/comfyui_video/comfyui_music, custom workflow_json/workflow_path inputs, output_node selection, missi… _(sumber: calesthio/OpenMontage)_
- **create-video** — | Create videos from a text prompt using HeyGen's Video Agent. Use when: (1) Creating a video from a description or idea, (2) Generating explainer, demo, or marketing videos from a… _(sumber: calesthio/OpenMontage)_
- **d3-viz** — Creating interactive data visualisations using d3.js. This skill should be used when creating custom charts, graphs, network diagrams, geographic visualisations, or any complex SVG… _(sumber: calesthio/OpenMontage)_
- **dashscope** — DashScope (Alibaba Cloud Bailian / 阿里云百炼) integration — image generation (qwen-image-2.0-pro), text-to-speech (qwen3-tts-flash), and ASR with word-level timestamps (qwen3-asr-flash… _(sumber: calesthio/OpenMontage)_
- **doubao-tts** — Generate Mandarin and multilingual narration with Volcengine Doubao Speech 2.0. Use when creating Chinese voiceovers, when the user prefers Doubao/Volcengine/火山引擎/豆包 TTS, or when n… _(sumber: calesthio/OpenMontage)_
- **elevenlabs** — Generate AI voiceovers, sound effects, and music using ElevenLabs APIs. Use when creating audio content for videos, podcasts, or games. Triggers include generating voiceovers, narr… _(sumber: calesthio/OpenMontage)_
- **faceswap** — | Swap faces in a video using AI via the HeyGen API. Use when: (1) Replacing a face in a video with another face, (2) Face swapping from a source image onto a target video, (3) Cre… _(sumber: calesthio/OpenMontage)_
- **ffmpeg** — Video and audio processing with FFmpeg. Use for format conversion, resizing, compression, audio extraction, and preparing assets for Remotion. Triggers include converting GIF to MP… _(sumber: calesthio/OpenMontage)_
- **figma** — Bring Figma into a HyperFrames video - rendered assets, brand tokens, components, storyboard frames as reconstructed motion (frames read as states, not slides), shaders and connect… _(sumber: heygen-com/hyperframes)_
- **fish-audio-tts** — Generate expressive, multilingual narration with fish.audio (S1 / S2-generation models) and reuse cloned voices via reference_id. Use when the user prefers fish.audio/Fish Audio TT… _(sumber: calesthio/OpenMontage)_
- **flux-best-practices** — Comprehensive guide for BFL FLUX image generation models. Covers prompting, T2I, I2I, structured JSON, hex colors, typography, multi-reference editing, and model-specific best prac… _(sumber: calesthio/OpenMontage)_
- **framer-motion** — Use when implementing Disney's 12 animation principles with Framer Motion in React applications _(sumber: calesthio/OpenMontage)_
- **gemini-omni** — | Generate and conversationally edit short videos with stable Google Gemini Omni Flash (`gemini-omni-1.1-flash`). Use when: (1) iterating on a clip with natural-language edits inst… _(sumber: calesthio/OpenMontage)_
- **grok-media** — xAI Grok image and video generation guide covering authentication, endpoints, prompt structure, image editing, reference-image video, and async polling. metadata: author: OpenMonta… _(sumber: calesthio/OpenMontage)_
- **heygen** — | [DEPRECATED] Use `create-video` for prompt-based video generation or `avatar-video` for precise avatar/scene control. This legacy skill combines both workflows — the newer focuse… _(sumber: calesthio/OpenMontage)_
- **hyperframes** — Read first to make, edit, animate or render any video with HyperFrames (HTML rendered to video), including launch films, explainers, music videos, charts, maps, vertical clips, tit… _(sumber: heygen-com/hyperframes)_
- **hyperframes-animation** — "All animation knowledge for HyperFrames — atomic motion rules, multi-phase scene blueprints, scene transitions, broader motion-design techniques, AND the seven runtime adapters (G… _(sumber: calesthio/OpenMontage)_
- **hyperframes-cli** — The HyperFrames CLI by job - scaffold, check, look at frames, edit the timeline, preview, render locally or in the cloud, publish, project history - plus reading its JSON and recov… _(sumber: heygen-com/hyperframes)_
- **hyperframes-core** — The HyperFrames composition contract — build one renderable project. Use for composition structure, the `data-*` timing attributes, `class="clip"`, tracks, sub-compositions, variab… _(sumber: calesthio/OpenMontage)_
- **hyperframes-creative** — Non-animation creative direction for HyperFrames videos. Use for design spec (frame.md / design.md) handling, palettes, typography, narration, beat planning, audio-reactive visuals… _(sumber: calesthio/OpenMontage)_
- **hyperframes-media** — Audio and media assets for HyperFrames compositions, produced by one shared audio engine (`scripts/audio.mjs`) — multi-provider TTS (HeyGen / ElevenLabs / Kokoro local), background… _(sumber: calesthio/OpenMontage)_
- **hyperframes-registry** — About 450 ready-made HyperFrames blocks and components installed as editable source - transitions, overlays, titles, kinetic type, captions, charts, map overlays, 3D, camera moves.… _(sumber: heygen-com/hyperframes)_
- **kling-official** — Official Kling direct API guidance for OpenMontage providers. Use before calling `kling_official_video`, `kling_official_image`, `kling_tts`, `kling_avatar`, or `kling_lip_sync`. m… _(sumber: calesthio/OpenMontage)_
- **lottie-bodymovin** — Use when implementing Disney's 12 animation principles with Lottie animations exported from After Effects _(sumber: calesthio/OpenMontage)_
- **ltx2** — AI video generation with LTX-2.3 22B — text-to-video, image-to-video clips for video production. Use when generating video clips, animating images, creating b-roll, animated backgr… _(sumber: calesthio/OpenMontage)_
- **lyria** — Generate and validate music with Google Lyria through the Gemini Interactions API. Use before calling OpenMontage `google_music`, designing Lyria 3.5 or Clip prompts, using image-t… _(sumber: calesthio/OpenMontage)_
- **manim-composer** — | Trigger when: (1) User wants to create an educational/explainer video, (2) User has a vague concept they want visualized, (3) User mentions "3b1b style" or "explain like 3Blue1Br… _(sumber: calesthio/OpenMontage)_
- **manimce-best-practices** — | Trigger when: (1) User mentions "manim" or "Manim Community" or "ManimCE", (2) Code contains `from manim import *`, (3) User runs `manim` CLI commands, (4) Working with Scene, Ma… _(sumber: calesthio/OpenMontage)_
- **manimgl-best-practices** — | Trigger when: (1) User mentions "manimgl" or "ManimGL" or "3b1b manim", (2) Code contains `from manimlib import *`, (3) User runs `manimgl` CLI commands, (4) Working with Interac… _(sumber: calesthio/OpenMontage)_
- **media-use** — Get or make any media for a HyperFrames video - music, sound effects, images, icons, logos, voiceover, avatar and generated video, transcripts, cutouts, colour grades and looks - w… _(sumber: heygen-com/hyperframes)_
- **minimax-h3** — | Generate MiniMax H3 (Hailuo 3.0) video through the official MiniMax v2 API, fal.ai, Runway, ComfyUI Partner Nodes, or local open weights in ComfyUI. Use for 4-15 second 2K clips,… _(sumber: calesthio/OpenMontage)_
- **motion-graphics** — > Use when the user wants a short, design-led motion graphic where motion is the message: kinetic typography, stat or number count-up, chart/data-viz hit, logo sting, brand lockup,… _(sumber: calesthio/OpenMontage)_
- **music** — Generate music using ElevenLabs Music API. Use when creating instrumental tracks, songs with lyrics, background music, jingles, or any AI-generated music composition. Supports prom… _(sumber: calesthio/OpenMontage)_
- **music-to-video** — "Use when the user has a music track (an audio file, or a video to pull audio from) and wants a beat-synced HyperFrames video, calm to hard-hitting. The music drives everything: on… _(sumber: calesthio/OpenMontage)_
- **playwright-recording** — Record browser interactions as video using Playwright. Use for capturing demo videos, app walkthroughs, and UI flows for Remotion videos. Triggers include recording a demo, capturi… _(sumber: calesthio/OpenMontage)_
- **pose-library-design** — Design reusable 2D character pose libraries, action cycles, and expression states for data-driven animation. license: MIT _(sumber: calesthio/OpenMontage)_
- **provider-model-refresh** — Use the September 2026 image, video, speech and Avatar V adapters with explicit model/host contracts. _(sumber: calesthio/OpenMontage)_
- **provider-refresh-oct23** — API contracts and production routing for the October 23, 2026 provider refresh. _(sumber: calesthio/OpenMontage)_
- **remotion** — Toolkit-specific Remotion patterns — custom transitions, shared components, and project conventions. For core Remotion framework knowledge (hooks, animations, rendering, etc.), see… _(sumber: calesthio/OpenMontage)_
- **remotion-best-practices** — Router for all Remotion skills version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-captions** — Transcribing, displaying and animating captions version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-create** — Create a new Remotion video version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-docs** — Search Remotion documentation version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-interactivity** — Structure Remotion markup for interactivity version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-license** — Find Remotion license information, FAQs, terms, and where to buy a license. version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-maps** — Remotion Map animation knowledge version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-markup** — Content, animation and effects best practices version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-multimedia** — Interacting with Mediabunny version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-render** — Export a Remotion video version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-saas** — Build an app with Remotion version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-studio** — Preview a Remotion video version: 4.0.541 _(sumber: remotion-dev/skills)_
- **remotion-to-hyperframes** — Bring existing video code or footage into HyperFrames and verify it frame by frame against the original - Remotion first, also Motion Canvas, Lottie, Three.js, p5.js, canvas or pla… _(sumber: heygen-com/hyperframes)_
- **remotion-upgrade** — Upgrade Remotion, and related packages version: 4.0.541 _(sumber: remotion-dev/skills)_
- **reverse-any-video** — Rebuild any video file as an editable HyperFrames project - motion graphics, talking heads, live action or AI-generated footage. Measure and watch it, rebuild every layer, then che… _(sumber: heygen-com/hyperframes)_
- **seedance-2-0** — | Generate cinematic clips with ByteDance Seedance 2.0 — the preferred premium video model in OpenMontage when a paid gateway is configured. Use when: (1) producing trailers, tease… _(sumber: calesthio/OpenMontage)_
- **seedance-2-5** — | Generate 4-30 second cinematic video with ByteDance Seedance 2.5 through fal.ai, Volcengine Ark, Runway, or ComfyUI Partner Nodes. Use for long single generations, synchronized a… _(sumber: calesthio/OpenMontage)_
- **setup-api-key** — Guides users through setting up an ElevenLabs API key for ElevenLabs MCP tools. Use when the user needs to configure an ElevenLabs API key, when ElevenLabs tools fail due to missin… _(sumber: calesthio/OpenMontage)_
- **slideshow** — Build a HyperFrames slideshow to present live - slides, fragment reveals, branching hotspots and presenter mode with speaker notes, served by `hyperframes present` - or turn an exi… _(sumber: heygen-com/hyperframes)_
- **sound-effects** — Generate sound effects from text descriptions using ElevenLabs. Use when creating sound effects, generating audio textures, producing ambient sounds, cinematic impacts, UI sounds,… _(sumber: calesthio/OpenMontage)_
- **speech-to-text** — Transcribe audio to text using ElevenLabs Scribe v2. Use when converting audio/video to text, generating subtitles, transcribing meetings, or processing spoken content. license: MI… _(sumber: calesthio/OpenMontage)_
- **style-sampling** — Make a new episode in a proven video style - Collage Explainer, Finance Explainer, Animated Science Explainer, 3D Brand Explainer, 3D True Crime - on the person's topic. Use for "a… _(sumber: heygen-com/hyperframes)_
- **svg-character-animation** — Animate SVG character rigs with GSAP, CSS transforms, Remotion frame control, and HyperFrames-compatible browser previews. license: MIT _(sumber: calesthio/OpenMontage)_
- **synthetic-screen-recording** — Synthetic terminal-style screen recording guidance for Remotion `TerminalScene`. license: MIT _(sumber: calesthio/OpenMontage)_
- **tailwind-design-system** — Build scalable design systems with Tailwind CSS v4, design tokens, component libraries, and responsive patterns. Use when creating component libraries, implementing design systems,… _(sumber: calesthio/OpenMontage)_
- **text-to-speech** — HeyGen native Voice1 and catalog speech, voice discovery, timestamps, and streaming. _(sumber: calesthio/OpenMontage)_
- **threejs-animation** — Three.js animation - keyframe animation, skeletal animation, morph targets, animation mixing. Use when animating objects, playing GLTF animations, creating procedural motion, or bl… _(sumber: calesthio/OpenMontage)_
- **threejs-fundamentals** — Three.js scene setup, cameras, renderer, Object3D hierarchy, coordinate systems. Use when setting up 3D scenes, creating cameras, configuring renderers, managing object hierarchies… _(sumber: calesthio/OpenMontage)_
- **threejs-geometry** — Three.js geometry creation - built-in shapes, BufferGeometry, custom geometry, instancing. Use when creating 3D shapes, working with vertices, building custom meshes, or optimizing… _(sumber: calesthio/OpenMontage)_
- **threejs-interaction** — Three.js interaction - raycasting, controls, mouse/touch input, object selection. Use when handling user input, implementing click detection, adding camera controls, or creating in… _(sumber: calesthio/OpenMontage)_
- **threejs-lighting** — Three.js lighting - light types, shadows, environment lighting. Use when adding lights, configuring shadows, setting up IBL, or optimizing lighting performance. _(sumber: calesthio/OpenMontage)_
- **threejs-loaders** — Three.js asset loading - GLTF, textures, images, models, async patterns. Use when loading 3D models, textures, HDR environments, or managing loading progress. _(sumber: calesthio/OpenMontage)_
- **threejs-materials** — Three.js materials - PBR, basic, phong, shader materials, material properties. Use when styling meshes, working with textures, creating custom shaders, or optimizing material perfo… _(sumber: calesthio/OpenMontage)_
- **threejs-postprocessing** — Three.js post-processing - EffectComposer, bloom, DOF, screen effects. Use when adding visual effects, color grading, blur, glow, or creating custom screen-space shaders. _(sumber: calesthio/OpenMontage)_
- **threejs-shaders** — Three.js shaders - GLSL, ShaderMaterial, uniforms, custom effects. Use when creating custom visual effects, modifying vertices, writing fragment shaders, or extending built-in mate… _(sumber: calesthio/OpenMontage)_
- **threejs-textures** — Three.js textures - texture types, UV mapping, environment maps, texture settings. Use when working with images, UV coordinates, cubemaps, HDR environments, or texture optimization… _(sumber: calesthio/OpenMontage)_
- **threejs-world-generation** — Build deterministic, editable, free-viewpoint Three.js worlds from text or structured briefs. Use for cinematic 3D terrain, semantic regions, procedural biomes, explicit landmarks,… _(sumber: calesthio/OpenMontage)_
- **vercel-composition-patterns** — React composition patterns that scale. Use when refactoring components with boolean prop proliferation, building flexible component libraries, or designing reusable APIs. Triggers… _(sumber: calesthio/OpenMontage)_
- **vercel-react-best-practices** — React and Next.js performance optimization guidelines from Vercel Engineering. This skill should be used when writing, reviewing, or refactoring React/Next.js code to ensure optima… _(sumber: calesthio/OpenMontage)_
- **video-download** — | Download video and audio from YouTube and 1000+ sites using yt-dlp. No API keys needed. Use when: (1) Downloading a video from YouTube or other sites, (2) Extracting audio from a… _(sumber: calesthio/OpenMontage)_
- **video-edit** — | Edit videos locally using ffmpeg. Trim, concat, resize, speed, overlay, extract audio, compress, and convert. Use when: (1) Trimming or cutting video segments, (2) Concatenating… _(sumber: calesthio/OpenMontage)_
- **video-shotcraft** — Create cinematic product videos from frontend projects or webpages with Remotion, real page captures, shot cards, the Ink Press template, beat sync and sound design. Use for full p… _(sumber: Vincentwei1021/video-shotcraft)_
- **video-toolkit** — Create professional videos autonomously using claude-code-video-toolkit — AI voiceovers, image generation, music, talking heads, and Remotion rendering. metadata: openclaw: emoji:… _(sumber: calesthio/OpenMontage)_
- **video-translate** — | Translate and dub existing videos into multiple languages using HeyGen. Use when: (1) Translating a video into another language, (2) Dubbing video content with lip-sync, (3) Crea… _(sumber: calesthio/OpenMontage)_
- **video-understand** — | Understand video content locally using ffmpeg frame extraction and Whisper transcription. No API keys needed. Use when: (1) Understanding what a video contains, (2) Transcribing… _(sumber: calesthio/OpenMontage)_
- **visual-style** — | Create, extract, and apply portable visual design systems via visual-style.md files. Use when: (1) Creating a visual-style.md design system from scratch, (2) Extracting a visual… _(sumber: calesthio/OpenMontage)_
- **web-design-guidelines** — Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practic… _(sumber: calesthio/OpenMontage)_
- **website-to-video** — "Capture a general website/URL and turn it into a HyperFrames video (site tour, showcase, or social clip from the site's own visuals). Uses headless Chrome screenshots + brand asse… _(sumber: calesthio/OpenMontage)_

### ✨ MOTION (9 skill)

- **gsap-core** — Official GSAP skill for the core API — gsap.to(), from(), fromTo(), easing, duration, stagger, defaults, gsap.matchMedia() (responsive, prefers-reduced-motion). Use when the user a… _(sumber: greensock/gsap-skills)_
- **gsap-frameworks** — Official GSAP skill for Vue, Svelte, and other non-React frameworks — lifecycle, scoping selectors, cleanup on unmount. Use when the user wants animation in Vue, Nuxt, Svelte, Svel… _(sumber: greensock/gsap-skills)_
- **gsap-performance** — Official GSAP skill for performance — prefer transforms, avoid layout thrashing, will-change, batching. Use when optimizing GSAP animations, reducing jank, or when the user asks ab… _(sumber: greensock/gsap-skills)_
- **gsap-plugins** — Official GSAP skill for GSAP plugins — registration, ScrollToPlugin, ScrollSmoother, Flip, Draggable, Inertia, Observer, SplitText, ScrambleText, SVG and physics plugins, CustomEas… _(sumber: greensock/gsap-skills)_
- **gsap-react** — Official GSAP skill for React — useGSAP hook, refs, gsap.context(), cleanup. Use when the user wants animation in React or Next.js, or asks about GSAP with React, useGSAP, or clean… _(sumber: greensock/gsap-skills)_
- **gsap-scrolltrigger** — Official GSAP skill for ScrollTrigger — scroll-linked animations, pinning, scrub, triggers. Use when building or recommending scroll-based animation, parallax, pinned sections, or… _(sumber: greensock/gsap-skills)_
- **gsap-timeline** — Official GSAP skill for timelines — gsap.timeline(), position parameter, nesting, playback. Use when sequencing animations, choreographing keyframes, or when the user asks about an… _(sumber: greensock/gsap-skills)_
- **gsap-utils** — Official GSAP skill for gsap.utils — clamp, mapRange, normalize, interpolate, random, snap, toArray, wrap, pipe. Use when the user asks about gsap.utils, clamp, mapRange, random, s… _(sumber: greensock/gsap-skills)_
- **motionmaxxing** — Direct and build professional motion-graphics films (launch videos, product promos, feature reveals, brand stings, kinetic-type pieces, social ads, CTAs) that read as made by a sen… _(sumber: Tejashmakwana/motionmaxxing)_

### 🧊 BLENDER (95 skill)

- **analog-found-footage-horror** — Analog, VHS, CRT, and found-footage horror aesthetics for Blender shots including camera imperfections and documentary framing. license: MIT metadata: author: https://github.com/ar… _(sumber: arjun988/blender-skills)_
- **animation** — Game-ready animation in Blender including walk/run/idle cycles, combat, mechanical animation, camera animation, constraints, Graph Editor, and NLA workflows via MCP. license: MIT m… _(sumber: arjun988/blender-skills)_
- **anime-style** — Anime and cel-shaded art direction for Blender with hard color breaks, toon shaders, clean silhouettes, and anime proportion language. license: MIT metadata: author: https://github… _(sumber: arjun988/blender-skills)_
- **apocalypse-worlds** — Apocalyptic and dystopian world art direction for Blender including post-apocalyptic, zombie, alien invasion, post-human, dystopian, and utopian contrast sets. license: MIT metadat… _(sumber: arjun988/blender-skills)_
- **archviz** — Architectural visualization in Blender for interiors/exteriors with real-world scale, camera composition, PBR materials, and still/animation delivery via MCP. license: MIT metadata… _(sumber: arjun988/blender-skills)_
- **asset-optimization** — Validates and optimizes Blender assets for polycount, topology, UV efficiency, material count, naming, collections, and game-ready performance. Use before export on all production… _(sumber: arjun988/blender-skills)_
- **biome-worlds** — Biome and setting art direction for Blender covering underwater, desert, arctic, jungle, underground, and floating-island environments. license: MIT metadata: author: https://githu… _(sumber: arjun988/blender-skills)_
- **blender-director** — Use when starting any Blender asset task, planning a production pipeline, coordinating multiple disciplines, or matching a reference photo/concept art. Invoke for game-ready assets… _(sumber: arjun988/blender-skills)_
- **blender-modeler** — Core Blender modeling specialist for Edit Mode, modifiers, collections, precision modeling, and scene organization. Use for general 3D modeling, blockouts, cleanup, non-destructive… _(sumber: arjun988/blender-skills)_
- **body-horror-style** — Body horror art direction for Blender focusing on flesh wrongness, mutation, fusion, and visceral material storytelling. license: MIT metadata: author: https://github.com/arjun988… _(sumber: arjun988/blender-skills)_
- **brutalist-mood** — Brutalist and concrete-monument mood direction for Blender architecture and scenes with raw concrete, monumental scale, and austere composition. license: MIT metadata: author: http… _(sumber: arjun988/blender-skills)_
- **camera-cinematography** — Cinematic camera work in Blender including framing, lenses, composition, camera animation, and shot language beyond basic rendering setup via MCP. license: MIT metadata: author: ht… _(sumber: arjun988/blender-skills)_
- **cartoon-style** — Cartoon art direction for Blender with squash-stretch readable shapes, bold colors, and graphic silhouettes for games and animation. license: MIT metadata: author: https://github.c… _(sumber: arjun988/blender-skills)_
- **character-archetypes** — Character archetype art direction for Blender covering fantasy races, horror creatures, roles (knight, assassin, detective), and body types (mecha, android, chibi, etc.). license:… _(sumber: arjun988/blender-skills)_
- **character-artist** — AAA character modeling for human anatomy, stylization, facial topology, clothing, hair, and animation-ready meshes. Use for game characters, facial expressions, and production char… _(sumber: arjun988/blender-skills)_
- **chibi-style** — Chibi and SD proportion art direction for Blender characters with oversized heads, simplified anatomy, and cute silhouette rules. license: MIT metadata: author: https://github.com/… _(sumber: arjun988/blender-skills)_
- **cloth-sim** — Garment blockout, cloth simulation, pin groups, and bake to shape keys or caches for characters and props in Blender via MCP. license: MIT metadata: author: https://github.com/arju… _(sumber: arjun988/blender-skills)_
- **collision-proxy** — Collision proxy authoring for games including UCX/UHX naming, convex hulls, capsules, and simple collider meshes in Blender via MCP. license: MIT metadata: author: https://github.c… _(sumber: arjun988/blender-skills)_
- **comic-book-style** — Comic book and graphic-novel art direction for Blender with ink-line emphasis, halftone cues, and high-contrast framing. license: MIT metadata: author: https://github.com/arjun988… _(sumber: arjun988/blender-skills)_
- **compositing** — Blender compositor workflows for beauty stacks, render passes, color grade, glare, and delivery outputs via MCP. license: MIT metadata: author: https://github.com/arjun988 version:… _(sumber: arjun988/blender-skills)_
- **cosmic-eldritch-horror** — Cosmic, eldritch, and Lovecraftian horror art direction for Blender with non-Euclidean cues, impossible scale, and incomprehensible forms. license: MIT metadata: author: https://gi… _(sumber: arjun988/blender-skills)_
- **cozy-wholesome-mood** — Cozy, cute, wholesome, relaxing, and peaceful mood direction for Blender assets and scenes. license: MIT metadata: author: https://github.com/arjun988 version: "1.0.0" domain: blen… _(sumber: arjun988/blender-skills)_
- **creature-artist** — AAA creature modeling for fantasy, aliens, monsters, and organic creature design with believable anatomy and movement. Use for creature blockouts, muscle flow, bone structure, and… _(sumber: arjun988/blender-skills)_
- **dark-gritty-mood** — Dark, grim, gritty, rusty, abandoned, decayed, industrial, lonely, and melancholic mood direction for Blender. license: MIT metadata: author: https://github.com/arjun988 version: "… _(sumber: arjun988/blender-skills)_
- **dream-loop** — Build a game or app from a description so that a live screenshot matches a generated rendering. Use when the user says "dream loop" or asks for something built to a very high level… _(sumber: achimala/dream-loop)_
- **dream-surreal-mood** — Dreamlike, surreal, mysterious, mystical, hopeful, and chaotic mood direction for Blender scenes. license: MIT metadata: author: https://github.com/arjun988 version: "1.0.0" domain… _(sumber: arjun988/blender-skills)_
- **dream-weirdcore-style** — Dreamcore, weirdcore, and traumacore-inspired art direction for Blender with nostalgic wrongness, liminal nostalgia, and surreal childhood spaces. license: MIT metadata: author: ht… _(sumber: arjun988/blender-skills)_
- **environment-artist** — AAA environment art for modular kits, buildings, terrain, vegetation, architecture, and scene composition. Use for game-optimized environments, storytelling through space, and modu… _(sumber: arjun988/blender-skills)_
- **export-pipeline** — Production export from Blender to FBX, GLTF, OBJ, USD, and Alembic with scale, pivot, rotation, normals, materials, animation, and collision verification via MCP. license: MIT meta… _(sumber: arjun988/blender-skills)_
- **fantasy-worlds** — Fantasy world-building art direction for Blender covering medieval, high fantasy, dark fantasy, and urban fantasy asset language. license: MIT metadata: author: https://github.com/… _(sumber: arjun988/blender-skills)_
- **folk-horror-style** — Folk horror art direction for Blender with rural ritual uncanny, pastoral daylight dread, and community-wrongness storytelling. license: MIT metadata: author: https://github.com/ar… _(sumber: arjun988/blender-skills)_
- **frutiger-aero-style** — Frutiger Aero art direction for Blender with glossy skeuomorphism, aqua UI cues, nature-tech optimism, and mid-2000s futurism. license: MIT metadata: author: https://github.com/arj… _(sumber: arjun988/blender-skills)_
- **genre-action-combat** — Art direction for action, hack-and-slash, beat 'em up, and fighting-game readable combat spaces and prop language in Blender. license: MIT metadata: author: https://github.com/arju… _(sumber: arjun988/blender-skills)_
- **genre-card-party-idle** — Art direction for card games, deck builders, party games, idle/incremental, educational, and rhythm game presentational spaces in Blender. license: MIT metadata: author: https://gi… _(sumber: arjun988/blender-skills)_
- **genre-metroidvania-roguelike** — Art direction for metroidvania, roguelike, and roguelite games in Blender with biome gates, room modules, and run-readable props. license: MIT metadata: author: https://github.com/… _(sumber: arjun988/blender-skills)_
- **genre-narrative-vn** — Art direction for visual novel, interactive movie, walking simulator, and story-driven presentation spaces in Blender. license: MIT metadata: author: https://github.com/arjun988 ve… _(sumber: arjun988/blender-skills)_
- **genre-open-world-sandbox** — Art direction for open world and sandbox games in Blender with biome landmarks, traversable scale, and discovery props. license: MIT metadata: author: https://github.com/arjun988 v… _(sumber: arjun988/blender-skills)_
- **genre-puzzle-platformer** — Art direction for puzzle and platformer games in Blender with readable interactables, jump volumes, and clear hazard language. license: MIT metadata: author: https://github.com/arj… _(sumber: arjun988/blender-skills)_
- **genre-racing-sports** — Art direction for racing and sports games in Blender with track landmarks, stadium kits, and high-speed readability. license: MIT metadata: author: https://github.com/arjun988 vers… _(sumber: arjun988/blender-skills)_
- **genre-rpg** — Art direction for RPG, JRPG, CRPG, ARPG, and MMORPG worlds in Blender including loot rarity reads and region identity. license: MIT metadata: author: https://github.com/arjun988 ve… _(sumber: arjun988/blender-skills)_
- **genre-shooter** — Art direction for FPS, TPS, shooter, battle royale, and extraction-shooter maps and props in Blender with sightline and cover language. license: MIT metadata: author: https://githu… _(sumber: arjun988/blender-skills)_
- **genre-soulslike** — Art direction for soulslike games in Blender with monumental melancholy spaces, fog gates, bonfire landmarks, and lethal readability. license: MIT metadata: author: https://github.… _(sumber: arjun988/blender-skills)_
- **genre-stealth** — Art direction for stealth-game spaces in Blender with shadow volumes, patrol-friendly layouts, and concealment materials. license: MIT metadata: author: https://github.com/arjun988… _(sumber: arjun988/blender-skills)_
- **genre-strategy-sim** — Art direction for strategy, RTS, turn-based strategy, tower defense, MOBA, city builder, colony sim, and simulation games in Blender. license: MIT metadata: author: https://github.… _(sumber: arjun988/blender-skills)_
- **genre-survival** — Art direction for survival and survival-horror gameplay spaces in Blender emphasizing resource props, crafting readability, and tension routes. license: MIT metadata: author: https… _(sumber: arjun988/blender-skills)_
- **geometry-nodes** — Blender Geometry Nodes for procedural modeling, scatter systems, vegetation, buildings, pipes, cables, and reusable node groups. Use for procedural asset generation and instancing… _(sumber: arjun988/blender-skills)_
- **godot-export** — Godot-specific Blender export favoring GLTF/GLB with correct scale, materials, animation clips, and collision shapes via MCP. license: MIT metadata: author: https://github.com/arju… _(sumber: arjun988/blender-skills)_
- **hair-groom** — Hair and fur grooming in Blender using curves, particle hair, geometry nodes, and game hair-card workflows. Use for characters, creatures, and real-time hair cards via MCP. license… _(sumber: arjun988/blender-skills)_
- **hand-painted-style** — Hand-painted texture art direction for Blender with brushwork albedo, soft value transitions, and stylized PBR restraint. license: MIT metadata: author: https://github.com/arjun988… _(sumber: arjun988/blender-skills)_
- **hard-surface** — AAA hard surface modeling for sci-fi, industrial, military, vehicles, weapons, robotics, and mechanical props. Use for boolean/bevel workflows, panel lines, greebles, chamfers, and… _(sumber: arjun988/blender-skills)_
- **hd-2d-style** — HD-2D art direction combining pixel characters/sprites with 3D environments, depth of field, and theatrical lighting. license: MIT metadata: author: https://github.com/arjun988 ver… _(sumber: arjun988/blender-skills)_
- **historical-worlds** — Historical and period world art direction for Blender including Western, pirate, samurai/ninja, Viking, ancient Egypt/Greece/Rome, Victorian, modern, and military eras. license: MI… _(sumber: arjun988/blender-skills)_
- **horror-style** — Psychological horror art direction for Blender assets inspired by Silent Hill, Resident Evil, Chilla's Art, Fear to Fathom, and Iron Lung. Use for sparse industrial environments, a… _(sumber: arjun988/blender-skills)_
- **indie-horror-aesthetics** — Indie horror aesthetic pack for Blender covering Silent Hill, Fear to Fathom, Puppet Combo, corporate horror, cabin/forest/hospital horror, and related looks. license: MIT metadata… _(sumber: arjun988/blender-skills)_
- **isometric-style** — Isometric and strategy-game art direction for Blender including diorama framing, true-iso camera setup, readable silhouettes, and tile asset rules. license: MIT metadata: author: h… _(sumber: arjun988/blender-skills)_
- **lighting** — Cinematic and game lighting in Blender including three-point lighting, HDRI, horror lighting, volumetrics, rim lighting, and mood-driven illumination. Use for look development and… _(sumber: arjun988/blender-skills)_
- **liminal-space-style** — Liminal space and Backrooms art direction for Blender with empty transitional architecture, wrong familiarity, and endless repetition. license: MIT metadata: author: https://github… _(sumber: arjun988/blender-skills)_
- **lod-pipeline** — Dedicated LOD generation, naming, screen-size targets, and validation for game meshes in Blender via MCP. license: MIT metadata: author: https://github.com/arjun988 version: "1.0.0… _(sumber: arjun988/blender-skills)_
- **lookdev** — Look development loop for Blender assets combining materials, lighting, camera, and screenshot comparison until shading reads correctly via MCP. license: MIT metadata: author: http… _(sumber: arjun988/blender-skills)_
- **lowpoly-style** — Low-poly art direction for Blender inspired by PS1/PS2, Lethal Company, Mouthwashing, and Fear to Fathom. Use for readable silhouettes, minimal polygons, simple materials, and stro… _(sumber: arjun988/blender-skills)_
- **manga-style** — Manga-inspired art direction for Blender emphasizing monochrome value design, speed lines, screentone feel, and manga panel staging. license: MIT metadata: author: https://github.c… _(sumber: arjun988/blender-skills)_
- **mascot-puppet-horror** — Mascot and puppet horror art direction for Blender with cheerful brand characters made wrong, felt/foam materials, and uncanny performance. license: MIT metadata: author: https://g… _(sumber: arjun988/blender-skills)_
- **materials** — Blender PBR and stylized material creation for metal, wood, concrete, fabric, glass, dirt, rust, and procedural shaders. Use for look development, material reuse, and production sh… _(sumber: arjun988/blender-skills)_
- **minimalist-style** — Minimalist and abstract-leaning art direction for Blender with reduced forms, limited palettes, and negative space. license: MIT metadata: author: https://github.com/arjun988 versi… _(sumber: arjun988/blender-skills)_
- **neon-retrofuturism** — Neon, vaporwave, synthwave, and retrofuturistic mood/art direction for Blender with grid horizons, chrome, and dusk palettes. license: MIT metadata: author: https://github.com/arju… _(sumber: arjun988/blender-skills)_
- **noir-style** — Noir art direction for Blender with high-contrast lighting, wet streets, silhouettes, and monochrome or limited-color grading. license: MIT metadata: author: https://github.com/arj… _(sumber: arjun988/blender-skills)_
- **painterly-style** — Painterly art direction spanning watercolor and oil-painting looks for Blender using soft edges, pigment texture, and illustrative lighting. license: MIT metadata: author: https://… _(sumber: arjun988/blender-skills)_
- **physics-sim** — Rigid body, soft body, and destruction setups in Blender including constraints, cell fracture debris, and baked caches via MCP. license: MIT metadata: author: https://github.com/ar… _(sumber: arjun988/blender-skills)_
- **pixel-art-style** — Pixel-art and texel-constrained art direction for Blender assets destined for pixel rendering, low-res textures, or HD-2D-adjacent pixel reads. license: MIT metadata: author: https… _(sumber: arjun988/blender-skills)_
- **procedural-modeling** — Procedural asset creation for rocks, buildings, vegetation, roads, terrain, pipes, cables, and sci-fi panels using Geometry Nodes and modifier-based workflows in Blender via MCP. l… _(sumber: arjun988/blender-skills)_
- **prop-artist** — Everyday and hero prop modeling for furniture, tools, household objects, kitbash parts, and readable game props. Use when hard-surface is too sci-fi/mechanical and the asset is a g… _(sumber: arjun988/blender-skills)_
- **psx-horror-style** — PS1/PSX-era horror art direction combining low-poly affine textures, limited color depth, fog, and psychological horror staging for Blender assets. license: MIT metadata: author: h… _(sumber: arjun988/blender-skills)_
- **qa-review** — Production QA gate for Blender assets using viewport screenshots, validation checklists, naming audits, and ship/no-ship verdicts via MCP. license: MIT metadata: author: https://gi… _(sumber: arjun988/blender-skills)_
- **realistic-style** — Photorealistic AAA art direction for Blender including photogrammetry cleanup, real-world scale, high-poly workflows, PBR accuracy, and scan optimization. Use for cinematic and AAA… _(sumber: arjun988/blender-skills)_
- **rendering** — Blender rendering with Cycles and Eevee including sampling, denoising, camera setup, render passes, color management, and render optimization. Use for final output and look validat… _(sumber: arjun988/blender-skills)_
- **retopology** — Production retopology for animation-ready, low-poly, quad-dominant meshes with proper edge loops and efficient polygon flow. Use after sculpting or high-poly modeling before riggin… _(sumber: arjun988/blender-skills)_
- **retro-16bit-style** — Retro 16-bit art direction for Blender-assisted SNES/Genesis-era color richness, dither cues, and sprite-like clarity. license: MIT metadata: author: https://github.com/arjun988 ve… _(sumber: arjun988/blender-skills)_
- **retro-8bit-style** — Retro 8-bit art direction for Blender-assisted pixel/low-res aesthetics inspired by NES-era constraints. license: MIT metadata: author: https://github.com/arjun988 version: "1.0.0"… _(sumber: arjun988/blender-skills)_
- **rigging** — Production rigging in Blender with armatures, IK/FK, constraints, weight painting, mechanical rigs, facial rigs, and drivers. Use before animation on deforming assets via MCP. lice… _(sumber: arjun988/blender-skills)_
- **scene-assembly** — Large scene layout in Blender with collections, linking, overrides, streaming-friendly organization, and set assembly via MCP. license: MIT metadata: author: https://github.com/arj… _(sumber: arjun988/blender-skills)_
- **sci-fi-punk-worlds** — Sci-fi and punk world art direction for Blender including hard sci-fi, space, cyberpunk, steampunk, dieselpunk, atompunk, solarpunk, biopunk, and clockpunk. license: MIT metadata:… _(sumber: arjun988/blender-skills)_
- **sculpting** — Blender sculpting for organic and hard surface detail using Dyntopo, multiresolution, brushes, alpha workflow, wrinkles, and damage. Use when high-frequency surface detail is neede… _(sumber: arjun988/blender-skills)_
- **set-dressing** — Set dressing and environmental storytelling placement for interiors and exteriors using prop density, narrative clusters, and readability rules via MCP. license: MIT metadata: auth… _(sumber: arjun988/blender-skills)_
- **stop-motion-craft-style** — Stop-motion and craft aesthetics for Blender including claymation, paper craft, and handmade physical-material cues. license: MIT metadata: author: https://github.com/arjun988 vers… _(sumber: arjun988/blender-skills)_
- **stylized-style** — Stylized art direction for Blender with shape language, exaggeration, color harmony, NPR rendering, and hand-painted asset workflows. Use for non-photorealistic game and animation… _(sumber: arjun988/blender-skills)_
- **texture-workflow** — Production texture workflow for atlases, baking AO/curvature/normal/roughness maps, decals, and texture memory optimization. Use for game-ready texture pipelines in Blender via MCP… _(sumber: arjun988/blender-skills)_
- **unity-export** — Unity-specific Blender export for scale, axis, materials, humanoid/generic rigs, LODs, and collision import via MCP. license: MIT metadata: author: https://github.com/arjun988 vers… _(sumber: arjun988/blender-skills)_
- **unreal-export** — Unreal Engine-specific Blender export for FBX scale, LODs, UCX collision, sockets, materials, and skeletal mesh workflows via MCP. license: MIT metadata: author: https://github.com… _(sumber: arjun988/blender-skills)_
- **uv-workflow** — Production UV unwrapping for seam placement, UV packing, texel density, UDIM, lightmap UVs, and modular UV layouts. Use when preparing meshes for texturing and engine export in Ble… _(sumber: arjun988/blender-skills)_
- **vector-style** — Vector-clean art direction for Blender with flat fills, sharp silhouettes, and UI-like graphic clarity. license: MIT metadata: author: https://github.com/arjun988 version: "1.0.0"… _(sumber: arjun988/blender-skills)_
- **vegetation-artist** — Vegetation and foliage authoring for Blender including trees, plants, grass cards, canopy LODs, and game-friendly leaf atlases via MCP. license: MIT metadata: author: https://githu… _(sumber: arjun988/blender-skills)_
- **vehicle-artist** — Dedicated vehicle modeling for cars, trucks, aircraft, ships, boats, mechs, and transit assets with proportion, panel flow, and game LOD awareness in Blender via MCP. license: MIT… _(sumber: arjun988/blender-skills)_
- **vfx-fx** — Cinematic and game VFX in Blender including smoke, fire, particles, trails, and Geometry Nodes FX setups via MCP. license: MIT metadata: author: https://github.com/arjun988 version… _(sumber: arjun988/blender-skills)_
- **visual-console-eras** — Visual era art direction for Blender covering PS1–PS5 stylistic cues, retro arcade, DOS, CRT, VHS, and film-grain presentation. license: MIT metadata: author: https://github.com/ar… _(sumber: arjun988/blender-skills)_
- **voxel-style** — Voxel and Minecraft-adjacent art direction for Blender with block grid modeling, limited palettes, and chunk-friendly assets. license: MIT metadata: author: https://github.com/arju… _(sumber: arjun988/blender-skills)_

### 🌐 3D WEB (11 skill)

- **3dviz-pro-max** — Design and build expressive 3D scenes, explainers and interactive models with grounded subject knowledge. Use for 3D creation or edits, including scientific visualization and spati… _(sumber: viettranx/3dviz-pro-max)_
- **anatomy** — Build crafted, highly detailed, interactive isometric SVG figures that explain a technical idea as a real physical object (a test rig, a dial gauge, a cabinet of drawers, a plotter… _(sumber: wheresryan22/anatomy)_
- **threejs-3d-generator** — "Generate, texture, rig, animate, stylize, convert, and download 3D assets for Three.js games via the Tripo API. Use for text-to-3D, image-to-3D, game-ready GLB/FBX, characters, cr… _(sumber: majidmanzarpour/threejs-game-skills)_
- **threejs-aaa-graphics-builder** — "Upgrade Three.js games from prototype visuals to premium browser graphics: art-direction critique, procedural model building, material and texture libraries, world prop kits, shad… _(sumber: majidmanzarpour/threejs-game-skills)_
- **threejs-audio-generator** — "Generate, convert, clean, and integrate audio for Three.js browser games with ElevenLabs: sound effects, looping ambience, music tracks and loops (menu, gameplay, boss, victory/de… _(sumber: majidmanzarpour/threejs-game-skills)_
- **threejs-debug-profiler** — "Debug and profile Three.js browser games: blank canvases, render and runtime bugs, asset and audio loading, animation, resize, mobile input, plus performance profiling of draw cal… _(sumber: majidmanzarpour/threejs-game-skills)_
- **threejs-game-director** — "Entrypoint for building, upgrading, and finishing Three.js browser games. Routes work across the sibling threejs-* skills for gameplay, graphics, UI, 3D/image/audio asset generati… _(sumber: majidmanzarpour/threejs-game-skills)_
- **threejs-game-ui-designer** — "Design premium Three.js game UI: HUDs, menus, overlays, pause/win/lose screens, settings, icon controls, touch UI, typography, responsive layout, safe areas, text fit, and UI/worl… _(sumber: majidmanzarpour/threejs-game-skills)_
- **threejs-gameplay-systems** — "Build and iterate playable Three.js game systems: starter scaffold, architecture, design briefs, core loops, level and encounter design, entities, input, camera, collision and phy… _(sumber: majidmanzarpour/threejs-game-skills)_
- **threejs-image-generator** — "Generate and edit 2D image assets for Three.js games with Google's Gemini image API: concept sheets, image-to-3D inputs, texture and material references, sky and background plates… _(sumber: majidmanzarpour/threejs-game-skills)_
- **threejs-qa-release** — "Verify and release Three.js browser games: playtest QA, automated bot playtests, mobile and responsive checks, production builds, static-hosting base paths, debug gating, bundle r… _(sumber: majidmanzarpour/threejs-game-skills)_

## Catatan

- Skill yang sama di beberapa repo asal hanya diambil **satu** (versi kanonik dari repo aslinya yang menang; salinan vendored di OpenMontage dilewati). Contoh: `gsap-core` diambil dari `greensock/gsap-skills`, bukan dari salinan di OpenMontage.
- Media demo berukuran besar (video mp4, BGM, galeri, folder `docs/` berisi video) **tidak** ikut disalin agar repo tetap ringan; media lengkap tetap ada di repo asal masing-masing.
- `tools/mcp-for-blender` adalah tool (bukan skill): butuh Blender + Python untuk jalan; lihat `tools/mcp-for-blender/README.md`.
- Lisensi tiap skill mengikuti repo asalnya (mayoritas MIT/Apache-2.0); lihat `SOURCES.md`.

## Sumber

Daftar lengkap 12 repo asal ada di [`SOURCES.md`](SOURCES.md).
