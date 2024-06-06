ls

cd-> path

mkdir -> new directory

rmdir -> remove an empty directory

rm filename -> remove file
rm -r directoryname -> remove directory and its files

cp sourcefile destfile
cp -r sourcedirectory destdirectory

mv oldname newname  -> move files
mv filename /path/to/dest

cat filename

more filename -> view file contents one screen at a time
less filename

head filename -> view beginning of a file
head -n 10 filename -> view first 10 lines
tail filename
tail -n 10 filename -> view last 10 lines

man ls -> display the manual page for a command

chmod 755 filename
chmod +x script.sh

ps
ps aux -> give detailed list of all processes

top

kill pid_num
kill -9 pid_num -> terminate a process forcefully by its id

ping -> check connectivity with host

ifconfig
ip addr show 

grep "search term" filename
grep -r "search term" /path/to/directory

find /path/to/search -name "filename"

sort filename

uniq filename

wc filename

