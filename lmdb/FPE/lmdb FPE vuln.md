# lmdb FPE漏洞

## Description

```
An issue was dicovered in py-lmdb 0.97.There is an FPE in the function mdb_env_open2 in lib/mdb.c for the env->me_psize variable.
```

## Version

version <=0.97

https://github.com/jnwatson/py-lmdb

## Vuln Detail

`mdb_env_read_header` function reads attributions of mdb file into  variable `meta`.When the `md_pad` field of `data.mdb` is set to 0,a divide-by-zero error exists in the `mdb_env_open2`.

```c
#define	mm_psize	mm_dbs[FREE_DBI].md_pad
static int ESECT
mdb_env_read_header(MDB_env *env, MDB_meta *meta)
{
	MDB_metabuf	pbuf;
	MDB_page	*p;
	MDB_meta	*m;
	int			i, rc, off;
	enum { Size = sizeof(pbuf) };

	for (i=off=0; i<NUM_METAS; i++, off += meta->mm_psize) {
		……
        //env->fd point to data.mdb,read the content of data.mdb to pbuf
		rc = pread(env->me_fd, &pbuf, Size, off);
		……
		p = (MDB_page *)&pbuf;
		……
		m = METADATA(p);
        ……
		if (off == 0 || m->mm_txnid > meta->mm_txnid)
          	//meta is assigned attributes of mdb file
			*meta = *m;
	}
	return 0;
}
```

`md_pad` is defined as `mm_psize`.

```c
static int ESECT
mdb_env_open2(MDB_env *env)
{
	……
	else {
        //me_psize is assigned meta.mm_dbs[0].md_pad
		env->me_psize = meta.mm_psize;
	}
	……
	env->me_maxpg = env->me_mapsize / env->me_psize; //FPE
	……
}
```

## Debug

```c
 RAX  0x10000000000
 RBX  0x694480 ◂— 0x300000004
 RCX  0x0
 RDX  0x0
 RDI  0x7efff5995010 ◂— 0x1beefc0de
 RSI  0x10000000000
 R8   0x4
 R9   0x0
 R10  0x1
 R11  0x246
 R12  0x0
 R13  0x1
 R14  0x7fffffff95f0 ◂— 0x0
 R15  0x7fffffff9560 ◂— 0x1beefc0de
 RBP  0x0
 RSP  0x7fffffff9560 ◂— 0x1beefc0de
 RIP  0x7ffff5cad0ac (mdb_env_open2+364) ◂— div    rcx
──────────────────────────────────────────────────────────[ DISASM ]───────────────────────────────────────────────────────────
 ► 0x7ffff5cad0ac <mdb_env_open2+364>    div    rcx
    ↓
 ► 0x7ffff5cad0ac <mdb_env_open2+364>    div    rcx

───────────────────────────────────────────────────────[ SOURCE (CODE) ]───────────────────────────────────────────────────────
In file: /home/yt360/yt/crashes/py-lmdb/lib/mdb.c
   4415 	env->me_nodemax = (((env->me_psize - PAGEHDRSZ) / MDB_MINKEYS) & -2)
   4416 		- sizeof(indx_t);
   4417 #if !(MDB_MAXKEYSIZE)
   4418 	env->me_maxkey = env->me_nodemax - (NODESIZE + sizeof(MDB_db));
   4419 #endif
 ► 4420 	env->me_maxpg = env->me_mapsize / env->me_psize;
   4421 
   4422 #if MDB_DEBUG
   4423 	{
   4424 		MDB_meta *meta = mdb_env_pick_meta(env);
   4425 		MDB_db *db = &meta->mm_dbs[MAIN_DBI];
───────────────────────────────────────────────────────────[ STACK ]───────────────────────────────────────────────────────────
00:0000│ r15 rsp  0x7fffffff9560 ◂— 0x1beefc0de
01:0008│          0x7fffffff9568 ◂— 0x0
02:0010│          0x7fffffff9570 ◂— 0x10000000000
03:0018│          0x7fffffff9578 ◂— 0x800000000
04:0020│          0x7fffffff9580 ◂— 0x0
... ↓
─────────────────────────────────────────────────────────[ BACKTRACE ]─────────────────────────────────────────────────────────
 ► f 0     7ffff5cad0ac mdb_env_open2+364
   f 1     7ffff5cae04f mdb_env_open+559
   f 2     7ffff5c9e781 env_new+705
   f 3     7ffff7182895
   f 4     7ffff709a333 PyObject_Call+67
   f 5     7ffff70f13a1 PyEval_EvalFrameEx+16865
   f 6     7ffff7225278 PyEval_EvalCodeEx+2008
   f 7     7ffff70ed029 PyEval_EvalCode+25
   f 8           402ca1
   f 9           403087
   f 10     7ffff75e4b97 __libc_start_main+231
```
## others
```
please send email to teamseri0us360@gmail.com if you have any questions.
```
