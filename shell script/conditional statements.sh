echo "Enter the filename:"
read filename

if [ -e "$filename" ]; then
    echo "File exists."
    [ -r "$filename" ] && echo "File is readable." || echo "File is not readable."
    [ -w "$filename" ] && echo "File is writable." || echo "File is not writable."
    [ -e "$filename" ] && echo "File is executable." || echo "File is not executable."
else
    echo "File doesnot exist"

fi
