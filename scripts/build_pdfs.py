#!/usr/bin/env python3
"""Build standalone manuscripts and validate logs/PDF text; --check is read-only."""
from pathlib import Path
import argparse, hashlib, json, os, re, shutil, subprocess
ROOT=Path(__file__).resolve().parents[1]
STEMS=('gamma_mds_active_uniform','terminal_cloud_staircase')
EPOCH='1791676800'

def run(args,**kw):return subprocess.run(args,check=True,text=True,**kw)
def pdf_text(path):return ''.join(run(['pdftotext',str(path),'-'],capture_output=True).stdout.split())
def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()
def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');args=p.parse_args()
 env=dict(os.environ,SOURCE_DATE_EPOCH=EPOCH,FORCE_SOURCE_DATE='1',TZ='UTC')
 records=[]
 for stem in STEMS:
  target=ROOT/'build'/('ci' if args.check else 'pdf')/stem;target.mkdir(parents=True,exist_ok=True)
  source=ROOT/f'{stem}.tex';built=target/f'{stem}.pdf';dest=ROOT/f'{stem}.pdf'
  run(['latexmk','-pdf','-interaction=nonstopmode','-halt-on-error','-file-line-error',
       '-outdir='+str(target),str(source)],cwd=ROOT,env=env,stdout=subprocess.DEVNULL)
  log=(target/f'{stem}.log').read_text(errors='replace')
  problems=re.findall(r'^.*(?:LaTeX Warning|Package \w+ Warning|Overfull \\[hv]box|Underfull \\[hv]box|undefined references|undefined citations).*$' ,log,re.M)
  if problems:raise RuntimeError('\n'.join(problems))
  if args.check:
   if not dest.is_file():raise RuntimeError(f'Missing tracked PDF: {dest.name}')
   if pdf_text(built)!=pdf_text(dest):raise RuntimeError(f'Rebuilt PDF text differs: {stem}')
  else:shutil.copyfile(built,dest)
  info=run(['pdfinfo',str(built)],capture_output=True).stdout
  pages=int(re.search(r'^Pages:\s+(\d+)',info,re.M).group(1))
  records.append({'source':source.name,'pdf':dest.name,'source_sha256':sha(source),'pdf_sha256':sha(dest),'pages':pages})
  print(f'{stem}: {pages} pages; warning-free build'+('; tracked text matches' if args.check else ''))
 if not args.check:
  (ROOT/'docs/pdf_manifest.json').write_text(json.dumps({'source_date_epoch':EPOCH,'manuscripts':records},indent=2)+'\n')
 return 0
if __name__=='__main__':raise SystemExit(main())
