def solve():
	_, songs = I(), MIIS()
	seq_start, max_seq = 0, 0
	uniq_songs = set()

	for song in songs:
		if song in uniq_songs:
			dup_index = songs.index(song, seq_start)
			uniq_songs.difference_update(songs[seq_start:dup_index])
			seq_start = dup_index + 1
		uniq_songs.add(song)
		max_seq = max(max_seq, len(uniq_songs))
		not LOCAL and log(f"Song {song}: Start:{seq_start}, MaxLen:{max_seq}, UniqSongs:{uniq_songs}")
	print(max_seq)


# source of cringe, don't watch below this line!
import sys

LOCAL = False


try: 
	sys.stdin=open('in.txt','r')
	# sys.stdout=open('out.txt', 'w')
	LOCAL = True
	def log(*a): print(*a,file=sys.stderr)
	from time import time
	start = time()
except FileNotFoundError:	
	pass

I=input
MIIS=lambda:[*map(int,I().split())]

solve()

if LOCAL:
	log(f'Finished in {time()-start:.3f}sec')