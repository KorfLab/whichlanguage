sort names.txt > names_sorted.txt
while read name index; do
    if found=`look $name names_sorted.txt`
    then
    echo $found $index
    fi
done < unique.txt