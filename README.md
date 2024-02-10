Which Language
==============

Some languages are better suited for certain tasks. But which ones and for
which tasks?

+ [Matching Names](#matching-names)
+ [Parsing Tables](#parsing-tables)
+ [Parsing Complex Files](#parsing-complex-files)
+ [Interprocess Communication](#interprocess-communication)

## Matching Names ##

A common bioinformatics task is to cross-reference the names from two or more
files. At the outset, you must know if the relationships are one-to-one,
one-to-many, or many-to-many.

1. The names are unique in both lists
2. The names occur once in one list, but multiple times in the other list
3. The names occur multiple times in both lists

### Setup ###

Let's make some example lists with the `makelists.py` program. This creates a
master list of names `names.txt`, a subset containing unique names and values
`unique.txt`, and a subset containing names associated with multiple values
`multi.txt`. The following command makes 1000 names for the `names.txt` file.
Approximately 10% end up in `unique.txt` and `multi.txt` but multi is larger
because it has multiple values for each token.

```
python3 makelists.py 1000
ls -lrth
wc *.txt
less *.txt
```

### Shell: grep_merge1.sh ###

The `grep_merge1.sh` file has the following contents.

```bash
1  while read name index; do
2      if found=`grep $name unique.txt`
3      then
4      echo $found $index
5      fi
6  done < names.txt
```

Lines 1-6 performa a `while` loop that iterates over the `names.txt` file as
STDIN.

Line 1 splits each line into variables `name` and `index`.

Line 2 performs a `grep` looking for the name in `unique.txt`. If successful,
the `found` variable contains the line.

Line 4 prints the grep-matched line and the index from line 1.

The `grep` solution is simple and fast to type. For small files, this works
okay, but the overall solution is both slow and wasteful for 2 reasons.

1. `grep` is called many times
2. `grep` is a linear search

Let's examine what happens if the list is twice as large.

```
python3 makelists.py 2000
time sh grep_merge.sh
```

Not too surprising: it takes twice as long. That's what it means for a search
to be linear. The way the script is constructed, the outer `while` loop is the
larger file and the inner `grep` is the smaller file. What happens if we
reverse the two?

```
time sh grep_merge2.sh
```

That's clearly a lot faster. Why? It's the same number of comparisons either
way. Every line of one file must be compared to every line of the other file.
However `grep_merg2.sh` runs `grep` fewer times. Every time you run a program,
there is overhead from the operating system. Let's imagine a case with 10,000
names.

```
python3 makelists.py 10000
time sh grep_merge2.sh
```

It takes my computer around 5.9 seconds to cross-reference 10,000 names with
another 1,000 names, or about 1,724,137 comparisons per second. That may sound
fast, but if each list was 1 million items long, it would take about 1 week.

### Shell: look ###

If your data is unique, it can be sorted and searched efficiently with a binary
search. First, you must `sort` the data, then search it with `look`.

```bash
sort names.txt > names_sorted.txt
while read name index; do
    if found=`look $name names_sorted.txt`
    then
    echo $found $index
    fi
done < unique.txt
```

Despite the overhead of having to sort the file initially, the `look` strategy
is faster. 

```
time sh look_merge.sh
```

Even though `look` is better than `grep`, if you find yourself wanting to go
faster than `grep`, don't use `look`. There are better solutions than running
hundreds or thousands of shell commands.

### Python: linear ###

Here are several Python solutions. They are all faster than `grep` but they are
still linear searches.

| Program             |  MCS   | Notes
|:--------------------|-------:|:----------------
| `grep_merge1.py`    |   0.30 | outer file large
| `grep_merge2.py`    |   1.72 | outer file small
| `python_linear1.py` |   2.07 | outer file large
| `python_linear2.py` |   2.52 | outer file small
| `python_linear3.py` |  55.13 | memorize a file

### Python: dict ###

Dictionaries are sort of like binary searches in performance. As the size of
the data grows, dictionaries increasingly out-perform lists.

| Program             |  1e3  |  1e4  |   1e5  |   1e7  | 
|:--------------------|------:|------:|-------:|:-------|
| `grep_merge1.py`    | 3.129 | 34.02 | 57 min | 4 days |
| `grep_merge2.py`    | 0.355 | 5.881 | 10 min | 16 hrs |
| `python_linear1.py` | 0.119 | 4.603 |  8 min | 13 hrs |
| `python_linear2.py` | 0.088 | 4.234 |  7 min | 12 hrs |
| `python_linear3.py` | 0.045 | 0.223 | 18.33s | 31 min |
| `python_dict.py`    | 0.044 | 0.047 | 0.102s | 0.674s |

**STOP DOING LINEAR SEARCHES**

---------------------------

+ one to many
+ many to many
+ sql comparisons too?

## Parsing Tables ##

+ split()
+ csv.reader()

## Parsing Complex Files ##

Some files are meant to be human readable and not much thought has gone into
making them easy to read by machines.

Perl regex and dictionary are super easy.

## Inter-process Communication ##

Backticking in Perl is quick-n-dirty.


