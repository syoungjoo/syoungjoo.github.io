# Gallery metadata

Each file here is **optional metadata** for an event folder under
`assets/img/gallery/<slug>/`.

## How to add a new event

1. Create a folder: `assets/img/gallery/<slug>/` (slug = any folder name, e.g. `2026-03-kickoff`).
2. Drop photos in — `.jpg`, `.jpeg`, `.png`, `.webp`, `.gif` are auto-detected.
3. *(Optional)* Create `_data/gallery/<slug>.yml` with any of:
   ```yaml
   title: My Event Title
   date: 2026-03-15      # free-form; used for sorting (ISO preferred)
   place: Seoul, Korea
   cover: photo1.jpg     # defaults to the first photo alphabetically
   ```

No YAML file? The slug becomes the title and events are sorted by slug (reverse).
Prefix slugs with `YYYY-MM-DD` for automatic chronological order.
