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
    # Quick regex for simple style strings like style="font-variation-settings: 'FILL' 1;"
    # Let's just handle this specific one manually
    jsx_str = jsx_str.replace('style="font-variation-settings: \'FILL\' 1;"', 'style={{ fontVariationSettings: "\'FILL\' 1" }}')
    
    # Comments: <!-- ... --> to {/* ... */}
    jsx_str = re.sub(r'<!--(.*?)-->', r'{/* \1 */}', jsx_str, flags=re.DOTALL)
    
    # Fix inline checked attribute
    jsx_str = jsx_str.replace('checked=""', 'defaultChecked')
    
    return jsx_str

with open("simulation_raw.html", "r", encoding="utf-8") as f:
    sim_html = f.read()

# Extract from <div class="p-8 max-w-7xl mx-auto w-full space-y-8"> to the end of main
start_idx = sim_html.find('<div class="p-8 max-w-7xl mx-auto w-full space-y-8">')
end_idx = sim_html.find('</main>')

sim_content = sim_html[start_idx:end_idx]
fab_content = sim_html[sim_html.find('<!-- Contextual FAB -->'):sim_html.find('</body>')]

sim_jsx = convert_to_jsx(sim_content + fab_content)

with open("src/pages/Simulation.jsx", "w", encoding="utf-8") as f:
    f.write('export default function Simulation() {\n  return (\n    <>\n')
    f.write(sim_jsx)
    f.write('\n    </>\n  );\n}')

# Resources
with open("resources_raw.html", "r", encoding="utf-8") as f:
    res_html = f.read()

# Extract from <section class="mb-16 pt-8"> to </footer>
start_idx2 = res_html.find('<section class="mb-16 pt-8">')
end_idx2 = res_html.find('</main>')

res_content = res_html[start_idx2:end_idx2]
res_jsx = convert_to_jsx(res_content)

with open("src/pages/Resources.jsx", "w", encoding="utf-8") as f:
    f.write('export default function Resources() {\n  return (\n    <div className="pt-8">\n')
    f.write(res_jsx)
    f.write('\n    </div>\n  );\n}')

print("Done converting")
