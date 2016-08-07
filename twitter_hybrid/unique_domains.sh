python domain_extractor.py $1
sort $1_domains | uniq >> $1_domains_unique
