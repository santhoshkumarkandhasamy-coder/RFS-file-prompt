import json,sys,collections
sys.setrecursionlimit(20000)
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from parse_tb import load
TOL=0.011
def build(rows):
    n=len(rows)
    zero=lambda v: all(abs(x)<TOL for x in v)
    key=lambda v: tuple(round(x,2) for x in v)
    fail=set(); gmemo={}
    def seq(p,rem,stop_at=None):
        # returns (end, kids) for nodes from p summing to rem; kids entries (p,e,t) or ('skip',p)
        if zero(rem) and (stop_at is None or p==stop_at): return (p,[])
        if p>=n or rows[p]['kind']=='P': return None
        k=(p,key(rem),stop_at)
        if k in fail: return None
        x=rows[p]
        if x['dup'] and x.get('second'):
            r=seq(p+1,rem,stop_at)
            if r: return (r[0],[('skip',p)]+r[1])
        opts=[]
        if x['kind']=='G':
            g=group(p)
            if g: opts.append(g)
        opts.append((p+1,None))
        for e,t in opts:
            r=seq(e,[a-b for a,b in zip(rem,x['v'])],stop_at)
            if r: return (r[0],[(p,e,t)]+r[1])
        if x['dup'] and not x.get('second'):
            r=seq(p+1,rem,stop_at)
            if r: return (r[0],[('skip',p)]+r[1])
        fail.add(k); return None
    def group(k):
        if k in gmemo: return gmemo[k]
        gmemo[k]=None
        if zero(rows[k]['v']): gmemo[k]=None; return None
        r=seq(k+1,rows[k]['v'])
        if r and r[1] and any(c[0]!='skip' for c in r[1]): gmemo[k]=(r[0],r[1])
        return gmemo[k]
    out=[]; skipped=[]
    def walk(kids,path):
        for c in kids:
            if c[0]=='skip': skipped.append(rows[c[1]]['r']); continue
            p,e,t=c; x=rows[p]
            if t is None:
                if zero(x['v']): continue
                out.append(dict(x,path=path))
            else: walk(t,path+[x['name']])
    tops=[k for k,x in enumerate(rows) if x['kind']=='P']
    for i,k in enumerate(tops):
        nxt=tops[i+1] if i+1<len(tops) else n
        if nxt==k+1:
            if not zero(rows[k]['v']): out.append(dict(rows[k],path=[]))
            continue
        r=seq(k+1,rows[k]['v'],stop_at=nxt)
        if r: walk(r[1],[rows[k]['name']])
        else: print('  FAIL PRIMARY',rows[k]['name'])
    return out,skipped
if __name__=='__main__':
    rows=load(sys.argv[1])
    seen=set()
    for x in rows:
        if x['dup']:
            k=(x['name'],tuple(round(a,2) for a in x['v']))
            x['second']= k in seen; seen.add(k)
    L,sk=build(rows)
    tot=[round(sum(x['v'][i] for x in L),2) for i in range(4)]
    print(sys.argv[1][-14:],'leaves',len(L),'tot',tot,'skipped rows',sk)
    json.dump(L,open(sys.argv[2],'w'))
