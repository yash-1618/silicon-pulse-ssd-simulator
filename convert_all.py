import re

def convert_to_jsx(html_str):
    # Convert class to className
    jsx_str = html_str.replace('class="', 'className="')
    # Close self-closing tags (input, img, hr, br)
    jsx_str = re.sub(r'(<input[^>]+)(?<!/)>', r'\1 />', jsx_str)
    jsx_str = re.sub(r'(<img[^>]+)(?<!/)>', r'\1 />', jsx_str)
    jsx_str = re.sub(r'(<hr[^>]*)(?<!/)>', r'\1 />', jsx_str)
    jsx_str = re.sub(r'(<br[^>]*)(?<!/)>', r'\1 />', jsx_str)
    
    # Convert style strings
    jsx_str = jsx_str.replace('style="font-variation-settings: \\\'FILL\\\' 1;"', 'style={{ fontVariationSettings: "\\\'FILL\\\' 1" }}')
    jsx_str = jsx_str.replace('style="background-color: #0b1326;"', 'style={{ backgroundColor: "#0b1326" }}')
    
    # Convert inline styles with templates
    # This is tricky, let's just do a naive replacement for common styles we see
    jsx_str = re.sub(r'style="background-color: (.*?);"', r'style={{ backgroundColor: "\1" }}', jsx_str)
    
    # Comments: <!-- ... --> to {/* ... */}
    jsx_str = re.sub(r'<!--(.*?)-->', r'{/* \1 */}', jsx_str, flags=re.DOTALL)
    
    # Fix inline attributes
    jsx_str = jsx_str.replace('checked=""', 'defaultChecked')
    jsx_str = jsx_str.replace('onclick', 'onClick')
    jsx_str = jsx_str.replace('for="', 'htmlFor="')
    
    # Remove script tags as they are not valid in JSX
    jsx_str = re.sub(r'<script.*?>.*?</script>', '', jsx_str, flags=re.DOTALL)
    
    return jsx_str

def process_file(raw_file, out_file, component_name):
    with open(raw_file, "r", encoding="utf-8") as f:
        html = f.read()

    start_idx = html.find('<main')
    if start_idx == -1:
        print(f"Could not find <main> in {raw_file}")
        return
        
    # find the end of the opening main tag
    start_content_idx = html.find('>', start_idx) + 1
    end_idx = html.find('</main>')

    content = html[start_content_idx:end_idx]
    
    # Extract Contextual FAB if it exists
    fab_idx = html.find('<!-- Contextual FAB -->')
    fab_content = ""
    if fab_idx != -1:
        fab_end_idx = html.find('</body>')
        fab_content = html[fab_idx:fab_end_idx]

    jsx_content = convert_to_jsx(content + fab_content)

    with open(out_file, "w", encoding="utf-8") as f:
        f.write(f'export default function {component_name}() {{\n  return (\n    <>\n')
        f.write(jsx_content)
        f.write('\n    </>\n  );\n}')
        
    print(f"Successfully created {out_file}")

files = [
    ("dashboard_raw.html", "src/pages/Dashboard.jsx", "Dashboard"),
    ("blockmap_raw.html", "src/pages/BlockMap.jsx", "BlockMap"),
    ("simulation_raw.html", "src/pages/Simulation.jsx", "Simulation"),
    ("resources_raw.html", "src/pages/Resources.jsx", "Resources")
]

for raw, out, name in files:
    process_file(raw, out, name)
