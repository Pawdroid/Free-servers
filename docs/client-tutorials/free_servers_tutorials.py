"""Shared, data-only tutorial enrichment for the four Free-servers publishers.

No network requests, node parsing or publication side effects.
"""
from pathlib import Path
import html
import json
import re
from functools import lru_cache

ROOT = Path(__file__).resolve().parent
REPO = 'https://github.com/Pawdroid/Free-servers/blob/main/docs/client-tutorials/'

@lru_cache(maxsize=1)
def data():
    return json.loads((ROOT / 'catalog.json').read_text(encoding='utf-8'))

@lru_cache(maxsize=16)
def locale(lang):
    return json.loads((ROOT / 'locales' / (lang + '.json')).read_text(encoding='utf-8'))

def entry_for(label):
    items = [x for x in data()['clients'] if label in x['names']]
    if len(items) != 1:
        raise ValueError('Unknown or duplicate tutorial client: ' + label)
    return items[0]

def official(item, lang):
    return item.get('official_zh') if lang == 'zh' and item.get('official_zh') else item.get('official')

def links(item, lang):
    loc = locale(lang)
    result = []
    off = official(item, lang)
    if off:
        result.append((loc['official'] + ' [' + off['language'] + ']', off['url']))
    result.append((loc['quick'], REPO + lang + '.md#' + item['id']))
    return result

def md_cell(item, lang):
    return ' · '.join('['+label+']('+url+')' for label,url in links(item,lang)) + '<br>' + item['format']

def html_cell(item, lang):
    return '<td data-client-tutorial="'+item['id']+'" style="border:1px solid #d1d5db;padding:0.7em 0.85em;vertical-align:top;min-width:12em;overflow-wrap:anywhere;">' + ' · '.join('<a href="'+html.escape(url,quote=True)+'">'+html.escape(label)+'</a>' for label,url in links(item,lang)) + '<br><small>'+html.escape(item['format'])+'</small></td>'

def enhance_markdown(text, lang):
    if 'docs/client-tutorials/'+lang+'.md#' in text:
        raise ValueError('Tutorials already present')
    loc=locale(lang); lines=text.splitlines(keepends=True); count=0; tables=0; out=[]; pos=0
    while pos<len(lines):
        if lines[pos].startswith('|'):
            end=pos
            while end<len(lines) and lines[end].startswith('|'):end+=1
            group=lines[pos:end]
            matches=[re.match(r'^\|\s*\*\*(.+?)\*\*\s*\|',l) for l in group[2:]]
            is_client=bool(matches) and all(m and any(m.group(1) in x['names'] for x in data()['clients']) for m in matches)
            if is_client:
                assert len(group)>=3
                def add(line,cell):
                    m=re.fullmatch(r'(.*)\|([ \t]*)(\r?\n)?',line)
                    assert m
                    return m.group(1)+'| '+cell+' |'+(m.group(3) or '')
                out.extend([add(group[0],loc['tutorial']),add(group[1],'---')])
                for line,m in zip(group[2:],matches):out.append(add(line,md_cell(entry_for(m.group(1)),lang)));count+=1
                tables+=1
            else:out.extend(group)
            pos=end
        else:
            line=lines[pos]
            if 'https://acl4ssr-sub.github.io' in line:line=loc['privacy']+'\n'
            out.append(line);pos+=1
    assert (count,tables)==(46,6),(count,tables)
    return ''.join(out)

def enhance_html(text, lang):
    if 'data-client-tutorial=' in text:raise ValueError('Tutorials already present')
    loc=locale(lang);total=0;tables=0
    def replace_table(match):
        nonlocal total,tables
        block=match.group(0);rows=re.findall(r'<tr\b[^>]*>.*?</tr>',block,re.S|re.I)
        items=[]
        for row in rows:
            cells=re.findall(r'<td\b[^>]*>(.*?)</td>',row,re.S|re.I)
            if not cells:continue
            name=html.unescape(re.sub('<[^>]+>','',cells[0])).strip()
            try:item=entry_for(name)
            except ValueError:return block
            items.append((row,item))
        if not items:return block
        heads=re.findall(r'<tr\b[^>]*>.*?</tr>',block,re.S|re.I)
        head=next(r for r in heads if '<th' in r)
        newhead=re.sub(r'</tr>', '<th style="border:1px solid #d1d5db;padding:0.7em 0.85em;text-align:start;min-width:12em;">'+html.escape(loc['tutorial'])+'</th></tr>',head,count=1,flags=re.I)
        block=block.replace(head,newhead,1)
        for row,item in items:
            block=block.replace(row,re.sub(r'</tr>',lambda m:html_cell(item,lang)+'</tr>',row,count=1,flags=re.I),1);total+=1
        tables+=1
        return block
    result=re.sub(r'<table\b[^>]*>.*?</table>',replace_table,text,flags=re.S|re.I)
    assert (total,tables)==(46,6),(total,tables)
    result=re.sub(r'<p\b[^>]*>(?:(?!</p>).)*https://acl4ssr-sub\.github\.io(?:(?!</p>).)*</p>',lambda m:'<p style="margin:0.8em 0;">'+html.escape(loc['privacy'])+'</p>',result,flags=re.S|re.I)
    return result

def render_guide(lang):
    loc=locale(lang);out=['# '+loc['title'],'',loc['intro'],'',loc['privacy'],'']
    out.extend('['+x['names'][0]+'](#'+x['id']+')' for x in data()['clients'])
    out.append('')
    for item in data()['clients']:
        out += ['<a id="'+item['id']+'"></a>','', '## '+item['names'][0],'','**'+loc['format']+':** '+item['format'],'']
        for note in item.get('notes',[]):out += [loc[note],'']
        if not official(item,lang):out += [loc['limited'],'']
        steps=[loc[item['workflow']]]
        if item['workflow']!='router':steps.append(loc['select'])
        steps.append(loc['troubleshoot'])
        out += ['### '+loc['steps'],'']+[str(i+1)+'. '+s for i,s in enumerate(steps)]+['',loc['limitations'],'']
        off=official(item,lang)
        if off:out += ['['+loc['official']+' ['+off['language']+']]('+off['url']+')','']
        if not off and any(r.get('kind')!='source' for r in item.get('reference',[])):out += [loc['fallback'],'']
        for ref in item.get('reference',[]):out += ['- ['+loc[ref.get('kind','reference')]+' ['+ref['language']+']]('+ref['url']+')']
        out += ['']
    return '\n'.join(out).rstrip()+'\n'

def write_guides():
    # Only generated tutorial documents inside this public docs directory.
    for lang in data()['languages']:
        target=ROOT/(lang+'.md');value=render_guide(lang)
        if not target.exists() or target.read_text(encoding='utf-8')!=value:
            target.write_text(value,encoding='utf-8')
