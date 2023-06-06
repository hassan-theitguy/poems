import json
from collections import Counter

json_file = 'poems.json'
stats = {}

with open(json_file) as json_data:
    data = json.load(json_data)
    
    total_words=0
    unique_words=set()
    total_poems=0
    all_words=[]
    str_top_ten_words=""
    longest_poem=""
    longest_poem_count=0
    
    for poem in data:
    	total_poems+=1
    	
    	poem_words=[]
    	words=poem['title'].lower().split()
    	
    	poem_words+=words
    	total_words+=len(words)
    	unique_words.update(words)
    	all_words.extend(words)
    	
    	for line in poem['lines']:
    		words=line.lower().split()
    		
    		poem_words+=words
    		total_words+=len(words)
    		unique_words.update(words)
    		all_words.extend(words)
    
    	if len(poem_words) > longest_poem_count:
    		longest_poem_count=len(poem_words)
    		longest_poem=poem['title']
    
    stats['total_words']=total_words
    stats['unique_words']=len(unique_words)
    stats['total_poems']=total_poems
    stats['average_words']=round(total_words/total_poems)
    
    ignore = {'the','a','if','in','it','of','or','and','i','to','is','on','we','my','with','for','you','this','no','what','that','be','from','our','am'}
    words_counter=Counter(x for x in all_words if x not in ignore)
    top_ten_words = words_counter.most_common(10)
    
    for word, count in top_ten_words:
    	str_top_ten_words+=word+" ("+str(count)+" times)<br>"
    	
    stats['top_words']=str_top_ten_words
    
    longest_word = max(all_words, key=len)
    
    stats['longest_word']=longest_word
    stats['longest_poem']=longest_poem
    
stats_json = json.dumps(stats, indent=4)
print(stats_json)