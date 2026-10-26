import sys,json,signal
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from parse_tb import load
import tree
FILES={'FY24':'input/TrialBal_FY_23-24.xlsx','FY25':'input/TrialBal_FY_24-25.xlsx','FY26':'input/TrialBal_FY_25-26.xlsx'}
def h(*a): raise TimeoutError
res={}
for fy,f in FILES.items():
    rows=load(f)
    seen=set()
    for x in rows:
        k=(x['name'],tuple(round(a,2) for a in x['v'])); x['second']=x['dup'] and k in seen; seen.add(k)
    tops=[k for k,x in enumerate(rows) if x['kind']=='P']
    for x in rows: x['type']=x['kind']; x['inc']=0; x['parent']=''
    for i,k in enumerate(tops):
        nxt=tops[i+1] if i+1<len(tops) else len(rows)
        sub=rows[k:nxt]
        signal.signal(signal.SIGALRM,h); signal.alarm(10)
        try:
            L,sk=tree.build(sub); ok=True
        except TimeoutError: ok=False
        signal.alarm(0)
        if ok:
            byr={x['r']:x for x in L}
            for x in sub:
                if x['r'] in byr:
                    x['inc']=1; x['parent']=byr[x['r']]['path'][-1] if byr[x['r']]['path'] else ''
                if x['r'] in sk: x['type']='X'
        else:
            last=x0=sub[0]['name']
            for x in sub[1:]:
                if x['kind']=='G': last=x['name']
                if x['kind']=='L':
                    if x['second']: x['type']='X'
                    else: x['inc']=1; x['parent']=last
            print(fy,'fallback for',sub[0]['name'])
        if len(sub)==1 and any(abs(a)>0.001 for a in sub[0]['v']): sub[0]['inc']=1
    # verify
    s=[round(sum(x['v'][t] for x in rows if x['inc']),2) for t in range(4)]
    print(fy,'included',sum(x['inc'] for x in rows),'sum',s)
    res[fy]=rows
os.makedirs('work',exist_ok=True); json.dump(res,open('work/tb_all.json','w'))
