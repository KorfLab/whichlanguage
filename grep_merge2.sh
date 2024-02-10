while read name index; do
	if found=`grep $name names.txt`
	then
	echo $found $index
	fi
done < unique.txt