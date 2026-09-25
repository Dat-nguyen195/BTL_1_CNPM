import xml.etree.ElementTree as ET
import urllib.parse
import re
import json

def unquote(text):
    if text is None: return ""
    return urllib.parse.unquote(text)

try:
    tree = ET.parse('/media/nguyen-dat/New Volume/HK1_261/Công nghệ Phần mềm/BTL_1/smart-emobility-hub/docs/diagrams/system/smartEhub.drawio')
    root = tree.getroot()
    
    nodes = {}
    edges = []
    
    for mxCell in root.iter('mxCell'):
        cell_id = mxCell.get('id')
        value = mxCell.get('value', '')
        clean_value = unquote(re.sub(r'<[^>]+>', ' ', value)).strip()
        style = mxCell.get('style', '')
        
        # Is it an edge?
        if mxCell.get('edge') == '1':
            source = mxCell.get('source')
            target = mxCell.get('target')
            edges.append({
                'id': cell_id,
                'value': clean_value,
                'source': source,
                'target': target,
                'style': style
            })
        elif mxCell.get('vertex') == '1':
            nodes[cell_id] = {
                'value': clean_value,
                'style': style,
                'parent': mxCell.get('parent')
            }

    print("--- NODES ---")
    for nid, ndata in nodes.items():
        if ndata['value']:
            print(f"[{nid}] '{ndata['value']}' (style: {ndata['style'][:30]})")
            
    print("\n--- EDGES ---")
    for e in edges:
        s_val = nodes.get(e['source'], {}).get('value', e['source'])
        t_val = nodes.get(e['target'], {}).get('value', e['target'])
        print(f"[{e['id']}] '{e['value']}' : '{s_val}' -> '{t_val}'")

except Exception as e:
    print(f"Error parsing drawio: {e}")
