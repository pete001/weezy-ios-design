#!/usr/bin/env python3
"""Export fresh native/web capture evidence to an exact-ID GitHub review pack."""
import argparse
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from PIL import Image, ImageStat, ImageChops


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def export(args):
    destination = Path(args.output)
    destination.mkdir(parents=True, exist_ok=True)
    inventory = list(csv.DictReader(Path(args.inventory).open()))
    raw = Path(args.raw)
    directories = [raw / 'weezy-v26-captures', raw / 'weezy-pop-studio-captures']
    candidates = {}
    records = {}
    for directory in directories:
        for path in sorted(directory.glob('*.png')):
            candidates[path.name] = path
        for path in sorted(directory.glob('*manifest.json')):
            payload = json.loads(path.read_text())
            if not isinstance(payload, list):
                continue
            for record in payload:
                filename = record.get('filename')
                if filename:
                    records[filename] = record
    hints = {}
    if args.mapping:
        hints = {row['id']: Path(row.get('image', '')).name for row in json.loads(Path(args.mapping).read_text())['screens']}
    parked = {
        'G-35R-basket-verified-reward': 'Parked for launch: cash/points rewards are not enabled. Collection progress and badges are the launch reward route. No active reward screen is claimed.',
        'G-28-pick-your-code': 'Future custom-code picker: not enabled in the launch app. Existing generated friend codes and their management are implemented.',
        'SHOPIFY-CODE': 'Shopify-owned secure authentication page. No current authorized live code session was captured; no mock is substituted.',
        'SHOPIFY-CHECKOUT': 'Shopify-owned checkout. No fresh live customer checkout was opened for this isolated review. Earlier unpaid verification is separate evidence and is not passed off as build-31 capture.',
        'W-07-app-first-open': 'The designed first-open/deferred-install invitation screen is not implemented. Installed-app manual link handling uses the captured X-04 import view; it is not substituted for this distinct design.'
    }
    base = {'build': args.build, 'device': args.device, 'scale': 3, 'viewport': {'width': 393, 'height': 852}, 'fixture': 'Isolated Claire design account; no production customer mutations'}
    manifest = []
    selected = {}
    warnings = []

    def image_entry(screen_id, path, row=None, **extra):
        with Image.open(path) as source:
            if source.size != (1179, 2556):
                raise ValueError(f'{screen_id}: expected fresh 393x852pt @3x, found {source.size}')
            image = source.convert('RGB')
            if max(ImageStat.Stat(image.resize((40, 80))).stddev) < 2:
                raise ValueError(f'{screen_id}: blank capture')
            file = screen_id + '.jpg'
            image.save(destination / file, format='JPEG', quality=80, optimize=True, subsampling=0)
        record = records.get(path.name, {})
        text_size = record.get('textSize') or ('accessibility5' if 'largest' in screen_id.lower() else 'large')
        entry = dict(base, id=screen_id, file=file, textSize=text_size,
                     sourceKind='production SwiftUI content render in XCTest; controlled 393pt canvas; not shipping AppRoot/live service evidence',
                     sourceFile=path.name, sha256=digest(destination / file), **extra)
        if row:
            entry['title'] = row['title']
            entry['journey'] = row['journey']
            entry['designOwner'] = row['owner']
        if record.get('source') or record.get('viewName'):
            entry['view'] = record.get('source') or record['viewName']
        manifest.append(entry)
        return entry

    for row in inventory:
        screen_id = row['id']
        if screen_id in parked:
            manifest.append(dict(base, id=screen_id, notCaptured=True, reason=parked[screen_id], title=row['title'], journey=row['journey']))
            continue
        if screen_id.startswith('W-') and screen_id != 'W-07-app-first-open':
            continue
        path = None
        # Literal production-content fixtures supersede older general fixtures.
        for filename in (screen_id + '-normal.png', screen_id + '.png', hints.get(screen_id)):
            if filename and filename in candidates:
                path = candidates[filename]
                break
        if screen_id == 'W-07-app-first-open':
            path = candidates.get('X-04-import-shared-wishlist.png') or next((p for n, p in candidates.items() if n.startswith('X-04-import-shared-wishlist-') and '-scroll-' not in n), None)
        if path is None:
            exact_records = [candidates[n] for n, r in records.items() if r.get('boardID') == screen_id and n in candidates]
            if len(exact_records) == 1:
                path = exact_records[0]
        if path is None:
            # Legacy capture helpers use short board IDs and a title slug.
            prefix = screen_id.split('-')[:2]
            board = '-'.join(prefix)
            wanted = [candidates[n] for n, r in records.items() if r.get('boardID') == board and n in candidates]
            if len(wanted) == 1:
                path = wanted[0]
        if path is None:
            manifest.append(dict(base, id=screen_id, notCaptured=True, reason='No fresh exact-state capture produced by this run; not substituted with an older build or design reference.', title=row['title'], journey=row['journey']))
            warnings.append(screen_id)
            continue
        selected[screen_id] = path
        entry = image_entry(screen_id, path, row)
        if 'basket' in row['journey'].lower() or 'summary' in screen_id:
            entry['fixturePricing'] = 'Board 4 reference fixture; verified £138 summary = £166 - £10 - £18; mock quote, not a live Shopify attestation. Set-only pieces state excludes the two loose pieces as specified by that reference.'
        if row['owner'] == 'Merchant content':
            entry['merchantDependency'] = 'Production pending/unavailable presentation is visible where merchant set/media configuration is still required. No live merchant content was edited.'
        if screen_id == 'W-07-app-first-open':
            entry['reason'] = 'Installed-app invitation uses the same current import view as X-04. Automatic deferred installation/link delivery is not implemented or proved by this still.'
            entry['sharedViewWith'] = 'X-04-import-shared-wishlist'

    used = {e['id'] for e in manifest}
    for screen_id, path in selected.items():
        scroll_file = path.with_name(path.stem + '-scrolls.json')
        if not scroll_file.exists():
            continue
        previous_path = path
        for index, segment in enumerate(json.loads(scroll_file.read_text()), 1):
            segment_path = path.with_name(segment['filename'])
            # A short sheet can have a scrollable feed behind it. Do not publish
            # continuations whose only change is the dimmed background header.
            with Image.open(previous_path) as before, Image.open(segment_path) as after:
                crop = (0, 660, 1179, 2454)
                difference = ImageChops.difference(before.convert('RGB').crop(crop), after.convert('RGB').crop(crop))
                if max(ImageStat.Stat(difference).mean) < 0.12:
                    continue
            previous_path = segment_path
            continuation_id = screen_id + '-more' + (f'-{index}' if index > 1 else '')
            while continuation_id in used:
                index += 1
                continuation_id = screen_id + f'-more-{index}'
            used.add(continuation_id)
            image_entry(continuation_id, segment_path, parentId=screen_id,
                        scrollOffset=segment['scrollOffset'], scrollHeight=segment['scrollHeight'], scrollViewportHeight=segment['viewportHeight'], textSizeOverride='accessibility5' if 'largest' in screen_id.lower() else 'large')

    web_manifest = raw / 'web' / 'manifest.json'
    if web_manifest.exists():
        for segment in json.loads(web_manifest.read_text()):
            row = next((r for r in inventory if r['id'] == segment['id']), None)
            entry = image_entry(segment['id'], raw / 'web' / segment['filename'], row)
            entry['device'] = 'Chrome mobile emulation; 393pt iPhone content viewport'
            entry['sourceKind'] = segment['sourceKind']
            entry['scrollOffset'] = segment['scrollOffset']
            if segment.get('parentId'):
                entry['parentId'] = segment['parentId']
            entry['fixture'] = 'Synthetic Claire loopback web fixture with Board 9 example values; synthetic paid webhook for gift receipt; no live checkout or customer mutation'
    for row in inventory:
        if row['id'] not in {e['id'] for e in manifest}:
            manifest.append(dict(base, id=row['id'], notCaptured=True, reason='No fresh web capture produced by this run.', title=row['title'], journey=row['journey']))
            warnings.append(row['id'])

    order = {r['id']: i for i, r in enumerate(inventory)}
    manifest.sort(key=lambda e: (order.get(e.get('parentId', e['id']), len(order)), e.get('parentId') is not None, e['id']))
    (destination / 'capture-details.json').write_text(json.dumps(manifest, indent=2) + '\n')
    concise = []
    for entry in manifest:
        short = {key: entry[key] for key in ('id', 'build', 'device', 'scale', 'file', 'sha256', 'notCaptured', 'reason', 'parentId', 'scrollOffset') if key in entry}
        if not entry.get('notCaptured'):
            short['captureKind'] = 'web-content' if entry['id'].startswith('W-') else 'native-content'
            if 'largest' in entry['id'].lower():
                short['textSize'] = 'accessibility5'
        concise.append(short)
    (destination / 'manifest.json').write_text('[\n' + ',\n'.join('  ' + json.dumps(entry, ensure_ascii=False) for entry in concise) + '\n]\n')
    with (destination / 'capture-inventory.csv').open('w', newline='') as file:
        columns = ['id', 'parentId', 'build', 'file', 'title', 'journey', 'textSize', 'notCaptured', 'reason']
        writer = csv.DictWriter(file, fieldnames=columns, lineterminator='\n')
        writer.writeheader()
        for entry in manifest:
            writer.writerow({key: entry.get(key, '') for key in columns})
    captured = [e['file'] for e in manifest if not e.get('notCaptured')]
    batches = [captured[i:i+50] for i in range(0, len(captured), 50)]
    (destination / 'import-batches.json').write_text(json.dumps(batches, indent=2) + '\n')
    coverage = {'build': args.build, 'generatedAt': datetime.now(timezone.utc).isoformat(), 'inventoryScreens': len(inventory), 'capturedInventoryScreens': sum(e['id'] in order and not e.get('notCaptured') for e in manifest), 'images': len(captured), 'additionalContinuations': sum(e.get('parentId') is not None for e in manifest), 'notCaptured': [e['id'] for e in manifest if e.get('notCaptured')], 'unexpectedMissing': warnings, 'imageFormat': 'JPEG', 'jpegQuality': 80, 'pixelWidth': 1179, 'pixelHeight': 2556, 'batches': [len(batch) for batch in batches]}
    (destination / 'validation.json').write_text(json.dumps(coverage, indent=2) + '\n')
    previous = Path(args.previous) if args.previous else None
    before = {e['id']: e for e in json.loads((previous / 'manifest.json').read_text())} if previous and (previous / 'manifest.json').exists() else {}
    changes = {'baseline': str(previous) if before else None, 'new': [], 'changed': [], 'unchanged': [], 'removed': sorted(set(before) - {e['id'] for e in manifest})}
    for entry in manifest:
        old = before.get(entry['id'])
        category = 'new' if old is None else ('unchanged' if (old.get('sha256'), old.get('reason'), old.get('notCaptured')) == (entry.get('sha256'), entry.get('reason'), entry.get('notCaptured')) else 'changed')
        changes[category].append(entry['id'])
    (destination / 'changes.json').write_text(json.dumps(changes, indent=2) + '\n')
    print(json.dumps(coverage, indent=2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--raw', required=True, help='Fresh raw folder with weezy-v26-captures, weezy-pop-studio-captures and web subdirectories')
    parser.add_argument('--output', required=True)
    parser.add_argument('--inventory', required=True)
    parser.add_argument('--mapping', help='Optional existing inventory metadata for legacy filename aliases; no images are imported from it')
    parser.add_argument('--build', type=int, required=True)
    parser.add_argument('--device', default='iPhone 16 Pro simulator / iOS 27.0; controlled 393x852pt content canvas')
    parser.add_argument('--previous', help='Previous build review folder for hash-based changed-screen report')
    export(parser.parse_args())
