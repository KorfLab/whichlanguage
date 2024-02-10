while read name index; do
	if found=`grep $name unique.txt`
	then
	echo $found $index
	fi
done < names.txt