#!/usr/bin/env python3
"""Structural, provenance, link and source/statement checks; not a proof checker."""
from pathlib import Path
import argparse, hashlib, json, re
ROOT=Path(__file__).resolve().parents[1]
STEMS=('gamma_mds_active_uniform','terminal_cloud_staircase')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def statements(text):
 out=[]
 pattern=r'\\begin\{(theorem|lemma|proposition|corollary)\}(?:\[([^\]]*)\])?(.*?)\\end\{\1\}'
 for m in re.finditer(pattern,text,re.S):
  lab=re.search(r'\\label\{([^}]+)\}',m.group(3))
  if not lab:raise ValueError('Unlabeled formal statement: '+str(m.group(2)))
  out.append({'label':lab.group(1),'kind':m.group(1),'title':m.group(2) or '',
              'statement_sha256':hashlib.sha256(m.group(0).encode()).hexdigest()})
 return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--sources-only',action='store_true');p.add_argument('--write-registry',action='store_true');args=p.parse_args()
 registry={};source_hashes={};count=0
 for stem in STEMS:
  text=(ROOT/f'{stem}.tex').read_text()
  labels=re.findall(r'\\label\{([^}]+)\}',text)
  if len(labels)!=len(set(labels)):raise ValueError('Duplicate labels: '+stem)
  refs=re.findall(r'\\(?:eqref|ref|autoref)\{([^}]+)\}',text)
  if set(refs)-set(labels):raise ValueError('Unresolved references: '+str(set(refs)-set(labels)))
  cited=set()
  for c in re.findall(r'\\cite(?:\[[^\]]*\])?\{([^}]+)\}',text):cited.update(x.strip() for x in c.split(','))
  bib=set(re.findall(r'\\bibitem\{([^}]+)\}',text))
  if cited!=bib:raise ValueError('Missing/unused bibliography: '+str(cited^bib))
  if re.search(r'\\(?:input|include)\{',text):raise ValueError('Manuscripts must be standalone')
  if text.count(r'\author{Christopher D. Long}')!=1:raise ValueError('Author mismatch')
  registry[f'{stem}.tex']=statements(text);count+=len(registry[f'{stem}.tex'])
  source_hashes[f'{stem}.tex']=sha(ROOT/f'{stem}.tex')
 # Full source hashes also detect edits to ambient hypotheses, definitions,
 # notation, or proofs outside the individually inventoried statement bodies.
 record={'status':'Analytic proofs supplied; no proof-assistant coverage claimed.',
         'source_sha256':source_hashes,'manuscripts':registry}
 regpath=ROOT/'docs/statement_registry.json'
 if args.write_registry:regpath.write_text(json.dumps(record,indent=2)+'\n')
 elif json.loads(regpath.read_text())!=record:raise ValueError('Statement/source registry is stale')
 archive=ROOT/'archive/v30/nonuniform_coverage_theorem_notes_v30.tex'
 expected=json.loads((ROOT/'archive/v30/provenance.json').read_text())
 if sha(archive)!=expected['sha256']:raise ValueError('The frozen v30 archive changed')
 for name in ['README.md','AGENTS.md','CITATION.cff','LICENSE','LICENSES/CC-BY-4.0.txt','LICENSES/MIT.txt','THEOREM_STATUS.md','FORMALIZATION_STATUS.md','FORMALIZATION_AUDIT.md']:
  if not (ROOT/name).is_file():raise ValueError('Missing '+name)
 for md in [*ROOT.glob('*.md'),*ROOT.glob('docs/*.md'),ROOT/'archive/v30/README.md',ROOT/'scripts/results/README.md']:
  for link in re.findall(r'\]\(([^)]+)\)',md.read_text()):
   if '://' not in link and not link.startswith(('#','mailto:')):
    path=(md.parent/link.split('#')[0])
    if not path.exists():raise ValueError(f'Broken local link in {md.name}: {link}')
 readme=(ROOT/'README.md').read_text()
 if r'\[' in readme or r'\(' in readme:raise ValueError('Use GitHub dollar-delimited mathematics')
 # GitHub README math must be self-contained and avoid unsupported macro definitions.
 for md in [ROOT/'README.md', ROOT/'archive/v30/README.md', ROOT/'scripts/results/README.md']:
  content=md.read_text()
  forbidden=re.search(r'\\(?:operatorname|DeclareMathOperator|DeclareRobustCommand|newcommand|renewcommand|providecommand|def|gdef)\b',content)
  if forbidden:raise ValueError(f'Unsupported/unexpanded README TeX macro in {md}: {forbidden.group(0)}')
 if re.search(r'^\s*[=\-]\s*$',readme,re.M):raise ValueError('Unsafe lone Markdown math line')
 if not args.sources_only:
  manifest=json.loads((ROOT/'docs/pdf_manifest.json').read_text())
  for row in manifest['manuscripts']:
   if sha(ROOT/row['source'])!=row['source_sha256'] or sha(ROOT/row['pdf'])!=row['pdf_sha256']:raise ValueError('PDF/source manifest is stale')
 print(f'PASS: {len(STEMS)} standalone manuscripts; {count} labeled statements; references, citations, archive, links'+('' if args.sources_only else ', PDF manifest'))
 return 0
if __name__=='__main__':raise SystemExit(main())
