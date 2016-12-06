tips="[wshell~logice]#"
while true
do
    read -e -p $tips name
    comma=""
    array=($name)
    for(( i=2;i<${#array[@]};i++ ))
    do
        comma="${comma}"" ""${array[i]}"
    done
    #echo $tips ${array[0]} ${array[1]} $comma
    #echo $tips "$name"
    echo $tips
    python mstsc_command.py ${array[0]} ${array[1]} "'$comma'"
done
