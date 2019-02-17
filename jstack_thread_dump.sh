for ((a=1; a <= 60; a++)); do jstack 21819 > thread-dump.$a; sleep 1; echo $a; done
