for f in tvision-py/include/tv/*.h; do h_file=$(basename $f | sed s/.h//); if [ ! -e "$h_file".i ]; then echo $h_file; fi; done
